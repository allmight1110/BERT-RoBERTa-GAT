#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author zhouhuawei time:2023/11/2
def extract_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()

    lines = data.split('\n')
    max_identifier = 0

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith('文件内容:'):
                content = line.split(':', 1)[1]
                file.write(content + '\n')

            if line.startswith('标识符:'):
                identifier = int(line.split(' ')[1])
                max_identifier = max(max_identifier, identifier)

    num_lines = max_identifier + 1
    print(f"提取并写入了 {num_lines} 行到新的txt文件中。")

# 调用函数进行提取和写入操作
extract_lines('建筑20000.txt', '建筑_corpus20000.txt')