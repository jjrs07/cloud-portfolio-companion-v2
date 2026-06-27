# # [Project Title: e.g., Serverless Generative AI Resume Analyzer]

<!-- 
GUIDE COMMENT:
Welcome to your project's README template! Fill out the placeholders bracketed in [brackets]. 
Use the inline comments to guide your text. Remove this guide comment before publishing your project on GitHub.
-->

A production-inspired, highly secure [brief description of what your application does, e.g., Serverless Generative AI application that allows users to upload PDF resumes and receive structured parsing metrics and improvement feedback using Amazon Bedrock].

---

## 📊 Project Specifications

* **Difficulty:** [e.g., Intermediate / Advanced]
* **Time to Build:** [e.g., 4 Hours]
* **Estimated AWS Cost:** [e.g., $0.00 Free Tier / ~$0.02 pay-as-you-go Bedrock tokens]
* **AWS Services Used:** [e.g., Amazon S3, Amazon API Gateway, AWS Lambda, Amazon Bedrock, Amazon CloudWatch]
* **Demonstrated Skills:** [e.g., Serverless Architecture, Infrastructure as Code (IaC), Least-Privilege IAM Access, API Development, GenAI Prompt Engineering]

---

## 📐 System Architecture

<!-- 
GUIDE COMMENT:
Replace the placeholder image link below with your actual architecture diagram. 
We recommend saving your diagram as a clean SVG or PNG inside an `images/` directory in your repo.
-->

![System Architecture Diagram](images/architecture_diagram.png)

### Architectural Data Flow:
1. **Frontend Hosting:** [e.g., The client static files are hosted securely on Amazon S3 and distributed globally via CloudFront CDN to minimize latency].
2. **API Endpoint Router:** [e.g., Web clients perform HTTP POST requests with base64 encoded PDFs to Amazon API Gateway (HTTP API) with CORS protections enabled].
3. **Compute Backend:** [e.g., API Gateway invokes an asynchronous AWS Lambda function running Node.js/Python, which extracts raw text from the document payload].
4. **AI Generation:** [e.g., Lambda invokes the Amazon Bedrock API, sending the resume text alongside a custom prompt to the Llama 3 8B Instruct model to receive JSON structured feedback].

---

## 🔒 Security Best Practices Implemented

<!-- 
GUIDE COMMENT:
Hiring managers scan portfolios specifically to find security awareness. Detail your security controls here.
-->

* **Zero Public Database Exposure:** [e.g., The Amazon RDS MySQL database is provisioned in isolated private subnets, accepting traffic ONLY from the EC2 web server security group].
* **SSM over SSH Security:** [e.g., The EC2 instances are administered passwordless using AWS Systems Manager (SSM) Session Manager. Port 22 is completely closed in all Security Groups, eliminating external SSH brute force attacks].
* **Least-Privilege IAM Access Policy:** [e.g., The Lambda function executor role is constrained with strict IAM permission boundaries, granting `bedrock:InvokeModel` access ONLY to the Llama 3 8B model resource].
* **Secure Environment Variables:** [e.g., Database credentials and API tokens are retrieved dynamically at runtime from AWS Secrets Manager instead of being hardcoded in version control].

---

## 🛠️ Step-by-Step Deployment Guide

<!-- 
GUIDE COMMENT:
Provide copy-pasteable commands so other builders can replicate your work. 
-->

### Prerequisites:
* AWS CLI configured with administrator credentials.
* Node.js / Python installed locally.
* [e.g., AWS SAM CLI or Terraform installed].

### Deployment Steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/[your-repo-name].git
   cd [your-repo-name]
   ```

2. **Validate the Infrastructure Template:**
   ```bash
   sam validate --template template.yaml
   ```

3. **Deploy the Resources:**
   ```bash
   sam build && sam deploy --guided
   ```
   *Fill out the parameter prompts: Stack Name, AWS Region, CORS origin URLs, and list ID variables.*

4. **Verify the Deployment:**
   ```bash
   # Retrieve the public HTTP API endpoint URL
   aws cloudformation describe-stacks --stack-name [your-stack-name] --query "Stacks[0].Outputs"
   ```

---

## ⚙️ "What If It Breaks?" (Troubleshooting Scenarios)

<!-- 
GUIDE COMMENT:
 Hacking things together is easy; troubleshooting them is what senior developers do. 
 Describe real obstacles you hit during this build and how you resolved them.
-->

### Scenario 1: Web Client blocked by CORS policy
* **The Error:** Browser console displays `Access to fetch at 'https://api.execute-api...' from origin '...' has been blocked by CORS policy`.
* **The Root Cause:** The API Gateway configuration was missing the appropriate CORS header maps, or the backend Lambda response structure failed to return matching Access-Control-Allow-Origin headers.
* **The Resolution:** Updated the HTTP API Gateway route configuration to allow origin headers and configured the Lambda handler's successful/error response structure to explicitly return:
  ```json
  "headers": {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Allow-Methods": "POST,OPTIONS"
  }
  ```

### Scenario 2: Lambda Execution Timeout during Bedrock Inference
* **The Error:** API Gateway returns `500 Internal Server Error`, and CloudWatch logs show `Task timed out after 3.00 seconds`.
* **The Root Cause:** Amazon Bedrock takes 4-6 seconds to run the prompt and stream back token responses, which exceeded the default 3-second Lambda execution timeout.
* **The Resolution:** Increased the Lambda timeout parameter inside `template.yaml` (under Properties) from `3` to `15` seconds to allow sufficient head-room for model inference.

---

## 📈 Cost Awareness & Optimization

<!-- 
GUIDE COMMENT:
Show hiring managers you understand cloud financial operations (FinOps) by documenting cost budgets.
-->

* **AWS Billing Alarm Setup:** A CloudWatch Billing Alarm is configured at **$5.00 USD** with an Amazon SNS email subscription to prevent unexpected billing slip-ups.
* **Resource Cleanup Script:** To prevent continuous billing, run this deletion cleanup command immediately after testing the deployment:
  ```bash
  aws cloudformation delete-stack --stack-name [your-stack-name]
  ```

---

## 🗣️ STAR Technical Interview Script

<!-- 
GUIDE COMMENT:
This section helps you prepare for questions about this project in job interviews. 
Customize these answers to match your personal experience.
-->

* **Situation:** I wanted to gain hands-on experience building production-grade serverless applications on AWS, integrating Generative AI features while enforcing modern corporate security baselines.
* **Task:** I designed, developed, and deployed an automated Serverless AI Resume Analyzer that parses file uploads and calls LLMs for feedback, ensuring zero public server exposure and zero hardcoded credentials.
* **Action:** I configured API Gateway HTTP endpoints, wrote a Node.js/Python Lambda function using Bedrock's API, secured the execution environment using strict IAM least-privilege resource roles, and managed the entire infrastructure declaratively via AWS CloudFormation (IaC).
* **Result:** I successfully deployed a scalable, pay-as-you-go portfolio application with zero fixed monthly fees. I also documented the build and resolved CORS/Lambda timeout bugs, which helped me gain a deep, operational understanding of serverless data flows.

---

*Project built under the guidance of **Build Your First Cloud Portfolio** by James Santos.*
