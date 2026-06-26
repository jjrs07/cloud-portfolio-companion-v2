import json
import os
import boto3

def lambda_handler(event, context):
    # Enforce Cross-Origin Resource Sharing (CORS) headers for frontend browser fetch calls
    cors_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization",
        "Access-Control-Allow-Methods": "OPTIONS,POST"
    }
    
    # Handle preflight OPTIONS requests from browser
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": ""
        }
        
    try:
        # Parse payload
        body = json.loads(event.get("body", "{}"))
        resume_text = body.get("resume", "").strip()
        job_desc = body.get("job_description", "").strip()
        
        if not resume_text or not job_desc:
            return {
                "statusCode": 400,
                "headers": cors_headers,
                "body": json.dumps({"error": "Missing resume or job description parameters."})
            }
            
        # Initialize Bedrock Client (invoking in us-east-1 where models are widely enabled)
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        
        # Structure LLM prompt
        prompt = f"""
        You are an expert technical recruiter. Analyze the following candidate resume text against the target job description.
        Identify missing keywords, missing technical skills, and provide exactly 3 actionable bullet points to optimize the resume.
        
        Resume:
        {resume_text}
        
        Job Description:
        {job_desc}
        """
        
        # Meta Llama 3 execution structure
        native_request = {
            "prompt": prompt,
            "max_gen_len": 512,
            "temperature": 0.5,
            "top_p": 0.9
        }
        
        # Invoke LLM
        response = bedrock.invoke_model(
            modelId="meta.llama3-8b-instruct-v1:0",
            body=json.dumps(native_request)
        )
        
        # Parse output stream
        response_body = json.loads(response.get("body").read().decode("utf-8"))
        analysis_result = response_body.get("generation", "Error: No generation found.")
        
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({"analysis": analysis_result})
        }
        
    except Exception as e:
        print(f"Serverless Error: {e}")
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"error": f"Internal Server Error: {str(e)}"})
        }