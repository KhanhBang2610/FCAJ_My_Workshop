import os

file_paths = [
    r"d:\TuMinhDucWorkshop\workshop-site\content\4-EventParticipated\event-1.md",
    r"d:\TuMinhDucWorkshop\workshop-site\content\4-EventParticipated\event-1.en.md"
]

images = {
    "Tinh Truong": "![Tinh Truong](/FCAJ%20May%2023%20assets/Tinh%20Truong.jpg)\n\n",
    "Team VIB": "![Team VIB](/FCAJ%20May%2023%20assets/Team%20VIB.jpg)\n\n",
    "Thinh Nguyen": "![Nguyen Tuan Thinh](/FCAJ%20May%2023%20assets/Thinh%20Nguyen.jpg)\n\n",
    "Hai Anh": "![Pham Hai Anh](/FCAJ%20May%2023%20assets/Hai%20Anh.jpg)\n\n",
    "Vy Lam": "![Vy Lam](/FCAJ%20May%2023%20assets/Vy%20Lam.jpg)\n\n",
    "Conclusion": "![Conclusion](/FCAJ%20May%2023%20assets/Conclusion.jpg)\n\n"
}

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Section 2
    if "**Nội dung cốt lõi:**" in content and "Tính Trương" in content:
        content = content.replace("Anh Tính Trương (Platform Engineer)*\n\n**Nội dung", "Anh Tính Trương (Platform Engineer)*\n\n" + images["Tinh Truong"] + "**Nội dung")
    elif "**Core Content:**" in content and "Tinh Truong" in content:
        content = content.replace("Tinh Truong (Platform Engineer)*\n\n**Core", "Tinh Truong (Platform Engineer)*\n\n" + images["Tinh Truong"] + "**Core")

    # Section 3
    if "Team VIB*\n\n**Nội dung" in content:
        content = content.replace("Team VIB*\n\n**Nội dung", "Team VIB*\n\n" + images["Team VIB"] + "**Nội dung")
    elif "Team VIB*\n\n**Core" in content:
        content = content.replace("Team VIB*\n\n**Core", "Team VIB*\n\n" + images["Team VIB"] + "**Core")

    # Section 4
    if "Tuấn Thịnh (DevOps Engineer)*\n\n**Nội dung" in content:
        content = content.replace("Tuấn Thịnh (DevOps Engineer)*\n\n**Nội dung", "Tuấn Thịnh (DevOps Engineer)*\n\n" + images["Thinh Nguyen"] + "**Nội dung")
    elif "Tuan Thinh (DevOps Engineer)*\n\n**Core" in content:
        content = content.replace("Tuan Thinh (DevOps Engineer)*\n\n**Core", "Tuan Thinh (DevOps Engineer)*\n\n" + images["Thinh Nguyen"] + "**Core")

    # Section 5
    if "Phạm Hải Anh*\n\n**Nội dung" in content:
        content = content.replace("Phạm Hải Anh*\n\n**Nội dung", "Phạm Hải Anh*\n\n" + images["Hai Anh"] + "**Nội dung")
    elif "Hai Anh*\n\n**Core" in content:
        content = content.replace("Hai Anh*\n\n**Core", "Hai Anh*\n\n" + images["Hai Anh"] + "**Core")

    # Section 6
    if "Chị Vy Lâm*\n\n**Vấn đề" in content:
        content = content.replace("Chị Vy Lâm*\n\n**Vấn đề", "Chị Vy Lâm*\n\n" + images["Vy Lam"] + "**Vấn đề")
    elif "Vy Lam*\n\n**Core" in content:
        content = content.replace("Vy Lam*\n\n**Core", "Vy Lam*\n\n" + images["Vy Lam"] + "**Core")

    # Conclusion
    if "## Tổng Kết\n\nĐi nghe" in content:
        content = content.replace("## Tổng Kết\n\nĐi nghe", "## Tổng Kết\n\n" + images["Conclusion"] + "Đi nghe")
    elif "## Conclusion\n\nAfter attending" in content:
        content = content.replace("## Conclusion\n\nAfter attending", "## Conclusion\n\n" + images["Conclusion"] + "After attending")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added images to Markdown files.")
