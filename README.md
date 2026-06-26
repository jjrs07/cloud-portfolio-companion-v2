# Build Your First Cloud Portfolio v2.0 — Companion Code Repository

Welcome to the official companion code repository for the e-book **"Build Your First Cloud Portfolio" (Version 2.0)** by James Santos.

> [!IMPORTANT]
> **Looking for the e-book?**  
> This code repository is a companion to the hands-on workbook **"Build Your First Cloud Portfolio (Version 2.0)"**. The book features step-by-step instructions, system architecture diagrams, and "What If It Breaks? (Interview Gold)" troubleshooting blueprints designed to help you construct a job-winning portfolio and ace technical interviews.
> 
> 👉 **[Get your copy of the e-book here!](https://portfolio.mastercloud.guru)**

This repository contains all the configuration files, automation scripts, and infrastructure-as-code templates detailed throughout the book's hands-on labs. Instead of copying and pasting code directly from your PDF reader, you can use these clean, production-ready files to deploy your portfolio components instantly.

---

## 📂 Repository Structure

The code is organized logically by chapters:

```text
cloud-portfolio-companion-v2/
├── chapter-1/              # CloudWatch Lab
│   └── monitoring-stack.yaml  # Automated VPC + EC2 + SNS Alarm CloudFormation template
├── chapter-2/              # IAM & Scripting Lab
│   ├── backup.sh           # Linux backup automation script (using syslogs)
│   └── policy.json         # Least-privilege S3 bucket access policy document
├── chapter-3/              # S3 & CloudFront CDN Lab
│   └── index.html          # Beautiful, mobile-responsive HTML/CSS portfolio home page
└── chapter-5/              # Serverless AI Resume Analyzer (Core Project)
    ├── template.yaml       # AWS SAM infrastructure blueprint (API Gateway, S3, Lambda)
    ├── app/
    │   └── index.html      # Frontend web interface (HTML/JS client)
    └── lambda/
        └── lambda_function.py # Python backend script invoking Amazon Bedrock (Llama 3)
```

---

## 🚀 How to Use This Repository

To use these files on your local computer, choose one of the following methods:

### Method A: Clone the Repository (Recommended)
Open your terminal (macOS/Linux) or Command Prompt/PowerShell (Windows) and run:
```bash
git clone https://github.com/YOUR_USERNAME/cloud-portfolio-companion-v2.git
```
Navigate to the directory:
```bash
cd cloud-portfolio-companion-v2
```

### Method B: Download as ZIP
1. Click the green **Code** button at the top right of this page.
2. Select **Download ZIP**.
3. Extract the ZIP file into a folder of your choice on your local machine.

---

## 🛠️ Chapter Highlights

### Chapter 1: CloudWatch Monitoring Stack
*   **Technology:** AWS CloudFormation (YAML)
*   **Purpose:** Deploys a VPC network, an EC2 web server, custom CloudWatch high-CPU alarms, SNS notification channels, and an operations dashboard to teach you infrastructure automation and telemetry.

### Chapter 2: Secure Backup Automation
*   **Technology:** Bash Scripting, IAM Roles
*   **Purpose:** Configures a script that packages web directories and pushes them to S3. Demonstrates IAM instance profiles to avoid hardcoding access keys in scripts.

### Chapter 3: Private S3 + CloudFront CDN Static Hosting
*   **Technology:** HTML/CSS, Amazon S3, CloudFront OAC, ACM, Route 53
*   **Purpose:** Deploys your portfolio website behind a secure CDN, ensuring that the backend S3 bucket remains private and only accessible via CloudFront over HTTPS.

### Chapter 5: Serverless AI Resume Analyzer
*   **Technology:** AWS SAM, Lambda (Python), API Gateway, Amazon Bedrock (Llama 3 8B Instruct)
*   **Purpose:** The star project of the book. Analyzes resume text against a target job description and returns an LLM recruiter assessment. Introduces serverless architectures and GenAI integrations.

---

## ⚖️ License & Contributions

This code is licensed under the **MIT License**—feel free to use it, customize it, and deploy it as part of your personal portfolio!

If you spot a bug or want to suggest an improvement, feel free to open an issue or open a Pull Request (PR) to help out your fellow cloud builders.

*Happy Building!*  
**James Santos**  
*AWS Authorized Instructor | Cloud Advocate*
