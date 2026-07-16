import os
import io

base_path = r"d:\TuMinhDucWorkshop\workshop-site\content"

def write_md(path, content):
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Root indexes
write_md(os.path.join(base_path, "_index.md"), """---
title: "Internship Report"
weight: 1
---

# Welcome to the Internship Report

This website documents the internship progress and activities of **Từ Minh Đức** at **Bootcamp First Cloud AI Journey**.

Please navigate through the sections on the left to read the worklogs, blogs, event participations, and self-assessment.
""")

write_md(os.path.join(base_path, "_index.vi.md"), """---
title: "Báo cáo thực tập"
weight: 1
---

# Chào mừng đến với Báo cáo thực tập

Trang web này ghi lại quá trình thực tập và các hoạt động của **Từ Minh Đức** tại **Bootcamp First Cloud AI Journey**.

Vui lòng sử dụng menu bên trái để điều hướng qua các phần: nhật ký công việc (worklog), blog, sự kiện đã tham gia và tự đánh giá.
""")

# 1-Worklog
write_md(os.path.join(base_path, "1-Worklog", "_index.md"), "---\ntitle: \"Worklog\"\nweight: 1\n---\n\nOverview of the weekly internship tasks.\n")
write_md(os.path.join(base_path, "1-Worklog", "_index.vi.md"), "---\ntitle: \"Nhật ký công việc\"\nweight: 1\n---\n\nTổng quan các công việc thực tập hàng tuần.\n")

weeks = [
    ("Week 1", "Tuần 1", "17/04/2026 - 26/04/2026", "Thực hiện tạo tài khoản AWS, tìm hiểu các bài lab của AWS, triển khai tìm hiểu về các dự án tiềm năng.", "Created AWS account, researched AWS labs, and explored potential projects."),
    ("Week 2", "Tuần 2", "26/4/2026 - 3/5/2026", "Bắt đầu nghiên cứu các tính năng trong môi trường tài nguyên của AWS như Lambda, VPC,...", "Started researching AWS resource features like Lambda, VPC,..."),
    ("Week 3", "Tuần 3", "4/5/2026 - 10/5/2026", "Tham dự event của công ty cũng như lần đầu lên công ty, gặp gỡ các anh chị admin, khám phá môi trường công ty, triển khai tiềm năng của mỗi dự án của mỗi thành viên trong team.", "Attended company event, visited office for the first time, met admins, explored the company environment, and evaluated potential projects for each team member."),
    ("Week 4", "Tuần 4", "11/5/2026 - 17/5/2026", "Lên văn phòng chính thức của công ty như 1 nhân viên thực tập, làm quen với đồng đội trong team cũng như môi trường làm việc, học hỏi quy định công ty cũng như bàn luận sâu hơn về đề tài dự án tổng kết kì thực tập, tìm kiếm data của dự án cuối kì.", "Officially started at the office as an intern, got acquainted with teammates and the work environment, learned company regulations, and had deep discussions about the final internship project and data gathering."),
    ("Week 5", "Tuần 5", "18/5/2026 - 24/5/2026", "- Dự event thứ 2 của công ty\n- Triển khai dự án nhóm theo mô hình Agile Sprint Week 1\n- Thiết kế API Data Contract và chuẩn hóa schema dữ liệu cho backend/frontend\n- Cấu hình môi trường Docker Compose cho frontend, backend và ChromaDB\n- Hỗ trợ xây dựng pipeline AI xử lý media: scene detection, image captioning và audio transcription\n- Khởi tạo FastAPI backend, thiết kế database schema và xây dựng giao diện frontend cơ bản bằng React + Tailwind CSS", "- Attended the 2nd company event\n- Started group project using Agile Sprint Week 1\n- Designed API Data Contract and standardized data schemas for backend/frontend\n- Configured Docker Compose environment for frontend, backend, and ChromaDB\n- Supported building AI media processing pipeline: scene detection, image captioning, and audio transcription\n- Initialized FastAPI backend, designed database schema, and built basic frontend interface using React + Tailwind CSS"),
    ("Week 6", "Tuần 6", "25/5/2026 - 31/5/2026", "- Tiếp tục triển khai dự án nhóm sử dụng Docker và các dịch vụ AI tích hợp\n- Xử lý các vấn đề tương thích phiên bản và tối ưu môi trường phát triển giữa các thành viên\n- Thực hiện kiểm thử backend FastAPI, database và các pipeline xử lý dữ liệu\n- Hoàn thiện cấu hình hệ thống và chuẩn hóa quy trình triển khai dự án\n- Chuẩn bị cho giai đoạn tích hợp và phát triển các tính năng tiếp theo của dự án nhóm", "- Continued deploying group project using Docker and integrated AI services\n- Handled version compatibility issues and optimized development environment across team members\n- Tested FastAPI backend, database, and data processing pipelines\n- Finalized system configuration and standardized deployment workflow\n- Prepared for the integration phase and development of next features"),
    ("Week 7", "Tuần 7", "01/06/2026 - 07/06/2026", "- Hoàn thiện AI Pipeline xử lý video gồm Scene Detection, Audio Transcription và Image Captioning.\n- Tích hợp ChromaDB Vector Store phục vụ lưu trữ và tìm kiếm ngữ nghĩa.\n- Xây dựng API Search và API Ingest trên FastAPI, hỗ trợ xử lý media bất đồng bộ.\n- Thực hiện kiểm thử và tối ưu pipeline AI nhằm đảm bảo tính ổn định của hệ thống.", "- Completed AI Video Processing Pipeline including Scene Detection, Audio Transcription, and Image Captioning.\n- Integrated ChromaDB Vector Store for storage and semantic search.\n- Built Search and Ingest APIs on FastAPI, supporting asynchronous media processing.\n- Tested and optimized the AI pipeline to ensure system stability."),
    ("Week 8", "Tuần 8", "08/06/2026 - 14/06/2026", "- Tối ưu AI Pipeline bằng cách chuyển từ WhisperX sang OpenAI Whisper và cập nhật mô hình Embedding phù hợp.\n- Xây dựng các UI Components và khung giao diện cơ bản cho Dashboard bằng React + Tailwind CSS.\n- Thiết kế và hoàn thiện các màn hình trên Figma như Dashboard, Upload, Login, Register và Asset Media Detail.\n- Thống nhất kiến trúc hệ thống, các dịch vụ triển khai trên AWS và xây dựng sơ đồ kiến trúc cloud cho dự án.", "- Optimized AI Pipeline by migrating from WhisperX to OpenAI Whisper and updating the embedding model.\n- Built UI Components and basic dashboard layout using React + Tailwind CSS.\n- Designed and finalized Figma screens including Dashboard, Upload, Login, Register, and Asset Media Detail.\n- Unified system architecture, AWS deployment services, and created a cloud architecture diagram for the project."),
    ("Week 9", "Tuần 9", "15/06/2026 - 21/06/2026", "- Hoàn thiện thiết kế giao diện Asset Detail dựa trên thiết kế Figma.\n- Phát triển các component chính của Asset Detail Page.\n- Tích hợp API Asset, Scene và Video Streaming.\n- Xây dựng luồng Upload Video và theo dõi tiến trình bằng WebSocket.\n- Hỗ trợ quản lý nhiều tiến trình xử lý đồng thời và khôi phục trạng thái sau khi refresh.\n- Phát triển API Re-Ingest và Regenerate Insights.\n- Hoàn thiện AI Pipeline và đồng bộ dữ liệu vào PostgreSQL, Redis.\n- Tích hợp Vector Embedding phục vụ Semantic Search.\n- Xây dựng abstraction cho AI Provider phục vụ triển khai AWS Bedrock.\n- Điều chỉnh và hoàn thiện kiến trúc triển khai AWS.", "- Completed Asset Detail interface design based on Figma.\n- Developed core components for the Asset Detail Page.\n- Integrated Asset, Scene, and Video Streaming APIs.\n- Built Video Upload flow and tracked progress via WebSocket.\n- Supported managing multiple concurrent processes and restoring state after refresh.\n- Developed Re-Ingest and Regenerate Insights APIs.\n- Finalized AI Pipeline and synchronized data to PostgreSQL and Redis.\n- Integrated Vector Embedding for Semantic Search.\n- Built abstraction for AI Provider for AWS Bedrock deployment.\n- Adjusted and finalized AWS deployment architecture."),
    ("Week 10", "Tuần 10", "22/06/2026 - 28/06/2026", "- Tích hợp Dashboard với API Backend và đồng bộ trạng thái Asset theo thời gian thực.\n- Kết nối Asset Detail với API, Video Streaming và In-Video Search.\n- Tích hợp Audio Waveform và đồng bộ phát video bằng WaveSurfer.js.\n- Nâng cấp luồng Upload, WebSocket và In-Video Search trên Backend.\n- Cải thiện luồng Upload, quản lý WebSocket và xử lý đa tiến trình trên Frontend.\n- Hoàn thiện kiến trúc hệ thống và điều chỉnh phương án sử dụng các AWS Services.\n- Họp nhóm, trao đổi với admin FCAJ và tiếp nhận feedback để tối ưu kiến trúc hệ thống.", "- Integrated Dashboard with Backend API and synchronized real-time Asset state.\n- Connected Asset Detail with API, Video Streaming, and In-Video Search.\n- Integrated Audio Waveform and synchronized video playback using WaveSurfer.js.\n- Upgraded Upload flow, WebSocket, and In-Video Search on the Backend.\n- Improved Upload flow, WebSocket management, and multi-process handling on the Frontend.\n- Finalized system architecture and adjusted AWS Services usage plan.\n- Held team meetings, communicated with FCAJ admins, and incorporated feedback to optimize system architecture.")
]

for i, w in enumerate(weeks):
    idx = i + 1
    # EN
    write_md(os.path.join(base_path, "1-Worklog", f"1.{idx}-Week{idx}.md"), f"---\ntitle: \"{w[0]}\"\nweight: {idx}\n---\n\n### Date: {w[2]}\n\n{w[4]}\n")
    # VI
    write_md(os.path.join(base_path, "1-Worklog", f"1.{idx}-Week{idx}.vi.md"), f"---\ntitle: \"{w[1]}\"\nweight: {idx}\n---\n\n### Thời gian: {w[2]}\n\n{w[3]}\n")

# 2-Proposal
write_md(os.path.join(base_path, "2-Proposal", "_index.md"), "---\ntitle: \"Proposal\"\nweight: 2\n---\n\n*Content pending...*\n")
write_md(os.path.join(base_path, "2-Proposal", "_index.vi.md"), "---\ntitle: \"Đề xuất (Proposal)\"\nweight: 2\n---\n\n*Nội dung đang chờ cập nhật...*\n")

# 3-BlogsPosted
write_md(os.path.join(base_path, "3-BlogsPosted", "_index.md"), "---\ntitle: \"Blogs Posted\"\nweight: 3\n---\n\n")
write_md(os.path.join(base_path, "3-BlogsPosted", "_index.vi.md"), "---\ntitle: \"Blog Đã Đăng\"\nweight: 3\n---\n\n")
for i in range(1, 4):
    write_md(os.path.join(base_path, "3-BlogsPosted", f"blog-{i}.md"), f"---\ntitle: \"Blog {i}\"\nweight: {i}\n---\n\n*Content for Blog {i}*\n")
    write_md(os.path.join(base_path, "3-BlogsPosted", f"blog-{i}.vi.md"), f"---\ntitle: \"Blog {i}\"\nweight: {i}\n---\n\n*Nội dung bài Blog {i}*\n")

# 4-EventParticipated
write_md(os.path.join(base_path, "4-EventParticipated", "_index.md"), "---\ntitle: \"Event Participated\"\nweight: 4\n---\n\n")
write_md(os.path.join(base_path, "4-EventParticipated", "_index.vi.md"), "---\ntitle: \"Sự Kiện Đã Tham Gia\"\nweight: 4\n---\n\n")
for i in range(1, 5):
    write_md(os.path.join(base_path, "4-EventParticipated", f"event-{i}.md"), f"---\ntitle: \"Event {i}\"\nweight: {i}\n---\n\n*Content for Event {i}*\n")
    write_md(os.path.join(base_path, "4-EventParticipated", f"event-{i}.vi.md"), f"---\ntitle: \"Sự kiện {i}\"\nweight: {i}\n---\n\n*Nội dung sự kiện {i}*\n")

# 5-Workshop
write_md(os.path.join(base_path, "5-Workshop", "_index.md"), "---\ntitle: \"Workshop\"\nweight: 5\n---\n\n*Content pending...*\n")
write_md(os.path.join(base_path, "5-Workshop", "_index.vi.md"), "---\ntitle: \"Workshop\"\nweight: 5\n---\n\n*Nội dung đang chờ cập nhật...*\n")

# 6-Self-Assessment
self_eval_vi = '''---
title: "Tự đánh giá"
weight: 6
---

Để nhìn nhận một cách khách quan về quá trình thực tập, tôi xin tự đánh giá dựa trên các tiêu chí sau:

| STT | Tiêu chí | Mô tả | Tốt | Khá | Trung bình |
| --- | -------- | ----- | --- | --- | ---------- |
| 1 | **Kiến thức & Kỹ năng chuyên môn** | Hiểu biết về lĩnh vực, áp dụng vào thực tế, sử dụng thành thạo các công cụ | ☐ | ☐ | ☐ |
| 2 | **Khả năng học hỏi** | Khả năng tiếp thu kiến thức mới và học hỏi nhanh | ☐ | ☐ | ☐ |
| 3 | **Sự chủ động** | Chủ động trong công việc, tìm kiếm nhiệm vụ mà không chờ nhắc nhở | ☐ | ☐ | ☐ |
| 4 | **Tinh thần trách nhiệm** | Hoàn thành công việc đúng hạn và đảm bảo chất lượng | ☐ | ☐ | ☐ |
| 5 | **Tính kỷ luật** | Tuân thủ giờ giấc, nội quy và quy trình làm việc | ☐ | ☐ | ☐ |
| 6 | **Tinh thần cầu tiến** | Sẵn sàng đón nhận góp ý và cải thiện bản thân | ☐ | ☐ | ☐ |
| 7 | **Giao tiếp** | Trình bày ý tưởng và báo cáo công việc rõ ràng | ☐ | ☐ | ☐ |
| 8 | **Làm việc nhóm** | Làm việc hiệu quả với đồng nghiệp và tham gia nhóm tốt | ☐ | ☐ | ☐ |
| 9 | **Thái độ chuyên nghiệp** | Tôn trọng đồng nghiệp, đối tác và môi trường làm việc | ☐ | ☐ | ☐ |
| 10 | **Kỹ năng giải quyết vấn đề** | Nhận diện vấn đề, đề xuất giải pháp và thể hiện sự sáng tạo | ☐ | ☐ | ☐ |
| 11 | **Đóng góp cho dự án/nhóm** | Hiệu quả công việc, ý tưởng đột phá, được nhóm ghi nhận | ☐ | ☐ | ☐ |
| 12 | **Đánh giá chung** | Nhận xét tổng quan về toàn bộ kỳ thực tập | ☐ | ☐ | ☐ |
'''

self_eval_en = '''---
title: "Self-Assessment"
weight: 6
---

To objectively reflect on my internship period, I would like to evaluate myself based on the following criteria:

| No. | Criteria | Description | Good | Fair | Average |
| --- | -------- | ----------- | ---- | ---- | ------- |
| 1 | **Professional knowledge & skills** | Understanding of the field, applying knowledge in practice, proficiency with tools | ☐ | ☐ | ☐ |
| 2 | **Ability to learn** | Ability to absorb new knowledge and learn quickly | ☐ | ☐ | ☐ |
| 3 | **Proactiveness** | Taking initiative, seeking out tasks without waiting for instructions | ☐ | ☐ | ☐ |
| 4 | **Sense of responsibility** | Completing tasks on time and ensuring quality | ☐ | ☐ | ☐ |
| 5 | **Discipline** | Adhering to schedules, rules, and work processes | ☐ | ☐ | ☐ |
| 6 | **Progressive mindset** | Willingness to receive feedback and improve oneself | ☐ | ☐ | ☐ |
| 7 | **Communication** | Presenting ideas and reporting work clearly | ☐ | ☐ | ☐ |
| 8 | **Teamwork** | Working effectively with colleagues and participating in teams | ☐ | ☐ | ☐ |
| 9 | **Professional conduct** | Respecting colleagues, partners, and the work environment | ☐ | ☐ | ☐ |
| 10 | **Problem-solving skills** | Identifying problems, proposing solutions, and showing creativity | ☐ | ☐ | ☐ |
| 11 | **Contribution to project/team** | Work effectiveness, innovative ideas, recognition from the team | ☐ | ☐ | ☐ |
| 12 | **Overall** | General evaluation of the entire internship period | ☐ | ☐ | ☐ |
'''
write_md(os.path.join(base_path, "6-Self-Assessment", "_index.md"), self_eval_en)
write_md(os.path.join(base_path, "6-Self-Assessment", "_index.vi.md"), self_eval_vi)

# 7-Sharing-and-Feedback
write_md(os.path.join(base_path, "7-Sharing-and-Feedback", "_index.md"), "---\ntitle: \"Sharing and Feedback\"\nweight: 7\n---\n\n*Content pending...*\n")
write_md(os.path.join(base_path, "7-Sharing-and-Feedback", "_index.vi.md"), "---\ntitle: \"Chia sẻ và Cảm nhận\"\nweight: 7\n---\n\n*Nội dung đang chờ cập nhật...*\n")

print("Content generated successfully.")
