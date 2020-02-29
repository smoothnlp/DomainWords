import os
from smoothnlp.algorithm.phrase import extract_phrase
import pandas as pd


news_path = 'DomainPhrase_Fudan/'
file_path1, file_path2 = 'Corpus_Fudan/test/', 'Corpus_Fudan/train/'


def read_data(file_name):
    '''read txt file'''
    with open(file_name, 'r') as f:
        words = f.readlines()
        words = [x.split('\n')[0] for x in words if len(x) > 1]
    return words


def eachFile(filepath):
    '''get all files in file path'''
    pathDir = [file for file in os.listdir(filepath) if not file.startswith('.')]  ## 忽略隐藏文件
    all_files = []
    for allDir in pathDir:
        all_files.append(os.path.join('%s%s' % (filepath, allDir)))
    return all_files


def is_chinese(uchar):
    """判断一个unicode是否包含汉字"""
    # 汉字\u4e00-\u9fa5，数字\u0030-\u0039，英文\u0041-\u005a\u0061-\u007a
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def get_file(file):
    """删除common words"""
    words = read_data(file)
    f = open(file,'w')
    for i in words:
        if i not in common_words:
            f.write(i+'\n')
    f.close()


domain_folder = eachFile(file_path1)
domain_folder = [x.split('test/')[1]+'/' for x in domain_folder]

num_file = []
num_char = []
domain_file = []
for folder in domain_folder:
    files = eachFile(file_path1 + folder) + eachFile(file_path2 + folder)
    num_file.append(len(files))
    corpus = ''
    #遍历同一domain folder下所有txt
    for txt in files:
        lines = open(txt, 'r', encoding='utf-8').readlines()
        corpus += ''.join([x.split('\n')[0] for x in lines if not '【' in x])
    num_char.append(len(corpus))
    top_k = extract_phrase(corpus,5000,max_n=5)
    file_name = news_path + folder[:-1] + '.txt'
    domain_file.append(file_name)
    f = open(file_name,'w')
    for i in top_k:
        if is_chinese(i):
            f.write(i+'\n')
    f.close()

df = pd.DataFrame({'domain':domain_file,'num_file':num_file,'num_char':num_char})\
                  .sort_values('num_char',ascending=False)
top_domain = df['domain'].values[:5]
common_words = set(read_data(top_domain[0]))
for domain in top_domain[1:]:
    common_words &= set(read_data(domain))

for file in eachFile(news_path):
    get_file(file)