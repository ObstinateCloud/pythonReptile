# 创建文件 访问模式：w可读可写 r 可读 a 追加模式
# open("lengedtest.txt", "w")

# 写文件文件
# file = open("lengedtest.txt", "w")
# file.write('hello world!\n'*10)
# # 使用完成后要关闭
# file.close()

# 读文件 必须使用r
# fp = open('lengedtest.txt', 'r')
# content = fp.readline()
# print(content)
# print(fp.readlines())
# fp.close()

# name_list = ['张三', '李思思','lisa']
# fp = open('test.txt', 'w')
import json
# 序列化 方式1

# nameStr = json.dumps(name_list)
# fp.write(nameStr)


# 序列化 方式2 dump 一步写入
# json.dump(name_list,fp)
# fp.close()


# 反序列化
fpr = open('test.txt','r')
# content = fpr.read()
# nameList = json.loads(content)
# print(nameList)

# 方式2
print(json.load(fpr))

fpr.close()