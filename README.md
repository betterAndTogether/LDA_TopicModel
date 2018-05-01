#
    使用LDA进驻主题分布分析
#


#
    py文件解析
#
    #   Tools.py

        ##  共有三个功能工具:
                1.Extract file titles   2. Extract file content     3.split word[分词]

    #   pre_process_data.py

        ##  对文本数据进行预处理


    #   LDA_model.py

        ##  使用gensim包，调用LDA模型接口。

#
    运行流程 pineline
#

    1.数据准备
        格式：将数据存放在./data/init_data/2016[2017,2018]/文件夹中，每个文件夹存放多个txt文件，每个txt文件
            相当于一个贴

    2.运行 Tool.py 文件，进而将原始文件，转化为 context.txt 文件。  【一行代表一个贴的文本数据】
        生成文件：
            ./data/processed_data/content.txt
        For example:
                #demo for extract content
                data_dir = "./data/init_data/"
                file_path_arr = Get_File_Name(data_dir)
                save_path = "./data/processed_data/content.txt"
                ExtractContent(file_path_arr,save_path)

    3.运行LDA_model.py文件，生成 ./result/topic.txt [若context_split.txt不存在，会对context.txt数据进行预处理，并生成context_split.txt]

        [若更新了context.txt文本数据文件，需要手动将context_split.txt文件先删除]

        For example:
                save_file = "./result/topic.txt"
                lda_main(save_file)

                生成的topic.txt文件样例：

                第0个主题:
                   "宿舍"  : ( 0.009)   "团子"  : ( 0.008)   "想"  : ( 0.007)   "说"  : ( 0.007)   "楼主"  : ( 0.006)
                第1个主题:
                   "工作"  : (0.013)   "学生"  : ( 0.008)   "时间"  : ( 0.007)   "中山大学"  : ( 0.006)   "月"  : ( 0.005) 
                第2个主题:
                   "自考"  : (0.083)   "广州中山大学"  : ( 0.048)   "年"  : ( 0.036)   "中山大学"  : ( 0.018)  
                第3个主题:
                    ......

    4.运行TextClassification.py，根据第3步保存的lda model，对新来的文档输出其主题分布概率

        需要调用LDA_model.py中接口，get_topic(splited_doc): 输入: 文档的分词数组  输出: 该文档概率最大的主题

        【此文件结合本项目需求，需将所有文档根据主题进行分类】

    5.运行sentiment_match.py

        此py文件，直接使用外部情感词典，从而判断文本的情感方向。二分情感分类：【消极/积极】







