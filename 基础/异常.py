try:
    fp = open('aa.txt','r')
    fp.read()
except FileNotFoundError:
    print('文件找不到了..')