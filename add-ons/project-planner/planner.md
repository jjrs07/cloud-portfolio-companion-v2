# Cloud Project Planning Worksheet

Use this worksheet to plan your cloud portfolio projects before you provision resources or write code. Planning upfront helps you avoid security vulnerabilities, architectural errors, and unexpected billing surprises.

---

## 📅 Project Details

* **Project Name:** __________________________________________________
* **Author / Builder:** __________________________________________________
* **Target Start Date:** ____ / ____ / ________
* **Target Launch Date:** ____ / ____ / ________

---

## 🎯 Phase 1: Objective & Scope

### 1. What problem does this application solve?
*(e.g., "Manual resume review is slow for hiring managers. This app automates feedback using serverless AI.")*
________________________________________________________________________________
________________________________________________________________________________

### 2. Who is the target user?
*(e.g., "Aspiring cloud professionals looking for resume feedback.")*
________________________________________________________________________________

### 3. What is the core architectural goal?
*(e.g., "Build a serverless, zero-fixed-cost application utilizing pay-as-you-go AWS services.")*
________________________________________________________________________________

---

## 📐 Phase 2: Architectural Mapping

Complete the checklist below to define the AWS services you will use across the **6 Core Pillars**:

* `[ ]` **Compute:** `[ ]` AWS Lambda • `[ ]` Amazon EC2 • `[ ]` ECS Fargate • `[ ]` EKS Kubernetes
* `[ ]` **Storage:** `[ ]` Amazon S3 • `[ ]` EBS Volume • `[ ]` EFS File System
* `[ ]` **Database:** `[ ]` Amazon RDS (Engine: ________) • `[ ]` DynamoDB • `[ ]` Aurora Serverless
* `[ ]` **Networking:** `[ ]` VPC • `[ ]` API Gateway • `[ ]` CloudFront CDN • `[ ]` Route 53 • `[ ]` ALB
* `[ ]` **Security:** `[ ]` IAM Roles • `[ ]` AWS Secrets Manager • `[ ]` AWS WAF • `[ ]` ACM SSL Certificates
* `[ ]` **Operations:** `[ ]` CloudWatch Alarms • `[ ]` Amazon SNS • `[ ]` AWS CloudTrail • `[ ]` AWS Budgets

---

## 🔒 Phase 3: Security & Network Zoning

### 1. Subnet Zoning Plan (VPC Projects)

If your project utilizes a custom VPC, map your subnets below:

| Subnet Name | IPv4 CIDR Block | Type (Public / Private / Isolated) | Services Hosted |
| :--- | :--- | :--- | :--- |
| *e.g., Public Subnet A* | *10.0.1.0/24* | *Public (Internet Gateway Router)* | *ALB, NAT Gateway* |
| *e.g., Private DB Subnet A* | *10.0.3.0/24* | *Isolated (No Internet Router)* | *Amazon RDS MySQL Instance* |
| | | | |
| | | | |
| | | | |

### 2. Security Group Rule Matrix

Define the inbound and outbound traffic boundaries between your resources:

| Security Group ID | Source / Destination | Protocol & Port Range | Rule Description |
| :--- | :--- | :--- | :--- |
| *e.g., sg-web-server* | *0.0.0.0/0 (Inbound)* | *TCP / Port 443 (HTTPS)* | *Allow secure HTTPS web traffic from the internet* |
| *e.g., sg-database* | *sg-web-server (Inbound)* | *TCP / Port 3306 (MySQL)* | *Allow DB traffic ONLY from the EC2 web server* |
| | | | |
| | | | |
| | | | |

---

## 🔑 Phase 4: Least-Privilege IAM Permission Map

Define the exact actions each execution role requires. Do NOT use wildcard admin permissions (`*:*`).

| IAM Role Name | Target AWS Service | Allowable Actions (API Calls) | Resource Scope (ARN) |
| :--- | :--- | :--- | :--- |
| *e.g., LambdaBedrockInvoker* | *Amazon Bedrock* | *`bedrock:InvokeModel`* | *`arn:aws:bedrock:us-east-1::foundation-model/llama3-8b`* |
| *e.g., EC2BackupExecutor* | *Amazon S3* | *`s3:PutObject`* | *`arn:aws:s3:::my-portfolio-backup-bucket/*`* |
| | | | |
| | | | |
| | | | |

---

## 💸 Phase 5: FinOps Budgeting Worksheet

Calculate your estimated monthly AWS bill using a simple pay-as-you-go math check:

| AWS Service | Billing Unit (e.g., GB stored, Lambda runs) | Estimated Usage | Unit Price | Monthly Cost Estimate |
| :--- | :--- | :--- | :--- | :--- |
| *e.g., Amazon S3* | *GB / Month* | *2 GB stored* | *$0.023 / GB* | *$0.05* |
| *e.g., AWS Lambda* | *Requests & GB-seconds* | *10,000 requests / month* | *Free Tier (under 1M)* | *$0.00* |
| *e.g., Amazon Bedrock* | *Tokens (Input/Output)* | *100 runs (approx. 200K tokens)* | *$0.00015 / 1K tokens* | *$0.03* |
| | | | | **Total: $0.08** |

### Budget Control Strategy:
* **Billing Alarm Threshold:** `$` ________.____ USD
* **Budget Notification Email:** __________________________________________________
* **Cleanup Schedule:** `[ ]` Retain for portfolio permanent showcase • `[ ]` Delete immediately after testing

---

## 🏁 Phase 6: Timeline & 7-Day Milestones

* **Day 1: Architectural Mapping & Security Setup**
  * `[ ]` Write down VPC layouts.
  * `[ ]` Configure AWS Budgets and CloudWatch Billing Alarms.
* **Day 2: Base Network & Compute Provisioning**
  * `[ ]` Deploy base VPC/Subnets or Serverless endpoint templates.
  * `[ ]` Test base compute connectivity.
* **Day 3: Application Integration & Code Development**
  * `[ ]` Code backend functions (Lambda/Boto3).
  * `[ ]` Deploy API integrations and test local connections.
* **Day 4: Security Configurations & Policy Testing**
  * `[ ]` Apply Security Groups and disable default public access.
  * `[ ]` Verify IAM role policies and test restriction scopes.
* **Day 5: Frontend Build & CDN Deployment**
  * `[ ]` Build client page and host on S3.
  * `[ ]` Deploy CloudFront CDN distribution with SSL bounds.
* **Day 6: Documentation & GitHub Showcase**
  * `[ ]` Draw clean SVG architecture diagrams.
  * `[ ]` Populate the Project README using the production template.
* **Day 7: Launch & Social Media Sharing**
  * `[ ]` Review logs and run clean delete tests.
  * `[ ]` Publish your LinkedIn technical case study!
