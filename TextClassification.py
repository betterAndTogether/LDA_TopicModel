#coding=utf-8

import LDA_model





#根据LDA进行分类
def text_classification(content_file):


    count_profession = 0
    kaoshi = 0
    count_life = 0
    job = 0
    kaoyan = 0
    new_student = 0
    pe = 0


    sum_count = 0

    txt_count_profession = []
    txt_kaoshi = []
    txt_count_life = []
    txt_job = []
    txt_kaoyan = []
    txt_new_student = []
    txt_pe = []

    # splited_doc = list(Tools.sentence_split(doc))

    with open(content_file,'r',encoding='utf-8') as f:


        line = f.readline().strip()

        while line:

            sum_count += 1
            print(sum_count)
            context = list(line.split())
            # print(context)

            topic = LDA_model.get_topic(context)

            # print(topic)
            # print(type(topic))
            # exit()

            if topic == 0:
                count_life+=1
                txt_count_life.append(line)


            elif topic == 1:
                job += 1
                txt_job.append(line)

            elif topic == [3,7]:
                kaoshi += 1
                txt_kaoshi.append(line)

            elif topic in [2,4,5]:
                kaoyan+=1
                txt_kaoyan.append(line)

            elif topic == 8:
                count_profession+=1
                txt_count_profession.append(line)

            line = f.readline().strip()


        #写入文件
        with open("./result/profession.txt",'w',encoding='utf-8') as wf:

            for line in txt_count_profession:
                wf.write(line+"\n")
        wf.close()

        with open("./result/life.txt", 'w', encoding='utf-8') as wf:

            for line in txt_count_life:
                wf.write(line + "\n")
        wf.close()

        with open("./result/job.txt", 'w', encoding='utf-8') as wf:

            for line in txt_job:
                wf.write(line + "\n")
        wf.close()

        with open("./result/kaoyan.txt", 'w', encoding='utf-8') as wf:

            for line in txt_kaoyan:
                wf.write(line + "\n")
        wf.close()

        with open("./result/new_student.txt", 'w', encoding='utf-8') as wf:

            for line in txt_new_student:
                wf.write(line + "\n")
        wf.close()

        with open("./result/pe.txt", 'w', encoding='utf-8') as wf:

            for line in txt_pe:
                wf.write(line + "\n")
        wf.close()

        with open("./result/kaoshi.txt", 'w', encoding='utf-8') as wf:

            for line in txt_kaoshi:
                wf.write(line + "\n")
        wf.close()

        #统计结果写入文件
        with open("./result/topic_count",'w',encoding='utf-8') as wf:

            wf.write(" job : {}\n".format(str(job)))
            wf.write(" kaoshi : {}\n".format(str(kaoshi)))
            wf.write(" kaoyan : {}\n".format(str(kaoyan)))
            wf.write(" life : {}\n".format(str(count_life)))
            wf.write(" new_student : {}\n".format(str(new_student)))
            wf.write(" pe : {}\n".format(str(pe)))
            wf.write(" profession : {}\n".format(str(count_profession)))

        wf.close()

        print(sum_count)


if __name__ == "__main__":
    content_file = "./data/processed_data/content_split.txt"
    text_classification(content_file)