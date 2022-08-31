person = {'name': 'lenged', 'age': 23, 'sex': '男'}
print(person['name'])
# 获取不存在的值会报错
# print(person['name1'])

# 查询字典
print(person.get('name'))
# 获取不存在的值不会报错
print(person.get('name1'))
# 修改字典
person['name'] = '张三'
# 添加字典
son = {'name': '李四', 'age': 12}
# 如果key存在则覆盖，不存在则为添加
person['son'] = son
person['son']['sex'] = '女'
print(person)
# 删除 指定key
del person['age']
print(person)
# 删除二级key
del person['son']['age']
print(person)
# 删除整个字典
# del person
# print(person)
# 清空字典
# person.clear()
# print(person)

# 遍历字典
# 遍历字典的key
for key in person.keys():
    print(key)
for kv in person:
    print(kv)
# 遍历字典的value
for value in person.values():
    print(value)
# 遍历字典的key 和value
for k, v in person.items():
    print(k, v)
# 遍历字典的项
for item in person.items():
    print(item)
