import os
import io

base_path = r"d:\TuMinhDucWorkshop\workshop-site\content"

def read_md(path):
    with io.open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_md(path, content):
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Update Root Indexes
root_en = """---
title: "Internship Report"
weight: 1
---

## Internship Report

**Full Name:** Tu Minh Duc  
**Email:** Tuminhduc20192004@gmail.com  
**University:** Ho Chi Minh City University of Technology  
**Major:** Software Development  
**Class:** 22DTHE4  
**Internship Company:** Amazon Web Services Viet Nam Company Limited  
**Internship Position:** Workforce Bootcamp - First Cloud AI Journey  
**Internship Duration:** From 15/04/2026 to 15/07/2026  

*(Please insert your avatar here by adding an image markdown like `![Avatar](/path/to/avatar.png)`)*

### Report Content

1. [Worklog](1-worklog/)
2. [Proposal](2-proposal/)
3. [Blogs Posted](3-blogsposted/)
4. [Events Participated](4-eventparticipated/)
5. [Workshop](5-workshop/)
6. [Self-evaluation](6-self-assessment/)
7. [Sharing and Feedback](7-sharing-and-feedback/)
"""

root_vi = """---
title: "Báo cáo thực tập"
weight: 1
---

## Báo cáo thực tập

**Họ và tên:** Từ Minh Đức  
**Email:** Tuminhduc20192004@gmail.com  
**Trường Đại học:** HUTECH  
**Chuyên ngành:** Phát triển phần mềm  
**Lớp:** 22DTHE4  
**Công ty thực tập:** Amazon Web Services Viet Nam Company Limited  
**Vị trí thực tập:** Workforce Bootcamp - First Cloud AI Journey  
**Thời gian thực tập:** Từ 15/04/2026 đến 15/07/2026  

*(Vui lòng chèn ảnh đại diện của bạn vào đây bằng cú pháp markdown `![Avatar](/path/to/avatar.png)`)*

### Report Content

1. [Worklog](1-worklog/)
2. [Proposal](2-proposal/)
3. [Blogs Posted](3-blogsposted/)
4. [Events Participated](4-eventparticipated/)
5. [Workshop](5-workshop/)
6. [Self-evaluation](6-self-assessment/)
7. [Sharing and Feedback](7-sharing-and-feedback/)
"""

write_md(os.path.join(base_path, "_index.md"), root_en)
write_md(os.path.join(base_path, "_index.vi.md"), root_vi)

# 2. Update section titles
# Worklog
c = read_md(os.path.join(base_path, "1-Worklog", "_index.md")).replace('title: "Worklog"', 'title: "1. Worklog"')
write_md(os.path.join(base_path, "1-Worklog", "_index.md"), c)
c = read_md(os.path.join(base_path, "1-Worklog", "_index.vi.md")).replace('title: "Nhật ký công việc"', 'title: "1. Worklog"')
write_md(os.path.join(base_path, "1-Worklog", "_index.vi.md"), c)

for i in range(1, 11):
    f_en = os.path.join(base_path, "1-Worklog", f"1.{i}-Week{i}.md")
    f_vi = os.path.join(base_path, "1-Worklog", f"1.{i}-Week{i}.vi.md")
    if os.path.exists(f_en):
        c = read_md(f_en).replace(f'title: "Week {i}"', f'title: "1.{i}. Week {i} Worklog"')
        write_md(f_en, c)
    if os.path.exists(f_vi):
        c = read_md(f_vi).replace(f'title: "Tuần {i}"', f'title: "1.{i}. Week {i} Worklog"')
        write_md(f_vi, c)

# Proposal
c = read_md(os.path.join(base_path, "2-Proposal", "_index.md")).replace('title: "Proposal"', 'title: "2. Proposal"')
write_md(os.path.join(base_path, "2-Proposal", "_index.md"), c)
c = read_md(os.path.join(base_path, "2-Proposal", "_index.vi.md")).replace('title: "Đề xuất (Proposal)"', 'title: "2. Proposal"')
write_md(os.path.join(base_path, "2-Proposal", "_index.vi.md"), c)

# Blogs Posted
c = read_md(os.path.join(base_path, "3-BlogsPosted", "_index.md")).replace('title: "Blogs Posted"', 'title: "3. Blogs Posted"')
write_md(os.path.join(base_path, "3-BlogsPosted", "_index.md"), c)
c = read_md(os.path.join(base_path, "3-BlogsPosted", "_index.vi.md")).replace('title: "Blog Đã Đăng"', 'title: "3. Blogs Posted"')
write_md(os.path.join(base_path, "3-BlogsPosted", "_index.vi.md"), c)

# Events Participated
c = read_md(os.path.join(base_path, "4-EventParticipated", "_index.md")).replace('title: "Event Participated"', 'title: "4. Events Participated"')
write_md(os.path.join(base_path, "4-EventParticipated", "_index.md"), c)
c = read_md(os.path.join(base_path, "4-EventParticipated", "_index.vi.md")).replace('title: "Sự Kiện Đã Tham Gia"', 'title: "4. Events Participated"')
write_md(os.path.join(base_path, "4-EventParticipated", "_index.vi.md"), c)

# Workshop
c = read_md(os.path.join(base_path, "5-Workshop", "_index.md")).replace('title: "Workshop"', 'title: "5. Workshop"')
write_md(os.path.join(base_path, "5-Workshop", "_index.md"), c)
c = read_md(os.path.join(base_path, "5-Workshop", "_index.vi.md")).replace('title: "Workshop"', 'title: "5. Workshop"')
write_md(os.path.join(base_path, "5-Workshop", "_index.vi.md"), c)

# Self-Assessment
c = read_md(os.path.join(base_path, "6-Self-Assessment", "_index.md")).replace('title: "Self-Assessment"', 'title: "6. Self-evaluation"')
write_md(os.path.join(base_path, "6-Self-Assessment", "_index.md"), c)
c = read_md(os.path.join(base_path, "6-Self-Assessment", "_index.vi.md")).replace('title: "Tự đánh giá"', 'title: "6. Self-evaluation"')
write_md(os.path.join(base_path, "6-Self-Assessment", "_index.vi.md"), c)

# Sharing and Feedback
c = read_md(os.path.join(base_path, "7-Sharing-and-Feedback", "_index.md")).replace('title: "Sharing and Feedback"', 'title: "7. Sharing and Feedback"')
write_md(os.path.join(base_path, "7-Sharing-and-Feedback", "_index.md"), c)
c = read_md(os.path.join(base_path, "7-Sharing-and-Feedback", "_index.vi.md")).replace('title: "Chia sẻ và Cảm nhận"', 'title: "7. Sharing and Feedback"')
write_md(os.path.join(base_path, "7-Sharing-and-Feedback", "_index.vi.md"), c)

# Create layouts/partials/logo.html
os.makedirs(r"d:\TuMinhDucWorkshop\workshop-site\layouts\partials", exist_ok=True)
logo_html = """
<a href="{{ "/" | relLangURL }}" id="logo" style="text-align: center; display: block; padding: 1rem;">
  <i class="fab fa-aws" style="font-size: 5rem; color: #fff;"></i>
</a>
"""
write_md(r"d:\TuMinhDucWorkshop\workshop-site\layouts\partials\logo.html", logo_html)

print("Update completed successfully.")
