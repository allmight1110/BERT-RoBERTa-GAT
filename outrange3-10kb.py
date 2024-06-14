#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author zhouhuawei time:2023/12/30
import os

def delete_invalid_txt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            file_size = os.path.getsize(file_path) / 1024  # 获取文件大小并转换为KB
            if file_size < 3 or file_size > 9:
                os.remove(file_path)

# 使用示例：
delete_invalid_txt_files("E:/建筑数据集处理后/建筑行业新闻")