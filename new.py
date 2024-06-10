from xpinyin import Pinyin

ch = input("输入汉字：")
en = Pinyin().get_pinyin(ch, '')  # 拼音结果连在一起
print("拼音为:{}".format(en))
