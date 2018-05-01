#coding=utf-8

import Tools
import os

from gensim import corpora,models
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

    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=20)

    #模型保存
    lda.save('./model_save/baidu_tieba.model')

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

    #模型保存
    lda.save('./model_save/baidu_tieba.model')

#根据新的文档，得到文档的主题分布，然后对根据主题，对文档进行分类
def get_topic(splited_doc):

    lda = models.LdaModel.load('./model_save/baidu_tieba.model')
    dictionary = lda.id2word
    #对新来的文档进行分词


    doc_bow = dictionary.doc2bow(splited_doc)
    doc_lda = lda[doc_bow]  # 得到新文档的主题分布
    # 输出新文档的主题分布
    # print(doc_lda)
    # for topic in doc_lda:
    #     print("%s\t%f\n" % (lda.print_topic(topic[0]), topic[1]))
    max_pro = 0
    max_topic = 0
    for topic in doc_lda:
        if topic[1] > max_pro:
            max_pro = topic[1]
            max_topic = topic[0]

    # print(int(max_topic))
    return int(max_topic)


def lda_model_test():

    train_file = "./data/processed_data/content.txt"
    save_file = "./data/processed_data/content_split.txt"

    # 第一次运行时
    train = constract_train(train_file, save_file)

    dictionary = corpora.Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]


    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=20)

    lda.save('./model_save/baidu_tieba.model')

    #lda输出说明s



if __name__ == "__main__":

    save_file = "./result/topic.txt"
    lda_main(save_file)

    # lda_model_test()

    # get_topic("地矿局肯德基奉公克己地方")























