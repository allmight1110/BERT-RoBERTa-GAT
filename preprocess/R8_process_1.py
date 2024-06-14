with open("E:/文本分类/text_gcn.pytorch-master/建筑20000.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

output_lines = []
for line in lines:
    line = line.strip()
    if line.startswith("标识符"):
        parts = line.split(":")
        identifier = parts[1].split("(")[0].strip()
        dataset = parts[1].split("(")[1].split(")")[0].strip()
    elif line.startswith("类型标识"):
        parts = line.split(":")
        label = parts[1].strip()
        output_lines.append(f"{identifier} {dataset} {label}")

output_file_path = "建筑三列20000.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.writelines("\n".join(output_lines))

print(f"修改后的内容已保存在文件: {output_file_path}")