---
title: "Workshop"
date: 2026-07-09
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Triển khai Hệ thống Quản lý Công việc trên AWS Serverless

#### Tổng quan

Workshop này hướng dẫn từng bước triển khai và xác thực **Hệ thống Quản lý Công việc (Task Management System)** sử dụng kiến trúc serverless của AWS. Hệ thống hỗ trợ xác thực người dùng, quản lý bảng công việc, theo dõi nhiệm vụ, cập nhật trạng thái và ghi nhật ký vận hành thông qua các dịch vụ AWS được quản lý.

Kiến trúc sử dụng:
- **Amazon S3** để host tĩnh frontend
- **Amazon Cognito** để xác thực người dùng
- **AWS AppSync** cho GraphQL API
- **AWS Lambda** để xử lý logic nghiệp vụ backend
- **Amazon DynamoDB** để lưu trữ dữ liệu
- **IAM** để kiểm soát quyền truy cập
- **Amazon CloudWatch** để thu thập log và quan sát hệ thống

#### Nội dung

1. [Tổng quan Workshop](5.1-workshop-overview/)
2. [Chuẩn bị môi trường và quyền IAM](5.2-prerequiste/)
3. [Triển khai frontend với Amazon S3](5.3-s3-vpc/)
4. [Cấu hình xác thực, API và backend](5.4-s3-onprem/)
5. [Xác thực DynamoDB, index và PITR](5.5-policy/)
6. [Dọn dẹp tài nguyên](5.6-cleanup/)
