#coding=utf-8

import Tools
import os

from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary

def constract_train(train_file,save_file):
    '''
    构造训练集
    :param train_file: 文档训练数据
    :return:
    '''
    train = []
    #判断文件是否存在
    if os.path.exists(save_file):
        #直接读取

        with open(save_file,'r',encoding='utf-8') as f:

            line = f.readline().strip()

            while line:

                sen = line.split()
                train.append(sen)

                line = f.readline().strip()

        return train

    with open(save_file,'w',encoding='utf-8') as wf:

        with open(train_file,'r',encoding='utf-8') as f:

            line = f.readline().strip()

            while line:

                sen_split = []
                sentences = line.split(",")

                #对每个句子进行分词
                for i in range(len(sentences)):

                    if i == 0 :
                     continue

                    split_word = Tools.sentence_split(sentences[i])
                    sen_split.extend(split_word)

                #写入文件
                wf.write(' '.join(sen_split)+"\n")

                train.append(sen_split)
                # print(train)
                # exit()
                line = f.readline().strip()
        f.close()
    wf.close()

    return train

def lda_main(topic_save_file):

    train_file = "./data/processed_data/content.txt"
    save_file = "./data/processed_data/content_split.txt"

    #第一次运行时
    train = constract_train(train_file,save_file)

    dictionary = corpora.Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]

    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=15, passes=20)

    with open(topic_save_file,'w',encoding='utf-8') as wf:

        for topic in lda.print_topics(num_words=15):

            wf.write("第{}个主题:\n".format(topic[0]))

            termNumber = topic[0]
            print(topic[0], ':', sep='')
            listOfTerms = topic[1].split('+')

            str = ""

            for term in listOfTerms:
                listItems = term.split('*')

                print('  ', listItems[1], '(', listItems[0], ')', sep='')
                wf.write("   {} : ({})".format(listItems[1],listItems[0]))

            wf.write("\n")

        wf.close()

def lda_model_test():

    train_file = "./data/processed_data/content.txt"
    save_file = "./data/processed_data/content_split.txt"

    # 第一次运行时
    train = constract_train(train_file, save_file)

    dictionary = corpora.Dictionary(train)
    print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in train]
    print(corpus)
    exit()

    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=20)

    #lda输出说明


if __name__ == "__main__":

    # save_file = "./result/topic.txt"
    # lda_main(save_file)

    lda_model_test()

























