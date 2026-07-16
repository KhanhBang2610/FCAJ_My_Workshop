import os
import io

base_path = r"d:\TuMinhDucWorkshop\workshop-site\content\1-Worklog"

# Data for 10 weeks
weeks = [
    {
        "week": 1,
        "date_range": "17/04/2026 - 26/04/2026",
        "days": [
            ("Monday", "Tạo tài khoản AWS và cấu hình cơ bản", "Create AWS account and basic config"),
            ("Tuesday", "Tìm hiểu các dịch vụ qua bài lab của AWS", "Learn AWS services via labs"),
            ("Wednesday", "Thực hành lab AWS cơ bản", "Practice basic AWS labs"),
            ("Thursday", "Khảo sát và tìm hiểu về các dự án tiềm năng", "Research potential projects"),
            ("Friday", "Tổng hợp thông tin và báo cáo dự án", "Summarize info and report on project")
        ]
    },
    {
        "week": 2,
        "date_range": "26/04/2026 - 03/05/2026",
        "days": [
            ("Monday", "Nghiên cứu tổng quan về AWS Lambda", "General research on AWS Lambda"),
            ("Tuesday", "Thực hành tạo và chạy hàm AWS Lambda", "Practice creating AWS Lambda functions"),
            ("Wednesday", "Nghiên cứu tổng quan về Amazon VPC", "General research on Amazon VPC"),
            ("Thursday", "Thực hành cấu hình VPC, Subnets", "Practice configuring VPC and Subnets"),
            ("Friday", "Kết hợp Lambda và VPC trong bài lab", "Combine Lambda and VPC in a lab")
        ]
    },
    {
        "week": 3,
        "date_range": "04/05/2026 - 10/05/2026",
        "days": [
            ("Monday", "Lên công ty lần đầu, làm quen môi trường", "First day at office, get familiar with environment"),
            ("Tuesday", "Tham dự sự kiện nội bộ của công ty", "Attend internal company event"),
            ("Wednesday", "Tìm hiểu quy trình làm việc nội bộ", "Learn internal workflows"),
            ("Thursday", "Thảo luận về tiềm năng của các dự án", "Discuss potential projects in the team"),
            ("Friday", "Xác định hướng đi dự án cá nhân/nhóm", "Define direction for team project")
        ]
    },
    {
        "week": 4,
        "date_range": "11/05/2026 - 17/05/2026",
        "days": [
            ("Monday", "Làm việc chính thức tại văn phòng", "Start official office work"),
            ("Tuesday", "Học hỏi quy định, văn hóa công ty", "Learn company rules and culture"),
            ("Wednesday", "Bàn luận chuyên sâu đề tài dự án tổng kết", "Deep discussion on final internship project"),
            ("Thursday", "Tìm kiếm và thu thập dữ liệu (data)", "Search and collect data for project"),
            ("Friday", "Lọc và chuẩn bị dữ liệu thô", "Filter and prepare raw data")
        ]
    },
    {
        "week": 5,
        "date_range": "18/05/2026 - 24/05/2026",
        "days": [
            ("Monday", "Tham dự event 2 & Lên kế hoạch Sprint 1", "Attend 2nd event & Plan Agile Sprint 1"),
            ("Tuesday", "Thiết kế API Data Contract và Schema", "Design API Data Contract and Schema"),
            ("Wednesday", "Khởi tạo FastAPI và Docker Compose", "Init FastAPI and Docker Compose"),
            ("Thursday", "Hỗ trợ xây dựng pipeline AI xử lý media", "Assist in building AI media pipeline"),
            ("Friday", "Xây dựng database và frontend React cơ bản", "Build database and basic React frontend")
        ]
    },
    {
        "week": 6,
        "date_range": "25/05/2026 - 31/05/2026",
        "days": [
            ("Monday", "Triển khai các dịch vụ AI tích hợp Docker", "Deploy AI services via Docker"),
            ("Tuesday", "Xử lý tương thích môi trường dev", "Resolve dev environment compatibility"),
            ("Wednesday", "Kiểm thử (testing) backend FastAPI", "Test FastAPI backend and database"),
            ("Thursday", "Kiểm thử và tinh chỉnh pipeline AI", "Test and refine AI pipelines"),
            ("Friday", "Chuẩn hóa quy trình cho giai đoạn tích hợp", "Standardize workflow for integration phase")
        ]
    },
    {
        "week": 7,
        "date_range": "01/06/2026 - 07/06/2026",
        "days": [
            ("Monday", "Hoàn thiện AI Pipeline (Scene, Image Caption)", "Complete AI Pipeline (Scene, Image Caption)"),
            ("Tuesday", "Tích hợp Audio Transcription vào pipeline", "Integrate Audio Transcription"),
            ("Wednesday", "Tích hợp ChromaDB Vector Store", "Integrate ChromaDB Vector Store"),
            ("Thursday", "Xây dựng API Ingest và API Search", "Build Ingest and Search APIs"),
            ("Friday", "Kiểm thử hệ thống xử lý media bất đồng bộ", "Test async media processing system")
        ]
    },
    {
        "week": 8,
        "date_range": "08/06/2026 - 14/06/2026",
        "days": [
            ("Monday", "Chuyển sang OpenAI Whisper và cập nhật Embedding", "Migrate to OpenAI Whisper & update Embedding"),
            ("Tuesday", "Thiết kế UI trên Figma (Dashboard, Upload)", "Design UI on Figma (Dashboard, Upload)"),
            ("Wednesday", "Xây dựng UI Components (React + Tailwind)", "Build UI Components (React + Tailwind)"),
            ("Thursday", "Thống nhất sơ đồ kiến trúc cloud AWS", "Unify AWS cloud architecture diagram"),
            ("Friday", "Chuẩn bị tài nguyên AWS theo sơ đồ", "Prepare AWS resources based on diagram")
        ]
    },
    {
        "week": 9,
        "date_range": "15/06/2026 - 21/06/2026",
        "days": [
            ("Monday", "Hoàn thiện giao diện Asset Detail Page", "Complete Asset Detail Page UI"),
            ("Tuesday", "Tích hợp API Asset và Upload Video WebSocket", "Integrate Asset API and Upload Video WebSocket"),
            ("Wednesday", "Đồng bộ dữ liệu PostgreSQL và Redis", "Sync PostgreSQL and Redis data"),
            ("Thursday", "Tích hợp Vector Embedding & API Re-Ingest", "Integrate Vector Embedding & Re-Ingest API"),
            ("Friday", "Xây dựng AI Provider cho AWS Bedrock", "Build AI Provider for AWS Bedrock")
        ]
    },
    {
        "week": 10,
        "date_range": "22/06/2026 - 28/06/2026",
        "days": [
            ("Monday", "Kết nối Dashboard với API Backend", "Connect Dashboard with Backend API"),
            ("Tuesday", "Tích hợp Audio Waveform (WaveSurfer.js)", "Integrate Audio Waveform (WaveSurfer.js)"),
            ("Wednesday", "Cải thiện luồng Upload và WebSocket", "Improve Upload and WebSocket flows"),
            ("Thursday", "Điều chỉnh kiến trúc AWS Services", "Adjust AWS Services architecture"),
            ("Friday", "Họp nhóm admin, nhận feedback và tối ưu", "Meeting with admin, feedback and optimize")
        ]
    }
]

def generate_markdown(week_data, lang):
    week_num = week_data["week"]
    date_range = week_data["date_range"]
    
    if lang == "vi":
        title = f'title: "1.{week_num}. Nhật ký Tuần {week_num}"'
        heading = f"### Thời gian: {date_range}\n\nChi tiết công việc trong tuần:\n\n"
        table_header = "| Thứ | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |\n| --- | -------- | ------------ | --------------- | ------------------ |\n"
        days_map = {"Monday": "Thứ 2", "Tuesday": "Thứ 3", "Wednesday": "Thứ 4", "Thursday": "Thứ 5", "Friday": "Thứ 6"}
    else:
        title = f'title: "1.{week_num}. Week {week_num} Worklog"'
        heading = f"### Duration: {date_range}\n\nWeekly task details:\n\n"
        table_header = "| Day | Task | Start Date | Completion Date | Reference Material |\n| --- | ---- | ---------- | --------------- | ------------------ |\n"
        days_map = {"Monday": "Monday", "Tuesday": "Tuesday", "Wednesday": "Wednesday", "Thursday": "Thursday", "Friday": "Friday"}

    table_content = ""
    for day_en, task_vi, task_en in week_data["days"]:
        day_str = days_map[day_en]
        task_str = task_vi if lang == "vi" else task_en
        # We leave dates and reference empty for the user to fill or just generic "-"
        table_content += f"| **{day_str}** | {task_str} | - | - | AWS Docs / Internal |\n"

    content = f"""---
{title}
weight: {week_num}
---

{heading}
{table_header}{table_content}
"""
    return content

for w in weeks:
    # Write VI
    vi_path = os.path.join(base_path, f"1.{w['week']}-Week{w['week']}.md")
    with io.open(vi_path, 'w', encoding='utf-8') as f:
        f.write(generate_markdown(w, "vi"))
        
    # Write EN
    en_path = os.path.join(base_path, f"1.{w['week']}-Week{w['week']}.en.md")
    with io.open(en_path, 'w', encoding='utf-8') as f:
        f.write(generate_markdown(w, "en"))

# Also handle week 11 and 12 as empty templates
for w_num in [11, 12]:
    empty_week = {
        "week": w_num,
        "date_range": "TBD",
        "days": [
            ("Monday", "Đang cập nhật...", "Updating..."),
            ("Tuesday", "Đang cập nhật...", "Updating..."),
            ("Wednesday", "Đang cập nhật...", "Updating..."),
            ("Thursday", "Đang cập nhật...", "Updating..."),
            ("Friday", "Đang cập nhật...", "Updating...")
        ]
    }
    vi_path = os.path.join(base_path, f"1.{w_num}-Week{w_num}.md")
    with io.open(vi_path, 'w', encoding='utf-8') as f:
        f.write(generate_markdown(empty_week, "vi"))
        
    en_path = os.path.join(base_path, f"1.{w_num}-Week{w_num}.en.md")
    with io.open(en_path, 'w', encoding='utf-8') as f:
        f.write(generate_markdown(empty_week, "en"))

print("Generated structured tables for Worklogs.")
