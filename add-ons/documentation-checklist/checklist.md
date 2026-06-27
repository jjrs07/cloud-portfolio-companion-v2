# Cloud Portfolio Documentation Checklist

Before you publish your cloud project repository or share your build on LinkedIn, use this checklist to perform a self-audit. Recruiters and technical hiring managers scan portfolios in under 60 seconds—this checklist ensures they see professional, production-grade cloud standards.

---

## 🎨 1. Visual & Architectural Diagram Audit

Your architecture diagram is the first thing a recruiter sees. Make sure it communicates design thinking clearly:

* `[ ]` **Grid Alignment:** All nodes, boxes, and blocks are aligned symmetrically. The diagram does not look chaotic or hand-drawn.
* `[ ]` **Directional Flows:** Every connection arrow has a clear arrowhead indicating the direction of traffic or data flow (e.g., Client &rarr; API Gateway &rarr; Lambda).
* `[ ]` **Clear Labels:** Arrow connections are labeled with protocols (e.g., HTTPS, Port 3306, gRPC) rather than generic text.
* `[ ]` **Multi-line Formatting:** Text labels are formatted into short, multiline blocks to avoid overlapping with connection lines.
* `[ ]` **Color Coding:** The diagram uses high-contrast, professional cloud provider colors (e.g., AWS Navy/Orange/Teal) rather than bright primary red or blue.
* `[ ]` **Subnet Boundaries:** VPC boundaries, public/private subnets, and security zones are demarcated using bounding boxes.
* `[ ]` **No Hand-Drawn / Drafts:** The diagram is generated using professional vector drawing tools (e.g., draw.io, Lucidchart) and saved as a high-quality SVG or PNG.

---

## 🔒 2. Security Architecture Audit

Hiring managers will immediately check if your project exposes security holes:

* `[ ]` **Zero Port 22 Exposures:** Security groups do NOT open Port 22 (SSH) to `0.0.0.0/0`. EC2 instance shell access is configured via AWS Systems Manager (SSM) Session Manager.
* `[ ]` **Isolated Databases:** Databases are placed in private or isolated subnets with no Route Table routing to the Internet Gateway.
* `[ ]` **Restricted Database Inbound traffic:** The database security group accepts connection requests strictly on the database port (e.g., 3306 for MySQL, 5432 for Postgres) from the web server security group ID—never from `0.0.0.0/0`.
* `[ ]` **Zero Hardcoded Secrets:** No API keys, passwords, access keys, or credentials exist anywhere in the source code. Database credentials are loaded from environment variables or AWS Secrets Manager.
* `[ ]` **Least-Privilege Roles:** IAM policies explicitly define resource scopes (ARN strings) instead of using wildcard targets (`Resource: "*"`).
* `[ ]` **HTTPS Encryption:** Public-facing web traffic is encrypted using HTTPS with SSL certificates (ACM) and edge caching (CloudFront).

---

## 💻 3. Infrastructure as Code (IaC) & Repository Audit

Show recruiters you build repeatable infrastructure:

* `[ ]` **Declarative Provisioning:** The repository contains Infrastructure as Code templates (e.g., AWS CloudFormation `template.yaml`, Terraform `.tf` files, or AWS CDK scripts) instead of manual console instructions.
* `[ ]` **IaC Templates Validated:** Code compiles and passes validation checks (`sam validate` or `terraform validate`) without warnings.
* `[ ]` **Clean Directory Structure:** Files are sorted into intuitive subdirectories:
  ```
  ├── src/                # Lambda backend source code
  ├── web/                # Frontend client files (HTML, CSS, JS)
  ├── templates/          # CloudFormation / SAM / Terraform templates
  └── README.md           # Main documentation
  ```
* `[ ]` **Exclusion Configurations:** A `.gitignore` file is active in the repository root, explicitly excluding `.env`, `node_modules/`, `dist/`, `.aws-sam/`, and temporary OS files (e.g., `.DS_Store`).
* `[ ]` **Clean Commit History:** Commit messages use clear, professional language (e.g., `feat: integrate bedrock lambda handler`, `fix: update api gateway cors headers`) rather than generic drafts (e.g., `update`, `test`, `temp`).

---

## 💸 4. FinOps & Operational Audit

Demonstrate that you treat cloud resources as business investments:

* `[ ]` **Billing Alerts Active:** CloudWatch billing alarms or AWS Budgets are active at a low threshold (e.g., $5.00) to notify you of unexpected usage.
* `[ ]` **Cleanup Script Provided:** Clear teardown instructions or teardown CLI commands (e.g., `sam delete` or `terraform destroy`) are documented at the bottom of the README.
* `[ ]` **Cost Estimates Disclosed:** The estimated cost of running and testing the project is documented in a small table.

---

## 🗣️ 5. Technical Interview Prep Audit

Ensure you can explain your decisions:

* `[ ]` **STAR Method Prepared:** You have written out the Situation, Task, Action, and Result for this project.
* `[ ]` **Troubleshooting Case Study logged:** You can explain at least two bugs or errors you encountered during the deployment and how you fixed them.
* `[ ]` **Design Choices Justified:** You can confidently answer why you chose specific services (e.g., "I used DynamoDB instead of RDS because the application requires low-latency lookups and our traffic pattern fits a serverless, document-based data store").
