from nltk.corpus import stopwords
import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wnl
import jieba

import sys
sys.path.append('E:/文本分类/text_gcn.pytorch-master/')
from utils.utils import clean_str, loadWord2Vec

# stop_words = set()
#
# with open('E:/stopwords-master/cn_stopwords.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         word = line.strip()  # 去除行末的换行符和空白字符
#         stop_words.add(word)
#
# doc_content_list = []
# #with open('data/wiki_long_abstracts_en_text.txt', 'r') as f:
# with open('E:/文本分类/text_gcn.pytorch-master/data/corpus/R8.txt', 'rb') as f:
#     for line in f.readlines():
#         doc_content_list.append(line.strip().decode('utf-8'))
# #print("doc_contest_list:",doc_content_list)
#
# word_freq = {}
# for doc_content in doc_content_list:
#     temp = clean_str(doc_content)
#     words = jieba.lcut(doc_content)
#     for word in words:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1
# print('words1:',words)
#
# clean_docs = []
# for doc_content in doc_content_list:
#     temp = clean_str(doc_content)
#     words = jieba.lcut(doc_content)
#     doc_words = []
#     for word in words:
#         if word not in stop_words and word_freq[word] >= 5:
#            doc_words.append(word)
# print('doc_words:', doc_words)
#
# doc_str =''.join(doc_words).strip()
# print("doc_str:",doc_str)
#     #if doc_str == '':
#         #doc_str = temp
# clean_docs.append(doc_str)
# clean_corpus_str = '\n'.join(clean_docs)



min_len = 10000
aver_len = 0
max_len = 0

with open('E:/文本分类/text_gcn.pytorch-master/data/corpus/R8.clean.txt', 'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp = line
        aver_len = aver_len + len(temp)
        if len(temp) < min_len:
            min_len = len(temp)
        if len(temp) > max_len:
            max_len = len(temp)

aver_len = 1.0 * aver_len / len(lines)
print('Min_len : ' + str(min_len))
print('Max_len : ' + str(max_len))
print('Average_len : ' + str(aver_len))



