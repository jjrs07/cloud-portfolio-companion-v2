# Cloud Architecture Template & Guidelines

This directory contains visual guidelines and a pre-configured **Draw.io diagram template** to help you design clean, recruiter-ready cloud architecture diagrams without starting from a blank page.

---

## 🚀 How to Use the Draw.io Template

1. Go to the free online diagram editor: [draw.io (app.diagrams.net)](https://app.diagrams.net/).
2. Select **Open Existing Diagram** (or go to *File > Import From > Device...*).
3. Select the template file located in this directory: [aws-drawio-template.xml](file:///C:/Users/jj_rs/projects/cloud-portfolio-companion-v2/add-ons/architecture-template/aws-drawio-template.xml).
4. The template will load instantly with pre-aligned AWS nodes, subnet boundaries, and directional arrows configured on a grid.
5. Double-click the text fields to customize labels, drag shapes to add services, and export your final design as a clean **SVG** or **PNG** file!

---

## 🎨 Diagram Design Guidelines (How to Stand Out)

Hiring managers check diagrams to see if you can communicate technical choices clearly. Avoid cluttered layouts by applying these rules:

### 1. The Grid and Box Alignment
* Keep all icons and subnets snapped to the grid. Aligned diagrams convey order and professionalism.
* Subnets hosting similar workloads (e.g., Public Subnet A and Public Subnet B) must be identical in size, height, and spacing.

### 2. Subnet Boundaries (Zoning)
* Always draw subnet borders to represent network isolation:
  * **Public Subnets:** Light Blue border with a clear routing table description (routing to Internet Gateway).
  * **Private Subnets:** Light Orange border with NAT routing or SSM endpoints.
  * **Isolated Subnets:** Dotted/dashed Dark Grey border (completely private with zero internet connectivity).

### 3. Directional Flows & Labels
* Data flow should travel logically in one direction (usually **Left-to-Right** or **Top-to-Bottom**).
* Label your connection arrows with protocols and ports instead of vague text (e.g., write `HTTPS / Port 443` or `MySQL / Port 3306` instead of `sends traffic` or `calls DB`).
* Wrap connection labels into short, multiline blocks so they don't overlap with or cover the arrows.

### 4. Icon Continuity
* Use the official, modern AWS Architecture Icons (pre-loaded in the template). Do not mix AWS icons with general clipart, emoji, or competing cloud provider icons.

---

## 📐 Template Component Schema

The [aws-drawio-template.xml](file:///C:/Users/jj_rs/projects/cloud-portfolio-ebook-v2/add-ons/architecture-template/aws-drawio-template.xml) file is pre-configured with:
1. **User Client:** Browser/Mobile representing the client entry point.
2. **Global CDN Layer:** CloudFront CDN caching edge node.
3. **Network Boundary:** VPC wrapper containing public, private, and database subnets.
4. **Compute Resources:** EC2 and Lambda instances equipped with least-privilege role designations.
5. **Database Node:** Amazon RDS database instance locked in the isolated zone.
6. **Managed API Router:** API Gateway routing requests from S3.
7. **GenAI Layer:** Amazon Bedrock calling foundation model blocks.
