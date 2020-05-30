# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba

# 不引入第三方包的
def connectJava(arges,param):
    print(arges)
    print(param)
    print("ok")

# def createWordCloud():
#     print("")
#     txtFilePath = "E:/GitHubProjects/algorithmic-engineering-python-v1/data\python_java_socket_web/wordCloud/DLRB.txt"
#     jpgFilePath = "E:/GitHubProjects/algorithmic-engineering-python-v1/data\python_java_socket_web/wordCloud/xin.jpg"
#     with open(txtFilePath) as fp:
#         text = fp.read()
#         # print(text)
#         # 将读取的中文文档进行分词
#         text = trans_CN(text)
#         mask = np.array(image.open(jpgFilePath))
#         wordcloud = WordCloud(
#             # 添加遮罩层
#             mask=mask,
#             # 生成中文字的字体,必须要加,不然看不到中文
#             font_path="C:\Windows\Fonts\STXINGKA.TTF"
#         ).generate(text)
#         image_produce = wordcloud.to_image()
#         image_produce.show()


# 分词
# def trans_CN(text):
#     # 接收分词的字符串
#     word_list = jieba.cut(text)
#     # 分词后在单独个体之间加上空格
#     result = " ".join(word_list)
#     return result



if __name__ == '__main__':
    arges = "python"
    param = "de"
    #connectJava(arges,param)
    #createWordCloud()