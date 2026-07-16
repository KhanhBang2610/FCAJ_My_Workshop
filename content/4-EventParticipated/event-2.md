---
title: "4.2. Báo cáo thu hoạch: Event FCAJ Community Day"
weight: 2
---

## Báo cáo thu hoạch: Những Kiến Thức Bản Thân Học Được Qua Event FCAJ Community Day ngày 23/5/2026

Chào mọi người,

Hôm nay mình muốn ngồi lại, gõ vài dòng recap về sự kiện công nghệ **FCAJ Community Day** diễn ra vào ngày 23/5 vừa qua.

Dưới đây là 6 bài học, 6 trải nghiệm thực tế từ các diễn giả đã mang lại cho bản thân mình nhiều góc nhìn mới, không chỉ về công nghệ mà còn là kinh nghiệm về việc xử lý công việc sao cho đúng để mang lại hiệu suất tốt nhất.

---

### 1. Sự bất trị của LLM: Khi Temp = 0 cũng không cản được AI "quay xe"
*Diễn giả: Anh Đức Đào (Solution Architect)*

**Nội dung cốt lõi:**
Bài nói của anh Đức Đào đã giúp mình có một nhìn nhận khác. Lâu nay, khi code các luồng tích hợp AI, mình luôn đinh ninh rằng cứ set tham số `temperature = 0` là hệ thống sẽ trả về đúng một định dạng JSON chuẩn xác 100% cho mọi lần gọi. Nhưng sự thật là: LLM vẫn có thể đưa ra kết quả khác nhau! Nguyên nhân sâu xa đến từ sai số số thực dấu phẩy động (floating-point) trên kiến trúc GPU và cơ chế tối ưu hóa batching của các nhà cung cấp.

> **Trải nghiệm bản thân:**
> Lúc nghe đến đoạn nguyên nhân từ phần cứng GPU, mình thực sự hiểu khác. Thật ra AI là xác suất, không phải là hàm toán học tuyến tính. Thay vì cố gắng ép nó thành một cỗ máy cứng nhắc, lời khuyên của anh Đức là hãy dùng `temperature = 0.1` để tránh model bị lặp từ vựng, kết hợp với JSON mode và quan trọng nhất: **Thiết kế hệ thống backend phải chấp nhận sự biến thiên của đầu ra**. Rõ ràng, việc lường trước lỗi và xử lý ngoại lệ (Exception Handling) rất quan trọng.

---

### 2. Dừng ngay việc làm "Kẻ gom rác Internet"
*Diễn giả: Anh Tính Trương (Platform Engineer)*

![Tinh Truong](/FCAJ%20May%2023%20assets/Tinh%20Truong.jpg)

**Nội dung cốt lõi:**
Anh Tính Trương đã bóc trần một sự thật phũ phàng: Mô hình AI trả lời "ngáo" thường không phải do nó dở, mà do chúng ta cung cấp sai ngữ cảnh. Rất nhiều người đang mắc kẹt ở hội chứng "Internet Puller" – tống vào mặt AI một đống thông tin hổ lốn, thừa thãi, hoặc đưa ra những yêu cầu mơ hồ không ràng buộc. Giải pháp anh đưa ra là xây dựng một **"Second AI Brain"** với luồng chuẩn mực: `Lưu trữ -> Truy xuất -> Tạo phản hồi -> Học hỏi`.

> **Trải nghiệm bản thân:**
> Nói thật là nhột! Đã bao lần mình copy nguyên một file document dài dằng dặc quăng vào các công cụ AI Agent như Cursor hay Trae rồi bực mình khi nó code không theo ý mình. Bài chia sẻ này giúp mình định hình lại cách xây dựng các hệ thống RAG (Retrieval-Augmented Generation). Chất lượng của Vector DB phụ thuộc hoàn toàn vào cách chúng ta làm sạch và phân mảnh dữ liệu (Chunking) ở bước "Lưu trữ", chứ không phải ở việc model đó có bao nhiêu tỷ tham số.

---

### 3. 36 hours, one product
*Diễn giả: Team VIB*

![Team VIB](/FCAJ%20May%2023%20assets/Team%20VIB.jpg)

**Nội dung cốt lõi:**
Team VIB đã tổng kết về hành trình của đội ngũ phát triển dự án UTMorpho tại LotusHacks, sự kiện lập trình có quy mô lớn nhất Việt Nam. Quá trình chuyển hóa từ một ý tưởng sơ khai thành một sản phẩm thực tế chỉ trong 36 giờ làm việc áp lực cao, đồng thời nhấn mạnh vào các bài học về khả năng chịu đựng và sự phối hợp nhóm.

Với vị thế là đội giành chiến thắng trong phân nhánh AWS Track, nhóm tác giả đã chia sẻ các cột mốc quan trọng từ khâu xác định vấn đề cho đến những thất bại mang tính bước ngoặt. Cuối cùng, định hướng tương lai nhằm tích hợp sản phẩm vào quy trình công việc thực tế và tiếp tục lan tỏa tinh thần học hỏi thông qua các nền tảng mã nguồn mở được vạch ra.

---

### 4. CloudFront không chỉ là CDN, nó là nền tảng bảo vệ, tối ưu hóa ứng dụng
*Diễn giả: Anh Nguyễn Tuấn Thịnh (DevOps Engineer)*

![Nguyen Tuan Thinh](/FCAJ%20May%2023%20assets/Thinh%20Nguyen.jpg)

**Nội dung cốt lõi:**
CDN thường bị xem là lớp hạ tầng phụ trợ, nhưng anh Thịnh đã chứng minh điều ngược lại. Bên cạnh sức mạnh từ hơn 700 điểm PoP toàn cầu giúp giảm độ trễ, CloudFront còn có khả năng chặn đứng DDoS ngay tại Edge thay vì phải đợi 3-4 phút như trước.

Đặc biệt, bản update Flat-rate pricing (ra mắt vào 18/11/2025) giúp cố định hóa đơn hàng tháng, cộng với tính năng cache và nén dữ liệu giảm tới 82% dung lượng file.
Ngoài ra, nó còn mang độ tin cậy khi có thể tự động chuyển hướng traffic đến Origin phụ (Secondary Origin) khi Origin chính gặp sự cố, cũng như phản hồi nội dung cũ từ cache khi Origin gặp lỗi (timeout) để đảm bảo trải nghiệm người dùng không bị gián đoạn.

> **Trải nghiệm bản thân:**
> Mình nhận ra đôi khi tối ưu code đến mệt cũng không tiết kiệm tài nguyên EC2 hay ALB bằng việc cấu hình đúng lớp mạng bên ngoài. Giảm 82% băng thông tải tĩnh và không bao giờ phải sợ hóa đơn AWS nhảy vọt do traffic tăng đột biến.

---

### 5. Ủy quyền sự nhàm chán cho Amazon Quick Suite
*Diễn giả: Anh Phạm Hải Anh*

![Pham Hai Anh](/FCAJ%20May%2023%20assets/Hai%20Anh.jpg)

**Nội dung cốt lõi:**
Với chủ đề Tự động hóa, anh Hải Anh giới thiệu về Amazon Quick Suite (Agentic AI). Công cụ này kết nối trực tiếp với hơn 40 nguồn dữ liệu khác nhau, tự động hóa hàng ngàn tác vụ trên các ứng dụng bên thứ ba. Từ việc lên lịch họp, tự soạn email, cho đến tạo biên bản cuộc họp (MoM) một cách chuẩn xác với các tính năng nổi bật:
- **Dữ liệu và Kiến thức:** Sử dụng dữ liệu công ty thông qua các Spaces/datasets, kết hợp kiến thức thế giới, hỗ trợ tải lên file, kết nối DBs và hơn 40 Data connectors.
- **Khả năng thực thi (Actions):** Thực hiện hàng nghìn hành động trong các ứng dụng bên thứ ba, cung cấp các UI và API có thể nhúng.
- **Quản trị và Bảo mật (Responsible AI):** Đảm bảo tuân thủ quy định, kiểm soát truy cập và bảo mật dữ liệu qua Guardrails & Governance.
- **Tính năng ứng dụng (BI & Automation):** Cung cấp Dashboards, Scenarios, Insights. Hỗ trợ các luồng tự động hóa cho nhiều phòng ban như Sales, Marketing, HR và Support.

> **Trải nghiệm bản thân:**
> Với việc mình là người không thích phải viết báo cáo hay tổng hợp log sau mỗi chặng dự án, việc có một "đại lý AI" lo liệu toàn bộ các tác vụ này thực sự giúp bản thân mình tối ưu hiệu suất làm việc. Nó cho phép mình tập trung toàn lực vào việc tư duy luồng dữ liệu (data flow) thay vì kẹt lại trong các tác vụ hành chính.

---

### 6. Enterprise-Grade Multi-Agent System
*Diễn giả: Chị Vy Lâm*

![Vy Lam](/FCAJ%20May%2023%20assets/Vy%20Lam.jpg)

**Vấn đề cốt lõi:** 
Chị Vy đã phân tích các mô hình đánh giá tín dụng truyền thống không phù hợp với thực tế của startup (yêu cầu lịch sử tài chính dài hạn, tài sản thế chấp trong khi startup có mô hình mới, dữ liệu phi cấu trúc).

**Giải pháp đa tác tử (Multi-Agent Paradigm):** 
Xây dựng "Ủy ban tín dụng ảo" với các tác tử chuyên biệt (Tài chính, Thị trường, Đội ngũ, Rủi ro, Tuân thủ) để phân tích đa chiều thay vì dùng một mô hình đơn lẻ.

**Hiệu quả (ROI):** 
Việc chuyển đổi sang hệ thống đa tác tử giúp tối ưu hóa đáng kể quy trình vận hành, giảm chi phí và thời gian xử lý.

---

## Tổng Kết

![Conclusion](/FCAJ%20May%2023%20assets/Conclusion.jpg)

Đi nghe một vòng, trải nghiệm lớn nhất mình nhận được là một sự thay đổi về nhiều góc nhìn. Không còn tư duy phụ thuộc tuyệt đối vào máy móc, không còn cắm đầu nhồi nhét dữ liệu vô tội vạ. 

Qua đó, kinh nghiệm mình rút ra được là chắc chắn phải lôi hệ thống ra, kiểm tra lại cấu hình nén của CloudFront, tinh chỉnh lại tham số Temperature, và vẽ lại toàn bộ luồng xử lý AI theo hướng thiết kế chấp nhận sai số. 

**Không quá quan trọng code sao cho chạy, mà là thiết kế sao cho hệ thống đủ tốt để phù hợp với yêu cầu của doanh nghiệp.**
