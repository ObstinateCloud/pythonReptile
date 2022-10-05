# 元组的元素是不可以修改的
tuple_a = ('a', 'b', 'c')
print(tuple_a[0])
# 元组元素不可修改
# tuple_a[0] = 'aa'
# print(tuple_a)

# 当元组中只有一个元素是他是整型
tuple_b = (5)
print(type(tuple_b))

# 如果想变成tuple类型需要加逗号
tuple_b = (5,)
print(type(tuple_b))
