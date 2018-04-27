"""
将Data/zhihu_HotTopics目录下的每一篇文章分词，并分别存放到Data/zhihu_HotTopics_fenci目录下
"""
import os
import jieba
import platform

sys_info = platform.system()  # 操作系统信息
root_dir = os.getcwd()
data_dir = os.path.join(root_dir, "Data")

# dict_file = os.path.join(data_dir, "user_dict.txt")
# jieba.load_userdict(dict_file)

# 判断字符串是否由数字.%以及英文字母组成
def isNumeric(s):
    """return True if string s is numeric"""
    return all([c in "0123456789.%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                for c in s])


# 返回停用词列表
def get_stopwords():
    stopwords = []
    stop_file = os.path.join(data_dir, "stop_word.txt")
    with open(stop_file, 'rb+') as fin:
        for line in fin:
            if line.strip():
                stopwords.append(line.strip())
    return stopwords


# 单个文件分词
# inFile, outFile为完整路径(unicode)
def fenci_file(inFile, outFile):
    stopwords = get_stopwords()
    all_words = []

    with open(inFile, 'rb+') as fin:
        for line in fin:
            if line.strip():
                line = line.strip().decode("utf-8")
                words = list(jieba.cut(line, cut_all=False))
                if words:
                    all_words.extend(words)

    # 筛词, 筛去长度为1的词,停用词,纯数字和纯英文
    all_words = [word for word in all_words if len(word) > 1]
    all_words = [word for word in all_words
                 if not isNumeric(word) and word not in stopwords]

    with open(outFile, "wb+") as fout:
        fout.write(" ".join(all_words).encode('utf-8', 'ignore'))


# inDir目录下每个文件分词, 存到outDir目录下
def fenci_dir(inDir, outDir):
    inDir = os.path.join(data_dir, inDir)
    outDir = os.path.join(data_dir, outDir)
    # 创建outDir目录
    if not os.path.exists(outDir):
        os.mkdir(outDir)

    for fn in os.listdir(inDir):
        inFile = os.path.join(inDir, fn)
        outFile = os.path.join(outDir, fn)

        fenci_file(inFile, outFile)


fenci_dir(inDir="zhihu_HotTopics", outDir="zhihu_HotTopics_fenci")
