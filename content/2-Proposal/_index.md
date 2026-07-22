---
title: "2. Đề xuất (Proposal)"
weight: 2
---

# Hệ thống Quản lý Công việc (Task Management System)
## Kiến trúc AWS Serverless cho Cộng tác Công việc An toàn

### 1. Tổng quan dự án

Hệ thống Quản lý Công việc được thiết kế như một ứng dụng web bảo mật, có khả năng mở rộng và vận hành tối giản, phục vụ việc tạo, phân công, theo dõi và cập nhật các công việc theo thời gian thực. Hệ thống sử dụng kiến trúc serverless của AWS để nhóm dự án có thể tập trung vào phát triển tính năng thay vì lo lắng về việc cấu hình máy chủ, cập nhật bản vá hay lập kế hoạch dung lượng.

Frontend được phân phối qua Amazon CloudFront từ một bucket Amazon S3 riêng tư, với Amazon Route 53 xử lý DNS, AWS Certificate Manager cung cấp TLS và AWS WAF bảo vệ lớp biên công khai. Người dùng xác thực qua Amazon Cognito và gửi các truy vấn, mutation và subscription GraphQL tới AWS AppSync với xác thực JWT. Logic nghiệp vụ chạy trên AWS Lambda, dữ liệu công việc được lưu trữ trong Amazon DynamoDB với tính năng khôi phục theo thời điểm (PITR), và các log, số liệu, cảnh báo vận hành được tập trung tại Amazon CloudWatch. Luồng triển khai được tự động hóa từ GitHub qua AWS CodePipeline, AWS CodeBuild và AWS CloudFormation.

### 2. Vấn đề cần giải quyết

**Vấn đề hiện tại?**

Nhiều nhóm nhỏ vẫn quản lý công việc qua tin nhắn chat, bảng tính hoặc ghi chú rời rạc. Điều này khiến việc nắm bắt chủ sở hữu công việc, trạng thái hiện tại, độ ưu tiên và lịch sử trở nên khó khăn. Khi nhóm phát triển, các cập nhật thủ công tạo ra thông tin trùng lặp, bỏ lỡ deadline và thiếu tầm nhìn tổng quan cho việc theo dõi dự án. Cách triển khai ứng dụng web truyền thống cũng có thể tạo thêm công việc vận hành không cần thiết cho sinh viên hay dự án thực tập: bảo trì máy chủ, các bước deploy thủ công, lập kế hoạch sao lưu cơ sở dữ liệu, cài đặt SSL và cấu hình giám sát.

**Giải pháp đề xuất**

Hệ thống đề xuất cung cấp một ứng dụng quản lý công việc tập trung, được hỗ trợ bởi các dịch vụ AWS được quản lý. Người dùng đăng nhập qua Cognito, sau đó tương tác với công việc thông qua AppSync GraphQL API. Các truy vấn và mutation hỗ trợ liệt kê, tạo mới, cập nhật, phân công và hoàn thành công việc. GraphQL subscription hỗ trợ cập nhật gần thời gian thực để các thành viên có thể thấy thay đổi mà không cần tải lại trang. Lambda xử lý validation và logic nghiệp vụ, trong khi DynamoDB lưu trữ dữ liệu với khả năng đọc/ghi có thể mở rộng và tính năng khôi phục theo thời điểm. Tài nguyên tĩnh của website được giữ riêng tư trong S3 và chỉ phục vụ qua CloudFront. CI/CD tự động hóa giảm công sức deploy thủ công và giữ các thay đổi hạ tầng nhất quán qua CloudFormation.

**Lợi ích và Giá trị đầu tư**

Hệ thống cải thiện tầm nhìn của nhóm bằng cách tập trung dữ liệu công việc, trạng thái, chủ sở hữu và cập nhật. Dịch vụ serverless giữ mô hình vận hành nhẹ nhàng và tiết kiệm chi phí vì hầu hết các thành phần đều tự động mở rộng theo mức sử dụng. Deploy tự động rút ngắn thời gian phát hành, giảm lỗi cấu hình và giúp dự án dễ duy trì hơn sau thời gian thực tập.

### 3. Kiến trúc giải pháp

Kiến trúc theo mô hình serverless với các lớp tách biệt: phân phối frontend, xác thực, API, backend, dữ liệu, quan sát và CI/CD. Yêu cầu từ website công khai được Route 53 phân giải và CloudFront phân phối từ bucket S3 riêng tư. Yêu cầu đăng nhập đi qua Cognito. Các yêu cầu đã xác thực sử dụng AppSync GraphQL với JWT token, sau đó AppSync gọi Lambda để xử lý logic nghiệp vụ và DynamoDB để lưu trữ dữ liệu công việc. CloudWatch thu thập log, số liệu và cảnh báo trên toàn ứng dụng.

**Danh sách dịch vụ AWS sử dụng:**

| Dịch vụ AWS | Mục đích sử dụng |
| :--- | :--- |
| **Amazon Route 53** | Quản lý bản ghi DNS cho tên miền ứng dụng. |
| **Amazon CloudFront** | Phân phối frontend toàn cầu và kết nối người dùng với S3 origin riêng tư. |
| **Amazon S3** | Lưu trữ tài nguyên tĩnh của website trong bucket riêng tư. |
| **AWS WAF** | Bảo vệ phân phối CloudFront khỏi các cuộc tấn công web phổ biến. |
| **AWS Certificate Manager** | Cung cấp và quản lý chứng chỉ TLS cho HTTPS. |
| **Amazon Cognito** | Xử lý đăng ký, đăng nhập, cấp JWT token và xác thực người dùng. |
| **AWS AppSync** | Cung cấp GraphQL API cho các query, mutation và subscription. |
| **AWS Lambda** | Chạy logic xử lý công việc backend mà không cần quản lý máy chủ. |
| **Amazon DynamoDB** | Lưu trữ dữ liệu công việc, người dùng, trạng thái và phân công với PITR. |
| **Amazon CloudWatch** | Thu thập log, số liệu và cảnh báo để giám sát và xử lý sự cố. |
| **AWS CodePipeline** | Tự động hóa quy trình deploy từ các thay đổi mã nguồn. |
| **AWS CodeBuild** | Build và xác thực các artifact ứng dụng. |
| **AWS CloudFormation** | Cấu hình và cập nhật hạ tầng dưới dạng mã (IaC). |
| **GitHub** | Lưu trữ mã nguồn và kích hoạt pipeline CI/CD. |

**Thiết kế thành phần:**

- **Phân phối Frontend**: Các file frontend tĩnh được upload lên bucket S3 riêng tư và phân phối qua CloudFront. Route 53 ánh xạ tên miền tùy chỉnh đến CloudFront distribution, và ACM kích hoạt HTTPS.
- **Lớp bảo mật biên**: AWS WAF được gắn vào CloudFront để lọc lưu lượng độc hại hoặc bất thường trước khi yêu cầu đến ứng dụng.
- **Xác thực**: Cognito quản lý người dùng và trả về JWT token sau khi đăng nhập. Frontend gắn token vào các yêu cầu GraphQL.
- **Lớp API**: AppSync xác thực JWT token và cung cấp các thao tác GraphQL cho việc tạo, cập nhật, phân công, lọc và subscription thời gian thực.
- **Logic Backend**: Lambda thực thi các quy tắc nghiệp vụ như xác thực quyền sở hữu công việc, cập nhật trạng thái và chuẩn bị dữ liệu phản hồi.
- **Lớp dữ liệu**: DynamoDB lưu trữ dữ liệu công việc và kích hoạt PITR để bảo vệ khỏi thao tác ghi/xóa nhầm.
- **Vận hành**: CloudWatch nhận log và số liệu từ AppSync, Lambda, DynamoDB và pipeline deploy. Cảnh báo có thể thông báo cho nhóm khi xuất hiện lỗi hoặc sử dụng bất thường.
- **Triển khai**: Developer push code lên GitHub. CodePipeline và CodeBuild đóng gói ứng dụng, sau đó CloudFormation cập nhật tài nguyên AWS và deploy các thay đổi frontend/backend.

### 4. Triển khai kỹ thuật

**Các giai đoạn triển khai:**

- **Phân tích yêu cầu và thiết kế kiến trúc**: Xác định vai trò người dùng, vòng đời công việc, các thao tác GraphQL, ranh giới bảo mật và trách nhiệm của từng dịch vụ AWS.
- **Thiết lập hạ tầng dưới dạng mã**: Tạo CloudFormation template cho S3, CloudFront, WAF, ACM, Cognito, AppSync, Lambda, DynamoDB, CloudWatch và tài nguyên CI/CD.
- **Phát triển Frontend**: Xây dựng giao diện công việc, màn hình xác thực, danh sách công việc, chi tiết công việc, bộ lọc và hành vi cập nhật thời gian thực.
- **Phát triển Backend và API**: Định nghĩa GraphQL schema, kết nối resolver với Lambda, triển khai logic validation và tích hợp các mẫu truy cập DynamoDB.
- **Giám sát và tăng cường bảo mật**: Cấu hình CloudWatch log, số liệu, cảnh báo, quyền IAM tối thiểu, DynamoDB PITR và WAF rule.
- **Kiểm thử và triển khai**: Xác thực đăng nhập, luồng CRUD, cập nhật subscription, deploy CI/CD, hành vi rollback và các kịch bản lỗi cơ bản.

**Yêu cầu kỹ thuật:**

- Frontend web tĩnh có thể build và deploy lên S3.
- Cognito user pool cho xác thực và phân quyền dựa trên JWT.
- AppSync GraphQL schema bao gồm query, mutation và subscription cho công việc.
- Lambda runtime cho logic backend và tích hợp DynamoDB.
- Thiết kế bảng DynamoDB cho công việc, người dùng, dự án, trạng thái, độ ưu tiên và mẫu truy cập phân công.
- CloudFormation template cho việc cấu hình hạ tầng lặp lại được.
- Pipeline CI/CD kết nối GitHub cho build và deploy tự động.
- CloudWatch dashboard hoặc cảnh báo để theo dõi lỗi và tầm nhìn vận hành.

### 5. Timeline và Tiến độ

**Lịch dự án:**

- **Trước khi triển khai**: Nghiên cứu dịch vụ AWS serverless, so sánh các phương án kiến trúc và hoàn thiện phạm vi dự án.
- **Tháng 1**: Thiết kế kiến trúc giải pháp, định nghĩa mô hình dữ liệu, tạo CloudFormation template ban đầu và cấu hình đường dẫn host frontend cơ bản.
- **Tháng 2**: Triển khai xác thực Cognito, AppSync GraphQL API, Lambda function và lưu trữ DynamoDB.
- **Tháng 3**: Hoàn thiện CI/CD, giám sát, cấu hình WAF, kiểm thử tích hợp, tài liệu hóa và thuyết trình dự án cuối kỳ.
- **Sau khi ra mắt**: Cải thiện UI/UX, thêm nhóm/dự án, tăng cường audit logging và tối ưu chi phí dựa trên mức sử dụng thực tế.

### 6. Ước tính Ngân sách

Dự án được thiết kế cho quy mô thực tập nhỏ, vì vậy hầu hết mức sử dụng nên nằm trong giới hạn chi phí thấp hoặc free tier.

| Dịch vụ AWS | Chi phí ước tính / Tháng |
| :--- | :--- |
| **Route 53** | ~$0.50 cho một hosted zone công khai, cộng phí truy vấn DNS nếu có. |
| **CloudFront & S3** | Rất thấp cho tài nguyên tĩnh và lưu lượng nhỏ; CloudFront có mức free-tier hàng tháng. |
| **Cognito** | $0 cho lượng người dùng nội bộ nhỏ trong giới hạn free tier. |
| **AppSync** | $0 trong giới hạn free tier; vượt free tier tính theo từng query/mutation/thao tác thời gian thực. |
| **Lambda** | $0 cho lượng gọi thấp trong giới hạn free tier của Lambda. |
| **DynamoDB** | $0 cho bảng nhỏ trong giới hạn free tier về lưu trữ/dung lượng đã cấp phát. |
| **CloudWatch** | $0 nếu log, số liệu và cảnh báo nằm trong giới hạn free tier. |
| **WAF** | ~$10–15/tháng cho một Web ACL với bộ rule nhỏ và lưu lượng thấp. |
| **CodePipeline, CodeBuild, CloudFormation** | Thấp cho pipeline CI/CD nhỏ với số lần build hạn chế. |
| **Tổng ước tính** | **~$1–3/tháng** (không có WAF) hoặc **~$12–18/tháng** (có WAF). |

### 7. Đánh giá Rủi ro

**Ma trận rủi ro:**

| Rủi ro | Mức độ ảnh hưởng | Xác suất |
| :--- | :--- | :--- |
| Cấu hình sai xác thực hoặc phân quyền | Cao | Trung bình |
| Lỗi GraphQL resolver hoặc Lambda | Trung bình | Trung bình |
| Sai mẫu truy cập DynamoDB | Trung bình | Trung bình |
| Xóa nhầm hoặc cập nhật sai dữ liệu | Cao | Thấp |
| Chi phí ngoài dự kiến từ WAF, log hoặc tăng đột biến lưu lượng | Trung bình | Thấp |
| Lỗi deploy CI/CD | Trung bình | Trung bình |

**Chiến lược giảm thiểu:**

- Áp dụng quyền IAM tối thiểu và xác thực JWT Cognito trong AppSync.
- Sử dụng structured logging và CloudWatch alarm cho lỗi Lambda và AppSync.
- Thiết kế DynamoDB key dựa trên mẫu truy cập công việc thực tế trước khi triển khai.
- Kích hoạt PITR cho DynamoDB và tránh thao tác ghi thủ công trực tiếp trên production.
- Cấu hình AWS Budgets và xem lại cài đặt thời gian lưu trữ log CloudWatch.
- Giữ các thay đổi hạ tầng trong CloudFormation và kiểm thử pipeline trước khi deploy cuối cùng.

**Kế hoạch dự phòng:**

- Rollback các deploy thất bại qua CloudFormation và CodePipeline.
- Khôi phục bản ghi DynamoDB qua PITR nếu dữ liệu bị sửa đổi nhầm.
- Tạm thời tắt các tính năng không quan trọng như subscription hoặc WAF rule nếu chúng gây vấn đề về chi phí hoặc khả năng hoạt động trong khi kiểm thử.
- Chỉ dùng deploy thủ công như giải pháp tạm thời trong khi sửa pipeline CI/CD.

### 8. Kết quả kỳ vọng

**Cải tiến kỹ thuật:**

Hệ thống cuối cùng cung cấp một ứng dụng quản lý công việc serverless an toàn với xác thực được quản lý, cập nhật GraphQL thời gian thực, deploy tự động, giám sát tập trung và lưu trữ dữ liệu công việc đáng tin cậy.

**Giá trị lâu dài:**

Kiến trúc có thể được tái sử dụng làm nền tảng cho các công cụ cộng tác nhóm tương lai, hệ thống theo dõi vấn đề hoặc ứng dụng quy trình làm việc nội bộ. Dự án cũng thể hiện kỹ năng AWS thực tế trên nhiều lĩnh vực: host frontend, quản lý danh tính, backend serverless, mô hình hóa dữ liệu NoSQL, giám sát, bảo mật và CI/CD tự động hóa.
