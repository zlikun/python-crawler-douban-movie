# Python 词云库测试
# https://amueller.github.io/word_cloud/index.html
# https://amueller.github.io/word_cloud/auto_examples/simple.html#sphx-glr-auto-examples-simple-py
import jieba as jieba
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot

# 读取文本文件
# text = open('./__word_cloud.py', 'r', encoding='utf-8').read()
# __file__ 表示当前文件
text = open(__file__, 'r', encoding='utf-8').read()

# 使用 jieba 分词
# 添加自定义分词
[jieba.add_word(k) for k in ['文本', '文件']]

# 对文本进行分词处理
seg_list = jieba.cut(text)
new_text = ' '.join(seg_list)

# 生成词云，需要指定支持中文的字体，否则无法生成中文词云
wc = WordCloud(
    # 设置词云图片背景色，默认黑色
    # background_color='white',
    # 设置词云最大单词数
    max_words=200,
    # 设置词云中字号最大值
    # max_font_size=80,
    # 设置词云图片宽、高
    width=1024,
    height=768,
    # 设置词云文字字体(美化和解决中文乱码问题)
    font_path=r'./fonts/FZXingKai-S04S.TTF'
).generate(new_text)

# 绘图(标准长方形图)
pyplot.imshow(wc, interpolation='bilinear')
# pyplot.figure()
pyplot.axis('off')
# 直接打印图片
# pyplot.show()
# 将图片输出到文件
wc.to_file(r'./images/__wc_1.png')

# 基于图像着色
background_image = pyplot.imread(r'./images/__background.jpg')
wc = WordCloud(
    font_path=r'./fonts/FZXingKai-S04S.TTF',
    mask=background_image,
    # random_state=32,
    # max_font_size=64,
    width=1000,
    height=833
).generate(new_text)
# 从背景图片生成颜色值
pyplot.imshow(wc.recolor(color_func=ImageColorGenerator(background_image)))
pyplot.axis('off')
# 绘制背景图片为底色的图片
pyplot.figure()
pyplot.imshow(background_image, cmap=pyplot.cm.gray)
pyplot.axis('off')
# pyplot.show()
wc.to_file(r'./images/__wc_2.png')
