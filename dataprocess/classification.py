# utf-8
import sys

import jieba
import kashgari
from collections import Counter
from textrank4zh import TextRank4Keyword, TextRank4Sentence


# 获取停用词
def getDirtyWord():
    ans = []
    file = '/Users/roarboil/Desktop/news-python/dataprocess/word.txt'
    f = open(file, 'r')
    ff = f.readlines()
    for line in ff:
        line = line.rstrip("\n")
        ans.append(line)
    return ans


def process(content):
    res = list(jieba.cut(content))
    dirty = []
    for c in res:
        if c in wordList:
            dirty.append(c)
    for i in dirty:
        if i in res:
            res.remove(i)
    return res


if __name__ == '__main__':
    wordList = getDirtyWord()
    # content = sys.argv[1]
    content = """
    2020十大科技趋势具体包括，人工智能从感知智能向认知智能演进、计算存储一体化突破AI算力瓶颈、工业互联网的超融合、机器间大规模协作成为可能、模块化降低芯片设计门槛、规模化生产级区块链应用将走入大众、量子计算进入攻坚期、新材料推动半导体器件革新、保护数据隐私的AI技术将加速落地、云成为IT技术创新的中心。
     """

    new_model = kashgari.utils.load_model('/Users/roarboil/Desktop/news-python/dataprocess/model')
    x = process(content)
    label = new_model.predict([x], batch_size=64)
    ans = Counter(label).most_common(4)
    print(ans[0][0])
