---
title: "3. Blogs Posted"
weight: 3
---

Welcome to the **Blogs Posted** section! During my learning and internship journey at AWS, I regularly read deep-dive articles on the AWS Blog. Below is a summary of the 3 most outstanding articles that I have carefully studied and drawn many practical lessons from. Click on the titles to view my full detailed reflections:

### 1. [Building Highly Available Oracle Databases with Amazon FSx for NetApp ONTAP](3.1-blog1/)
This blog provides a practical perspective on how to combine multiple services (Amazon FSx, EC2 Auto Scaling, AWS Backup, Lambda, and Systems Manager) to create a self-healing architecture. My biggest takeaway is not just how to deploy a database, but the mindset of designing a highly available system that ensures the minimum possible Recovery Time Objective (RTO) and Recovery Point Objective (RPO).

### 2. [Query Amazon S3 access logs instantly: Goodbye to log data "cleanup" nightmares!](3.2-blog2/)
If you've ever struggled to build complex ETL pipelines just to read raw logs from S3, this blog offers the perfect solution. By sending S3 Access Logs directly into CloudWatch Logs and S3 Tables, the system automatically structures the data. This allows us to perform instant queries at lightning speed, saving operational time and optimizing the security auditing workflow.

### 3. [Claude Apps Gateway for AWS - The solution for Enterprise AI Management](3.3-blog3/)
As AI booms, the question is no longer "How powerful is the AI?" but "How do we manage the AI?". This blog introduces the Claude Apps Gateway - a middleware layer that helps enterprises strictly control access, track user activity, and manage costs when utilizing AI. This provides an extremely practical perspective for engineers looking to deploy AI securely in real-world enterprise environments.
