import os

DICT_URL = './data/static_data/hownet_sentiment_dict.txt'
positive_list = list()
negtive_list = list()


def main():

    file_path = ["./result/job.txt","./result/kaoshi.txt","./result/kaoyan.txt","./result/life.txt","./result/new_student.txt","./result/pe.txt"
                 ,"./result/profession.txt"]

    positive_arr = []
    negative_arr = []

    with open("./data/static_data/hownet_sentiment_dict.txt",'r',encoding='utf-8') as f:

        line = f.readline().strip()

        while line:

            line_arr = line.split(",")

            if int(line_arr[1]) == 1:
                positive_arr.append(line_arr[0])
            else:
                negative_arr.append(line_arr[0])

            line = f.readline().strip()

    f.close()

    for file_name in file_path:

        positive_count = 0
        negtive_count = 0

        with open(file_name,'r',encoding='utf-8') as f:

            line = f.readline().strip()

            while line:

                line_arr = line.split()

                for word in line_arr:

                    if word in positive_arr:

                        positive_count += 1

                    if word in negative_arr:

                        negtive_count += 1


                line = f.readline().strip()


            print(file_name)
            print("positive_count: {}".format(positive_count))
            print("negative_count: {}".format(negtive_count))



if __name__ == '__main__':
    main()