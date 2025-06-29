# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-29 12:27
#  @FileName: name.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
import os

# 遍历某个文件夹下的所有py文件
# 开头写入
# -------------------------------
header_content = "from config import Sbus, Settings ,Logger"


# 要遍历的目录
folder_path = "E:/python/MCServer"  # 替换为你的目标文件夹路径

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)

            # 读取原文件内容
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.read()

            # 写入头部 + 原内容
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(header_content + original_content)

print("已向所有 .py 文件开头写入指定内容。")