# Python 中文分词模块
# https://github.com/fxsjy/jieba
# https://pypi.org/project/jieba/

import jieba


def print_iterator(_iter):
    print('/'.join(_iter))


# 全模式
# 我/来到/北京/清华/清华大学/华大/大学
print_iterator(jieba.cut("我来到北京清华大学", cut_all=True))

# 精确模式
# 我/来到/北京/清华大学
print_iterator(jieba.cut("我来到北京清华大学", cut_all=False))

# 默认是精确模式
# 他/来到/了/网易/杭研/大厦
print_iterator(jieba.cut("他来到了网易杭研大厦"))

# 搜索引擎模式
# 小明/硕士/毕业/于/中国/科学/学院/科学院/中国科学院/计算/计算所/，/后/在/日本/京都/大学/日本京都大学/深造
print_iterator(jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造"))

# 自定义词典：一个词占一行，每行分三列，词语、词频(可省略)、词性(可省略)，使用空格分隔，文件使用UTF-8编码
# jieba.load_userdict(r'./dicts/my_dict.txt')


# 载入自定义字典前
# 她/是/市/创新/办/主任/，/也/是/云/计算/方面/的/专家
print_iterator(jieba.cut('她是市创新办主任，也是云计算方面的专家'))

# 载入自定义字典
jieba.load_userdict(r'./dicts/my_dict.txt')

# 载入自定义字典后
# 她/是/市/创新办/主任/，/也是/云计算/方面/的/专家
print_iterator(jieba.cut('她是市创新办主任，也是云计算方面的专家'))

# 调整词典

# 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典
jieba.add_word('市创新办')
# 她/是/市创新办/主任/，/也是/云计算/方面/的/专家
print_iterator(jieba.cut('她是市创新办主任，也是云计算方面的专家'))
jieba.del_word('也是')
# 她/是/市创新办/主任/，/也/是/云计算/方面/的/专家
print_iterator(jieba.cut('她是市创新办主任，也是云计算方面的专家'))

# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来
# 如果/放到/post/中将/出错/。
print_iterator(jieba.cut('如果放到post中将出错。', HMM=False))
# 494
print(jieba.suggest_freq(('中', '将'), True))
# 如果/放到/post/中/将/出错/。
print_iterator(jieba.cut('如果放到post中将出错。', HMM=False))
