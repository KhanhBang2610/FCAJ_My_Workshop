---
title : "Dọn dẹp tài nguyên"
date : 2026-07-09
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Tổng kết workshop

Chúc mừng bạn đã hoàn thành workshop TaskManager. Trong workshop này, bạn đã kiểm tra:

- IAM dashboard và các khuyến nghị bảo mật cơ bản.
- S3 bucket chứa frontend build output.
- Cognito User Pool `taskmanager-users-dev`.
- AppSync GraphQL API `TaskManagerAPI-dev`.
- Lambda functions xử lý backend.
- DynamoDB tables, Global Secondary Index và PITR.
- CloudWatch log groups cho Lambda backend.

#### Dọn dẹp tài nguyên

Nếu không còn sử dụng môi trường TaskManager, hãy dọn tài nguyên để tránh phát sinh chi phí.

1. Xóa frontend objects trong S3 bucket `taskmanager-frontend-dev-*`.

   ![Xóa frontend objects trong S3 bucket](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-s3-objects.png)

2. Xóa AppSync API `TaskManagerAPI-dev`.

   ![Xóa AppSync API TaskManagerAPI-dev](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-appsync-api.png)

3. Xóa Lambda functions `userManager-dev`, `boardManager-dev`, `taskProcessor-dev`, `streamProcessor-dev`.

   ![Xóa các Lambda functions của TaskManager](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-lambda-functions.png)

4. Xóa DynamoDB tables `TaskManager-*` nếu không cần giữ dữ liệu.

   ![Xóa các DynamoDB tables của TaskManager](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-dynamodb-tables.png)

5. Xóa Cognito User Pool `taskmanager-users-dev`.

   ![Xóa Cognito User Pool taskmanager-users-dev](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-cognito-user-pool.png)

6. Xóa CloudWatch log groups `/aws/lambda/*Manager-dev`, `/aws/lambda/taskProcessor-dev` và `/aws/lambda/streamProcessor-dev` nếu không cần audit log.

   ![Xóa các CloudWatch log groups của TaskManager](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-cloudwatch-log-groups.png)

7. Xóa IAM roles/policies được tạo riêng cho project nếu không còn dùng.

   ![Xóa IAM roles và policies của TaskManager](/FCAJ_My_Workshop/images/5-Workshop/5.6-Cleanup/delete-iam-roles-policies.png)

{{% notice warning %}}
Trước khi xóa DynamoDB tables hoặc Cognito User Pool, hãy chắc chắn rằng dữ liệu không còn cần thiết. PITR chỉ giúp khôi phục trong khoảng thời gian được cấu hình khi bảng còn tồn tại hoặc khi quy trình restore được thực hiện đúng cách.
{{% /notice %}}

#### Kết luận

TaskManager là một ví dụ hoàn chỉnh về serverless application trên AWS: frontend tĩnh, authentication được quản lý, GraphQL API, compute bằng Lambda, database bằng DynamoDB và observability bằng CloudWatch.
