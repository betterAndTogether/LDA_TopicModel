#coding=utf-8

import Tools

#对于字符串context 进行预处理 和 分词
def split_word(filename,save_file):
    '''
    :param filename: 文本数据文件，对每一行文基本进行分词
    :param save_file : 分词后保存的路径
    :return: None
    '''

    #read file
    with open(save_file,'w',encoding='utf-8') as wf:
        with open(filename,'r',encoding='utf-8') as f:

            line = f.readline().strip()

            while line:

                #分词
                splited_words = Tools.sentence_split(line)
                splited_sen = ' '.join(splited_words)
                wf.write(splited_sen+"\n")
                line = f.readline()

        f.close()
    wf.close()

if __name__ == "__main__":

    split_word("./data/processed_data/title.txt","./data/processed_data/title_splited.txt")
