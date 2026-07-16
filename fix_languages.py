import os
import glob
import re

base_path = r"d:\TuMinhDucWorkshop\workshop-site\content"

translations = {
    'title: "1. Worklog"': 'title: "1. Nhật ký công việc"',
    'title: "2. Proposal"': 'title: "2. Đề xuất (Proposal)"',
    'title: "3. Blogs Posted"': 'title: "3. Blog đã đăng"',
    'title: "4. Events Participated"': 'title: "4. Sự kiện đã tham gia"',
    'title: "5. Workshop"': 'title: "5. Hội thảo (Workshop)"',
    'title: "6. Self-evaluation"': 'title: "6. Tự đánh giá"',
    'title: "7. Sharing and Feedback"': 'title: "7. Chia sẻ và Cảm nhận"',
}

# 1. Rename English files (*.md that are not *.vi.md) to *.en.md
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".md") and not file.endswith(".vi.md") and not file.endswith(".en.md"):
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, file.replace(".md", ".en.md"))
            os.rename(old_path, new_path)

# 2. Process Vietnamese files (*.vi.md) -> Translate titles -> Rename to *.md
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".vi.md"):
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, file.replace(".vi.md", ".md"))
            
            with open(old_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply static translations
            for en_title, vi_title in translations.items():
                content = content.replace(en_title, vi_title)
            
            # Apply dynamic translations (Week X Worklog -> Nhật ký Tuần X)
            content = re.sub(r'title: "1\.(\d+)\. Week \d+ Worklog"', r'title: "1.\1. Nhật ký Tuần \1"', content)
            
            # Apply dynamic translations (Event X -> Sự kiện X)
            content = re.sub(r'title: "Event (\d+)"', r'title: "Sự kiện \1"', content)
            
            # For Report Content in _index.md (which is now Vietnamese)
            content = content.replace("### Report Content", "### Nội dung Báo cáo")
            content = content.replace("1. [Worklog](1-worklog/)", "1. [Nhật ký công việc](1-worklog/)")
            content = content.replace("2. [Proposal](2-proposal/)", "2. [Đề xuất](2-proposal/)")
            content = content.replace("3. [Blogs Posted](3-blogsposted/)", "3. [Blog đã đăng](3-blogsposted/)")
            content = content.replace("4. [Events Participated](4-eventparticipated/)", "4. [Sự kiện đã tham gia](4-eventparticipated/)")
            content = content.replace("5. [Workshop](5-workshop/)", "5. [Hội thảo](5-workshop/)")
            content = content.replace("6. [Self-evaluation](6-self-assessment/)", "6. [Tự đánh giá](6-self-assessment/)")
            content = content.replace("7. [Sharing and Feedback](7-sharing-and-feedback/)", "7. [Chia sẻ và Cảm nhận](7-sharing-and-feedback/)")
            
            with open(old_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            os.rename(old_path, new_path)

print("Fixed language mapping and translated Vietnamese titles.")
