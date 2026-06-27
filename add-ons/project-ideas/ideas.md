# 30 Cloud Portfolio Project Ideas

Never ask yourself, *"What should I build next?"* again. This compilation contains 30 curated project blueprints sorted into three difficulty tiers. Each blueprint outlines the project objective, target AWS services, and a core security constraint to ensure you build to production-grade standards.

---

## 🟢 Tier 1: Foundations, Automation & Operations (Beginner)
*Focus: Command Line Interface (CLI), Shell Scripting, IAM boundaries, and basic operational alerts.*

### 1. S3 Object Lifecycle Cleaner
* **Objective:** Automatically purge old logs or temp files from S3 buckets using lifecycle rules and write a Bash/Python script to verify cleanup.
* **Services:** Amazon S3, AWS CLI, IAM.
* **Security Constraint:** The runner script must execute under an IAM User/Role possessing read/write permissions strictly mapped to that single bucket.

### 2. CloudWatch to Slack Alert Notification Pipeline
* **Objective:** Push real-time billing alarms or EC2 status notifications to a private Slack channel.
* **Services:** CloudWatch, SNS, Lambda (Python), Slack Webhook.
* **Security Constraint:** Encrypt the Slack webhook URL inside AWS Systems Manager (SSM) Parameter Store as a SecureString.

### 3. IAM Policy Compliance Auditor
* **Objective:** Write a script that scans your AWS account and lists any IAM policies containing wildcard permissions (`Resource: "*"`) or public exposure rules.
* **Services:** IAM, AWS CLI / Boto3 SDK.
* **Security Constraint:** The audit tool must run under a read-only role (`SecurityAudit` managed policy).

### 4. Automated EC2 Image (AMI) Cleanup Tool
* **Objective:** Clean up unused AMIs and orphaned EBS snapshots older than 30 days to optimize storage costs.
* **Services:** EC2, Lambda, CloudWatch Events (EventBridge).
* **Security Constraint:** The Lambda execution role must not have permission to delete volumes that are currently attached or tagged as `prod-retain`.

### 5. S3 Public Access Auditor
* **Objective:** Scan all S3 buckets in your account and trigger a high-severity alert if public access is enabled on any bucket.
* **Services:** S3, EventBridge, Lambda, SNS.
* **Security Constraint:** Enable S3 Block Public Access at the account level during deployment to prevent accidental overrides.

### 6. CloudTrail Event Log Dashboard
* **Objective:** Stream CloudTrail logs to a CloudWatch log group and create a dashboard tracking root login attempts and console activity.
* **Services:** AWS CloudTrail, CloudWatch Logs, SNS.
* **Security Constraint:** CloudTrail logs must be encrypted with an AWS KMS customer-managed key.

### 7. Automated EC2 Auto-Start/Auto-Stop Scheduler
* **Objective:** Automatically shut down EC2 development instances outside business hours (e.g., 7 PM to 7 AM) to save running costs.
* **Services:** EC2, EventBridge scheduler, Lambda.
* **Security Constraint:** The Lambda script can only stop/start instances containing the tag `Env: Dev`.

### 8. AWS Config Compliance Monitor
* **Objective:** Set up AWS Config rules to monitor if EBS volumes are encrypted by default, alerting via SNS if non-compliant volumes are detected.
* **Services:** AWS Config, CloudWatch Alarms, SNS.
* **Security Constraint:** Restrict SNS topic policy so only AWS Config can publish to it.

### 9. Multi-Region S3 Backup Sync
* **Objective:** Replicate S3 objects dynamically to a backup bucket located in a different geographical region.
* **Services:** S3 Cross-Region Replication (CRR), IAM.
* **Security Constraint:** Enable S3 Versioning on both source and target buckets, and enforce KMS bucket-key encryption.

### 10. CLI Budget Cost Alarm Setup
* **Objective:** Automate the provisioning of multiple cost alarms using the AWS CLI and a JSON configuration file.
* **Services:** AWS CLI, AWS Budgets, SNS.
* **Security Constraint:** Enforce MFA (Multi-Factor Authentication) on the root billing credential.

---

## 🟡 Tier 2: Infrastructure, Networking & Containers (Intermediate)
*Focus: Custom VPC configurations, Security Groups, Load Balancing, Containers, and SSL/TLS.*

### 11. Secure Multi-Tier VPC with Isolated Database
* **Objective:** Host a web app inside a custom VPC with public subnets for the load balancer, private subnets for web servers, and isolated subnets for databases.
* **Services:** VPC, EC2, RDS (MySQL), ALB.
* **Security Constraint:** The RDS database subnet must have no Route Table association with an Internet Gateway, accepting connections strictly from the EC2 security group.

### 12. Bastion-less Private EC2 Administration
* **Objective:** Administer EC2 instances located in private subnets without deploying a public bastion host.
* **Services:** Systems Manager (SSM) Session Manager, EC2, IAM.
* **Security Constraint:** Completely close Port 22 SSH in all Security Groups. Access instances strictly via HTTPS through SSM Session Manager.

### 13. Dockerized Web App on ECS Fargate
* **Objective:** Package a Python/Node.js web application into a Docker container and run it on Amazon ECS Fargate.
* **Services:** ECS Fargate, ECR, ALB, Route 53.
* **Security Constraint:** Run ECS tasks inside private subnets, exposing them only via the Application Load Balancer in the public subnet.

### 14. Secure Static Website with CloudFront and WAF
* **Objective:** Host a static HTML site on S3 securely behind a CloudFront CDN edge cache with AWS WAF protection.
* **Services:** S3, CloudFront, ACM (SSL), Route 53, AWS WAF.
* **Security Constraint:** Use Origin Access Control (OAC) to completely block public read access to the S3 bucket, allowing access only via CloudFront.

### 15. Auto-Scaling EC2 Web Server Fleet
* **Objective:** Set up an Auto Scaling group that scales EC2 instances horizontally based on average CPU utilization.
* **Services:** EC2, ALB, Auto Scaling, CloudWatch.
* **Security Constraint:** Instances must boot using a custom AMI pre-configured with security patches and run as non-root users.

### 16. Serverless REST API with API Gateway and DynamoDB
* **Objective:** Build a serverless CRUD API that reads and writes data to a NoSQL database.
* **Services:** API Gateway, Lambda, DynamoDB.
* **Security Constraint:** Enable CORS with strict origin mapping, and validate input parameters in API Gateway before invoking Lambda.

### 17. AWS Client VPN Tunnel to Private Subnets
* **Objective:** Establish a secure VPN connection from your local computer to access databases and servers in your private VPC subnets.
* **Services:** AWS Client VPN, Directory Service, VPC.
* **Security Constraint:** Authenticate VPN clients using mutual authentication (certificates) managed via ACM.

### 18. Multi-VPC Transit Gateway Network
* **Objective:** Connect multiple independent VPCs (e.g., Dev, Testing, Shared Services) together using a hub-and-spoke model.
* **Services:** Transit Gateway, VPC route tables.
* **Security Constraint:** Enforce security boundaries so the Dev VPC cannot route traffic directly to the Prod VPC.

### 19. Dynamic DNS Update Pipeline
* **Objective:** Automatically update Route 53 DNS records whenever an EC2 instance is launched or stopped.
* **Services:** EC2, EventBridge, Lambda, Route 53.
* **Security Constraint:** Grant Lambda edit access restricted strictly to the targeted hosted zone ID.

### 20. S3 Bucket Encryption with Customer-Managed KMS Keys
* **Objective:** Enforce server-side encryption on S3 using a key you manage, logging all decryptions in CloudTrail.
* **Services:** S3, Key Management Service (KMS), CloudTrail.
* **Security Constraint:** The KMS key policy must restrict decryption actions strictly to specific authorized IAM roles.

---

## 🔴 Tier 3: Serverless, Microservices & Generative AI (Advanced)
*Focus: Event-driven workflows, machine learning integration, LLM prompts, and automated pipelines.*

### 21. Serverless PDF Text Extractor
* **Objective:** Automatically extract text from PDF documents uploaded to S3 and save the results as text files.
* **Services:** S3, Lambda, Amazon Textract.
* **Security Constraint:** Encrypt output text files inside the destination bucket using S3 Managed Keys (SSE-S3).

### 22. Serverless Generative AI Chatbot
* **Objective:** Build a web-based chatbot that queries an LLM to answer technical questions and saves conversation histories.
* **Services:** S3 (Client), API Gateway, Lambda, Amazon Bedrock (Llama 3), DynamoDB.
* **Security Constraint:** Restrict DynamoDB reads/writes strictly to the authenticated user's session ID using DynamoDB Fine-Grained Access Control.

### 23. AI-Powered Image Generator API
* **Objective:** Expose an API endpoint that generates custom images based on text prompts using Stable Diffusion.
* **Services:** API Gateway, Lambda, Amazon Bedrock (Stable Diffusion), S3.
* **Security Constraint:** Apply API Gateway API Key authorization and rate-limiting throttling rules to prevent resource exhaustion.

### 24. Serverless Video/Audio Transcriber
* **Objective:** Transcribe audio files automatically upon upload to S3 and email the text transcript to the user.
* **Services:** S3, Lambda, Amazon Transcribe, Amazon SES (Simple Email Service).
* **Security Constraint:** Restrict SES execution permissions so only verified domains can receive transcription outputs.

### 25. Automated ECS CI/CD Deployment Pipeline
* **Objective:** Automatically build, test, and deploy containerized code changes to ECS Fargate whenever commits are pushed to GitHub.
* **Services:** GitHub Actions, ECS Fargate, ECR, AWS CodeDeploy.
* **Security Constraint:** Authenticate GitHub Actions with AWS using OpenID Connect (OIDC) instead of storing permanent IAM credentials.

### 26. RAG (Retrieval-Augmented Generation) Search Engine
* **Objective:** Build a search engine that queries internal documents and provides accurate answers using a vector database.
* **Services:** Amazon Bedrock, OpenSearch Serverless (Vector Engine), S3, Lambda.
* **Security Constraint:** Enforce strict VPC endpoint transit for all OpenSearch API calls, keeping database traffic private.

### 27. Serverless API Rate Limiter
* **Objective:** Protect a public Lambda backend from DDoS attacks using rate-limiting keys.
* **Services:** API Gateway, Lambda, AWS WAF.
* **Security Constraint:** Apply an AWS WAF rate-limiting rule block that restricts requests to 100 per 5-minute interval per IP address.

### 28. Event-Driven Email Marketing Funnel
* **Objective:** Build a serverless webhook receiver that processes checkouts and sends personalized follow-up sequences.
* **Services:** API Gateway, Lambda, DynamoDB, Amazon SES.
* **Security Constraint:** Validate payment payload signatures (HMAC SHA-256) inside the Lambda handler before queuing emails.

### 29. Sentiment Analysis Pipeline for Reviews
* **Objective:** Stream customer reviews in real-time, determine their sentiment (Positive/Negative), and visualize trends.
* **Services:** Amazon Kinesis, Firehose, Lambda, Amazon Comprehend, S3.
* **Security Constraint:** The Kinesis stream must encrypt all data in transit using TLS 1.2+ and at rest using KMS.

### 30. WAF SQL-Injection Guard for Serverless Apps
* **Objective:** Protect an API Gateway backend from SQL injection and Cross-Site Scripting (XSS) payloads.
* **Services:** API Gateway, Lambda, AWS WAF.
* **Security Constraint:** Enable WAF rulesets for Core Rule Set (CRS) and SQL database injection checks, blocking malicious requests at the edge.
