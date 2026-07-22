---
title: "4.2. Báo cáo thu hoạch: Event FCAJ Community Day (27/6/2026)"
weight: 2
---

## Báo cáo thu hoạch: Những Kiến Thức Bản Thân Học Được Qua Event FCAJ Community Day ngày 27/6/2026

Chào mọi người,

Hôm nay mình lại ngồi lại, gõ vài dòng recap về sự kiện công nghệ **FCAJ Community Day** diễn ra vào tháng 6/2026 vừa qua. Sự kiện lần này là một bức tranh toàn cảnh về cách doanh nghiệp ứng dụng AI vào thực tế, từ vận hành hạ tầng đến quản trị nhân sự.

Dưới đây là 5 bài học, 5 trải nghiệm thực tế từ các diễn giả đã mang lại cho mình nhiều góc nhìn mới về kỷ nguyên AI Agentic.

---

### 1. Deep Response Engine: Chuyển dịch từ 'Cảnh báo' sang 'Hành động'
*Diễn giả: Anh Steve Trần*

![Steve Tran](/FCAJ_My_Workshop/FCAJ%20June%2027%20assets/Steve%20Tran.jpg)

**Nội dung cốt lõi:**
Anh Steve đã chỉ ra 'bức tường phức tạp' (complexity wall) mà các hệ thống cloud hiện đại đang gặp phải. Thay vì cứ phụ thuộc vào các hệ thống cảnh báo (alert-driven) khiến đội ngũ ops luôn trong tình trạng 'cháy máy', giải pháp là chuyển sang hệ thống Action-driven. Với Deep Response Engine, AI không chỉ báo lỗi mà còn tự động điều tra (investigation) và đề xuất phương án xử lý, biến thời gian xử lý sự cố từ vài giờ xuống còn vài phút.

> **Trải nghiệm bản thân:**
> Mình nhận ra các startup thường mắc kẹt ở việc chỉ build 'ý tưởng' (BC ideas) mà thiếu đi các 'Champion khách hàng'. Bài học lớn nhất là phải gắn giải pháp vào bài toán thực tế của doanh nghiệp (như F88, FPT), nơi mà mỗi phút downtime đều là tiền bạc.

---

### 2. Voice Agents: Khi AI biết nói tiếng người
*Diễn giả: Anh Trung, Kiệt Trần và Nghị Danh Hoàng Hiếu*

![Trung Vu](/FCAJ_My_Workshop/FCAJ%20June%2027%20assets/Trung%20Vu.jpg)

**Nội dung cốt lõi:**
Từ IVR và Chatbot truyền thống, chúng chúng ta đã tiến lên kỷ nguyên AI Voice Agents. Anh Trung nhấn mạnh thách thức của ngôn ngữ Tiếng Việt là một 'low resource language'. Thay vì dùng mô hình speech-to-speech toàn phần (thường kém ổn định), giải pháp là kiến trúc 3 bước: `Speech-to-Text -> LLM (xử lý logic) -> Text-to-Speech (tạo giọng)`. Đặc biệt, khi làm cho ngân hàng, cần tuyệt đối tuân thủ Audit log, Versioning và Knowledge base để kiểm soát AI không nói 'linh tinh'.

---

### 3. AWS DevOps Agent: Trợ lý vận hành không bao giờ ngủ
*Diễn giả: Chị Bảo & Anh Nguyên*

![Bao and Nguyen](/FCAJ_My_Workshop/FCAJ%20June%2027%20assets/Ms%20Bao%20and%20mr%20Nguyen.jpg)

**Nội dung cốt lõi:**
Đây là phần mình thích nhất vì tính ứng dụng cao cho dân DevOps. Hệ thống sử dụng khái niệm Agent Space để học topology của hạ tầng. Khi có sự cố (ví dụ ECS task lỗi), agent sẽ tự truy vết nguyên nhân (root cause), đưa ra kế hoạch khắc phục (mitigation plan) và người vận hành chỉ cần duyệt (Human-in-the-loop).

> **Trải nghiệm bản thân:**
> Điều kiện tiên quyết là hệ thống phải có Observability tốt (log, metric, alarm rõ ràng). Nếu bạn không có data nền tảng, AI cũng chỉ là 'thầy bói xem voi' với việc generate thông tin mà không có context cụ thể. Dẫn chứng về việc giảm 77% thời gian MTTR tại một trường đại học là con số rất thuyết phục.

---

### 4. Amazon Quick Suite: Định nghĩa lại Productivity cho HR
*Diễn giả: Anh Trường & Chị Minh Anh*

![Truong Tran](/FCAJ_My_Workshop/FCAJ%20June%2027%20assets/Truong%20tran.jpg)

**Nội dung cốt lõi:**
Sự kết hợp giữa Amazon Quick và các quy trình HR. Không chỉ là công cụ chatbot, Quick giúp tự động hóa việc sàng lọc CV (OCR), đối chiếu với JD, và chấm điểm ứng viên dựa trên thang đo kỹ thuật/kỹ năng mềm. Nó biến HR từ 'kẻ làm việc hành chính' thành 'chiến lược gia nhân sự' bằng cách giải phóng họ khỏi các tác vụ lặp đi lặp lại.

---

### 5. Xây dựng kết nối MCP bảo mật
*Diễn giả: Bạn Toàn Nguyễn & Anh Nghị*

![Toan Nguyen](/FCAJ_My_Workshop/FCAJ%20June%2027%20assets/Toan%20Nguyen.jpg)

**Nội dung cốt lõi:**
Model Context Protocol (MCP) là cầu nối để AI 'mở rộng' ra thế giới (Jira, Zalo, Gmail, AWS). Tuy nhiên, rủi ro bảo mật là cực lớn. Các diễn giả đã hướng dẫn cách thiết lập VPC Private Connectivity, sử dụng ALB và mã hóa TLS để đảm bảo MCP server nằm trong vùng an toàn (Private Subnet), tránh bị public dữ liệu ra Internet.

> **Trải nghiệm bản thân:**
> Kỹ thuật này nhắc nhở mình rằng: Công nghệ mới luôn đi kèm rủi ro bảo mật mới. Đừng bao giờ ưu tiên sự tiện lợi của AI mà đánh đổi bằng việc public các endpoint nhạy cảm.

---

## Tổng Kết

![Conclusion](/FCAJ_My_Workshop/FCAJ%20June%2027%20assets/conclusion.jpg)

Sau sự kiện, mình rút ra được tư duy cốt lõi: **AI Agent không thay thế con người, nhưng người dùng AI Agent sẽ thay thế người không tận dụng nó.**

Kinh nghiệm rút ra là phải bắt tay vào thiết lập hạ tầng quan sát (Observability) thật tốt, đảm bảo mọi kết nối MCP phải nằm trong VPC an toàn, và quan trọng nhất là thiết kế luồng xử lý AI sao cho con người luôn nắm quyền kiểm soát cuối cùng (Human-in-the-loop).

Không chỉ là xây dựng công cụ, mà là thiết kế một hệ sinh thái vận hành tự động và bảo mật.
