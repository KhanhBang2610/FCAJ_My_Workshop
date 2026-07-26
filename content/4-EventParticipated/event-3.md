---
title: "4.3. Báo cáo Tổng kết: Hackathon Agentic AI Build Week (AABW)"
weight: 3
---

## Báo cáo Tổng kết: Hackathon Agentic AI Build Week (AABW) - Các Dự Án Nổi Bật

Sự kiện Hackathon Agentic AI Build Week (AABW) đã khép lại với những dự án đầy sáng tạo, tập trung vào việc giải quyết các bài toán thực tế của doanh nghiệp bằng sức mạnh của AI Agentic và AWS. Dưới đây là phần tổng hợp về 4 dự án xuất sắc tham dự sự kiện.

---

### 1. Đội 3KA: Dự án S.H.E.P.H.E.R.D (Quản lý dòng người và dự báo rủi ro)

**Nội dung cốt lõi:**
Dự án S.H.E.P.H.E.R.D tập trung vào việc phân tích luồng người (Human-flow), đánh giá, dự đoán, phát hiện mối nguy hiểm và điều phối phản hồi theo thời gian thực. Bằng việc kết hợp YOLO, ByteTrack và Amazon SageMaker cùng Amazon Bedrock AgentCore, hệ thống biến video camera thông thường thành các số liệu vận hành rõ ràng: đo lường mật độ đám đông, ước tính tình trạng xếp hàng và dự đoán sớm sự tắc nghẽn. 

**Bài học rút ra:**
- Xây dựng một sản phẩm AI cần nhiều hơn một mô hình tốt; nó đòi hỏi kiến trúc tổng thể ổn định từ video streaming, độ trễ suy luận (latency), cho đến một bảng điều khiển (dashboard) trực quan cho người vận hành.
- "Bắt đầu nhỏ, hoàn thiện tốt" (Small, finished work beats big, broken ideas) - Tập trung vào một tính năng cốt lõi và làm cho nó hoạt động trơn tru trong giới hạn 24 giờ của Hackathon.

---

### 2. Đội One Team: KFC Bot Agent (Trợ lý AI gọi món đa kênh)

**Nội dung cốt lõi:**
Dự án giải quyết vấn đề "rơi rớt đơn hàng" (lost orders) khi khách hàng phải chuyển đổi ứng dụng. KFC Bot Agent cho phép người dùng đặt hàng trực tiếp ngay trên Zalo hoặc Messenger thông qua hội thoại tự nhiên. 
Thay vì một chatbot thông thường, đây là một Agent thực thụ: có khả năng hiểu ý định (intent), lên kế hoạch (plan), tra cứu dữ liệu menu, áp dụng mã giảm giá và xác nhận đơn hàng với giỏ hàng thực tế. Kiến trúc "Thiết kế một lần - Triển khai mọi nơi" (Design Once | Deploy Everywhere) giúp việc thêm kênh mới dễ dàng thông qua các adapters.

**Bài học rút ra:**
- Xử lý ngôn ngữ tự nhiên trong đặt hàng rất phức tạp (từ ngữ lóng, thay đổi ý định giữa chừng). AI Agent không chỉ cần hiểu ngôn ngữ mà phải kết nối chặt chẽ với các "tool" và hệ thống nghiệp vụ (Business Rules).

---

### 3. Đội Plan V: Solution Architect Professional Native App (AI tự động hóa thiết kế kiến trúc)

**Nội dung cốt lõi:**
Ứng dụng hướng đến việc tự động hóa công việc của các Solution Architect. Khách hàng chỉ cần tải lên yêu cầu hoặc trò chuyện bằng ngôn ngữ tự nhiên, hệ thống sẽ tự động: phân tích yêu cầu, phác thảo các phương án kiến trúc cấp cao (high-level architecture), tạo biểu đồ Drawio tự động bằng các biểu tượng chuẩn AWS và đưa ra dự toán chi phí (cost estimation) trên AWS.

**Bài học rút ra:**
- AI có khả năng giải phóng các chuyên gia khỏi các tác vụ lặp đi lặp lại như đọc tài liệu yêu cầu (BRD/PRD) hay vẽ biểu đồ thủ công. Điều này giúp họ tập trung vào tư duy chiến lược và phản biện lại "bản nháp" đầu tiên mà AI tạo ra.

---

### 4. Đội Signal Scout: Nền tảng phát hiện thay đổi chiến lược doanh nghiệp sớm

**Nội dung cốt lõi:**
Dự án được thiết kế để phân tích các số liệu tài chính, hoạt động và tín hiệu từ doanh nghiệp nhằm phát hiện sớm các chiến lược thay đổi hoặc rủi ro (như tái cấu trúc). Hệ thống kết nối các "tín hiệu phân tán" thành một câu chuyện rõ ràng, cung cấp báo cáo và cảnh báo rủi ro thông qua một Dashboard trực quan. Mọi kết luận của AI đều được minh chứng bằng các dữ liệu thực tế đã thu thập.

**Bài học rút ra:**
- Sự minh bạch là chìa khóa. Trong các hệ thống hỗ trợ ra quyết định (Decision Support), mọi suy luận của AI cần phải được truy xuất nguồn gốc và kiểm chứng bằng bằng chứng dữ liệu rõ ràng. Việc giữ cho con người đưa ra quyết định cuối cùng (Human-controlled decision) vẫn là yếu tố thiết yếu.

---

## Tổng Kết 

Hackathon AABW không chỉ là cuộc thi lập trình 24 giờ, mà là minh chứng rõ rệt cho sự chuyển dịch sang kỷ nguyên **Agentic AI**. Các đội thi đã cho thấy AI không chỉ dừng lại ở việc tạo văn bản hay hình ảnh, mà đã có khả năng thực thi các luồng công việc phức tạp, gọi API, và đưa ra các quyết định có độ tin cậy cao dựa trên dữ liệu thực tế.
