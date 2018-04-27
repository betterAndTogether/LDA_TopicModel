#coding=utf-8

import os
import jieba

def Get_File_Name(file_dir):
    '''
    :param dir:源文件夹路径
    :return:file_path :所有文件名的路径数组
    '''
    file_path = []
    #跑一层
    first_dir = None
    for root, dirs, files in os.walk(file_dir):
        first_dir = dirs
        break

    #对每个dir在跑一层

    for dir in first_dir:
        for root,dirs,files in os.walk(file_dir+dir+"/"):
            for file in files:
                file_name = str(file_dir)+str(dir)+"/"+str(file)
                file_path.append(file_name)
    return file_path

def ExtractTitle(file_path_arr,save_name):
    '''
    :param file_path_arr: 所有文件相对路径数组
    :param save_name: 保存title的文件
    :return: None
    '''
    with open(save_name,'w',encoding='utf-8') as wf:

        for file_name in file_path_arr:
            with open(file_name,'r',encoding='utf-8') as f:

                #读取第一行 ==》 即title
                line = f.readline().strip()

                #写入文件
                wf.write(line+"\n")

            f.close()

    wf.close()

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

#判断是否为中文
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

#对于字符串只保留汉字
def format_str(content):
    # content = str(content,'utf-8') python2
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str+i
    return content_str


#对于字符串context 进行预处理 和 分词
def sentence_split(context):

    #只保留汉字
    content = format_str(context)

    #结巴分词
    splited_words = list(jieba.cut(content,cut_all=False))
    stopwords = stopwordslist("./data/static_data/stopwords.txt")
    out_words = []
    #去停用词
    for word in splited_words:
        if word not in stopwords:

            out_words.append(word)

    return out_words

if __name__ == "__main__":

#demo for extract titles
    # data_dir = "./data/init_data/"
    # file_path_arr = Get_File_Name(data_dir)
    # save_path = "./data/processed_data/title.txt"
    # ExtractTitle(file_path_arr,save_path)


#demo for split word
    splited_sen = sentence_split("你好，胡安娜发电机房就饿哦积分")
    print(splited_sen)


