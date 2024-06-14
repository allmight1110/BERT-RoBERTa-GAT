#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author zhouhuawei time:2023/10/21
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, f1_score, precision_score
import sys


# 1. 数据准备
# 加载词向量和类别标签数据
word_vectors = []
labels = []

with open('E:/建筑R8/embedding_sentence_20000.txt', 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        label = int(line[0])
        vector = [float(x) for x in line[1:]]
        labels.append(label)
        word_vectors.append(vector)

# with open('E:/word_vectors.txt', 'w') as file:
#     for vector in word_vectors:
#         vector_str = ' '.join(str(num) for num in vector)
#         file.write(vector_str + '\n')
#print('word_vectors[0]:',word_vectors[0])

# 转换为PyTorch张量
word_vectors = torch.tensor(word_vectors, dtype=torch.float32)
labels = torch.tensor(labels, dtype=torch.long)

# 2. 构建模型
class Classifier(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(Classifier, self).__init__()
        self.fc = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.fc(x)
        return out

# 定义模型参数
input_dim = len(word_vectors[0])
output_dim = 14

# 创建模型实例
model = Classifier(input_dim, output_dim)

# 3. 模型训练
# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 划分训练集和验证集(错误)
# train_ratio = 0.8
# train_size = int(train_ratio * len(word_vectors))
# train_data = word_vectors[:train_size]
# train_labels = labels[:train_size]
# val_data = word_vectors[train_size:]
# val_labels = labels[train_size:]
train_data, val_data, train_labels, val_labels = train_test_split(word_vectors, labels, test_size=0.2, stratify=labels, random_state=3072)


# 设置训练参数
num_epochs = 300
batch_size = 32

# 进行训练
for epoch in range(num_epochs):
    running_loss = 0.0
    correct = 0
    total = 0

    for i in range(0, len(train_data), batch_size):
        inputs = train_data[i:i+batch_size]
        target = train_labels[i:i+batch_size]

        outputs = model(inputs)
        loss = criterion(outputs, target)

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # 计算训练准确率
        _, predicted = torch.max(outputs, dim=1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

    # 打印每个epoch的损失和训练准确率
    train_loss = running_loss / len(train_data)
    train_acc = correct / total
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {train_loss}, Train Accuracy: {train_acc}')


# 在验证集上进行预测
with torch.no_grad():
    outputs = model(val_data)
    _, predicted = torch.max(outputs, dim=1)

    # 计算准确率
    correct = (predicted == val_labels).sum().item()
    total = len(val_labels)
    accuracy = correct / total

    # 计算召回率和F1得分
    recall = recall_score(val_labels, predicted, average='macro')
    f1 = f1_score(val_labels, predicted, average='macro')
    precision = precision_score(val_labels, predicted, average='macro', zero_division=1)


    print(f'Validation Accuracy: {accuracy}')
    print(f'Validation Recall: {recall}')
    print(f'Validation F1 Score: {f1}')
    print(f'Validation Precision: {precision}')

sys.stdout = sys.__stdout__