#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author zhouhuawei time:2023/11/2
import os
import random
import re
def contains_non_numeric_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fff]')
    return bool(pattern.search(text)) and not text.isdigit()

# 主文件夹路径
main_folder = "E:/建筑数据集处理后"

# 创建一个字典来存储每个子文件夹的提取文件数量和标识符偏移量
folder_extracted_files = {}
folder_identifier_offsets = {}

# 遍历每个子文件夹
for sub_folder in os.listdir(main_folder):
    sub_folder_path = os.path.join(main_folder, sub_folder)

    # 检查子文件夹是否存在
    if os.path.isdir(sub_folder_path):
        # 获取子文件夹中所有大小介于3,000到10,000字节且行数介于3到8行的txt文件路径
        small_files = [
            file for file in os.listdir(sub_folder_path) if file.endswith(".txt")
            and 3000 < os.path.getsize(os.path.join(sub_folder_path, file)) < 10000
            # and 3 < len(open(os.path.join(sub_folder_path, file), 'r', encoding='utf-8').readlines()) < 20
            and contains_non_numeric_chinese(open(os.path.join(sub_folder_path, file), "r", encoding="utf-8").read())
        ]
        # 计算当前子文件夹应提取的文件数量
        total_small_files = len(small_files)
        folder_extracted_files[sub_folder] = total_small_files

# 计算每个子文件夹实际提取的文件数量和标识符偏移量
total_extracted_files = 20000
extracted_files = {}
identifier_offset = 0
for sub_folder, count in folder_extracted_files.items():
    ratio = count / sum(folder_extracted_files.values())
    extracted_count = int(ratio * total_extracted_files)
    extracted_files[sub_folder] = extracted_count
    folder_identifier_offsets[sub_folder] = identifier_offset
    identifier_offset += extracted_count

# 提取文件内容并保存到一个txt文件中
with open("建筑20000.txt", "w", encoding="utf-8") as output_file:
    for sub_folder, count in extracted_files.items():
        sub_folder_path = os.path.join(main_folder, sub_folder)
        small_files = [file for file in os.listdir(sub_folder_path) if file.endswith(".txt")
                       and 3000 < os.path.getsize(os.path.join(sub_folder_path, file)) < 10000
                       # and 3 < len(open(os.path.join(sub_folder_path, file), 'r', encoding='utf-8').readlines()) < 20
                       and contains_non_numeric_chinese(open(os.path.join(sub_folder_path, file), "r", encoding="utf-8").read())]

        random.shuffle(small_files)
        selected_files = small_files[:count]
        output_file.write(f"子文件夹名称: {sub_folder}\n")
        train_count = int(0.7 * len(selected_files))
        train_files = selected_files[:train_count]
        test_files = selected_files[train_count:]
        for index, file_name in enumerate(train_files):
            file_path = os.path.join(sub_folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as input_file:
                lines = input_file.readlines()
                content = " ".join([line.strip() for line in lines])
                identifier = folder_identifier_offsets[sub_folder] + index
                output_file.write(f"标识符: {identifier} (训练集)\n")
                output_file.write(f"文件名: {file_name}\n")
                output_file.write(f"类型标识: {sub_folder}\n")
                output_file.write(f"文件内容: {content}\n\n")
        for index, file_name in enumerate(test_files):
            file_path = os.path.join(sub_folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as input_file:
                lines = input_file.readlines()
                content = " ".join([line.strip() for line in lines])
                identifier = folder_identifier_offsets[sub_folder] + index + len(train_files)
                output_file.write(f"标识符: {identifier} (测试集)\n")
                output_file.write(f"文件名: {file_name}\n")
                output_file.write(f"类型标识: {sub_folder}\n")
                output_file.write(f"文件内容: {content}\n\n")

print("内容已保存")