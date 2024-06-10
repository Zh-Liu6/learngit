from xpinyin import Pinyin

def chinese2english():
    ch = input("输入汉字：")
    en = Pinyin().get_pinyin(ch, '')  # 拼音结果连在一起
    print("拼音为:{}".format(en))

if __name__ == '__main__':

    while True:
        chinese2english()


# 解决Pyinstaller打包xpinyin报错找不到mandarin.dat
# 使用pyinstaller把程序打包成exe，打包后运行报错找不到mandarin.dat文件。这个文件是受xpinyin库调用的，搜索解决办法找到两种办法，
# 一是把xpinyin的文件修改到mypinyin.py，并在使用xpinyin的程序中将xpinyin改成写mypinyin，二是修改源代码。
# 1.首先找到xpinyin所在的文件夹，我的是在D:\Anaconda3\Lib\site-packages\xpinyin，通过在cmd内输入pip show package xpinyin查看得知。
# 2.进入文件夹，把Mandarin.dat复制出来保存在桌面，再找到__init__.py文件，打开，里面有一句这样的代码，用于获取mandarin.dat文件：
# data_path = Path(__file__).resolve().with_name('Mandarin.dat')
# 在这行代码下一行加入如下代码：
# if not Path.is_file(data_path):
#     data_path = Path('.').resolve().with_name('Mandarin.dat')
# 保存修改。代码含义是当上一行在xpinyin文件夹内找不到Mandarin.dat时，在当前程序所在文件夹内寻找。
# 3.运行pyinstaller -F打包要打包的程序。打包完成后，将之前从xpinyin文件夹内复制出来的Mandarin.dat，
# 放到打包后的程序文件夹内、dist文件夹外，此时再运行exe文件不再报错。