# 读取Mongo中短评数据，对其进行中文分词，并生成词云

# 读取Mongo中的短评数据
import pymongo
import jieba
from jieba import analyse

# https://pypi.org/project/pymongo/
# http://github.com/mongodb/mongo-python-driver
from matplotlib import pyplot
from wordcloud import WordCloud

text = None

with pymongo.MongoClient(host='192.168.0.105', port=27017) as client:
    # 获取集合
    comments = client.douban.movie_26752088_comments

    # 不知道为什么爬虫只取到了1000条评论~
    print('count:', comments.estimated_document_count())

    # pymongo.cursor.Cursor
    cursor = comments.find()

    # 遍历数据，这里只遍历短评数据(好在数据量并不太大)
    text = ''.join(map(lambda doc: doc.get('comment'), cursor))

# 对短语数据文本进行分词
# 添加自定义分词
[jieba.add_word(k) for k in []]

# 取Top50的词生成词云
# https://github.com/fxsjy/jieba#基于-tf-idf-算法的关键词抽取
tags = analyse.extract_tags(text, topK=50, withWeight=False)
new_text = ' '.join(tags)
print(new_text)

# 对分词文本生成词云
# 生成词云，需要指定支持中文的字体，否则无法生成中文词云
wc = WordCloud(
    # 设置词云图片背景色，默认黑色
    # background_color='white',
    # 设置词云最大单词数
    max_words=200,
    # 设置词云中字号最大值
    # max_font_size=80,
    # 设置词云图片宽、高
    width=768,
    height=1024,
    # 设置词云文字字体(美化和解决中文乱码问题)
    font_path=r'../example/fonts/FZXingKai-S04S.TTF'
).generate(new_text)

# 绘图(标准长方形图)
pyplot.imshow(wc, interpolation='bilinear')
pyplot.figure()
pyplot.axis('off')
# 将图片输出到文件
wc.to_file(r'./images/wc.png')
