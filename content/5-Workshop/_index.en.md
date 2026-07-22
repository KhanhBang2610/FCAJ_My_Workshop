---
title: "Workshop"
date: 2026-07-09
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Deploying the Task Management System on AWS Serverless

#### Overview

This workshop walks through the deployment and validation of a **Task Management System** using a serverless AWS architecture. The system supports user authentication, board management, task tracking, status updates, and operational logging through managed AWS services.

The architecture uses:
- **Amazon S3** for static frontend hosting
- **Amazon Cognito** for user authentication
- **AWS AppSync** for the GraphQL API
- **AWS Lambda** for backend business logic
- **Amazon DynamoDB** for data storage
- **IAM** for access control
- **Amazon CloudWatch** for logs and observability

#### Content

1. [Workshop overview](5.1-workshop-overview/)
2. [Environment preparation and IAM permissions](5.2-prerequiste/)
3. [Deploy the frontend with Amazon S3](5.3-s3-vpc/)
4. [Configure authentication, API, and backend](5.4-s3-onprem/)
5. [Validate DynamoDB, indexes, and PITR](5.5-policy/)
6. [Clean up resources](5.6-cleanup/)
