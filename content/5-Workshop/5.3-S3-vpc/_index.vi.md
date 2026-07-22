---
title : "Triển khai frontend với Amazon S3"
date : 2026-07-09
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Tổng quan

Frontend của TaskManager là static web application. Sau khi build, các file HTML, JavaScript, CSS và SVG được upload lên Amazon S3 bucket `taskmanager-frontend-dev-*`.

Trong kiến trúc production, S3 bucket nên được đặt private và phân phối qua CloudFront. Trong phạm vi workshop này, chúng ta tập trung xác minh rằng frontend artifacts đã được upload thành công vào S3.

![S3 upload status](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/s3-upload.png)

#### Nội dung

- [Upload frontend assets lên S3](5.3.1-create-gwe/)
- [Kiểm tra kết quả upload frontend](5.3.2-test-gwe/)
