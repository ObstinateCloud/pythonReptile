# 安装 jsonpath pip install jsonpath
import jsonpath
import json

# 获取json对象
obj = json.load(open('jsonpath本地测试文件.json','r',encoding='utf-8'))

'''
 .. 代表所有下级 .直接下级 $ 根节点 * 代表所有
'''



# 查询A,下所有的城市名称
# A_city_list = jsonpath.jsonpath(obj,'$.returnValue.A[*].regionName')
# A_city_list = jsonpath.jsonpath(obj,'$.returnValue.A[1].regionName')
# A_city_list = jsonpath.jsonpath(obj,'$.returnValue.A..regionName')
# print(A_city_list)

# 查询所有的城市名称
# city_list = jsonpath.jsonpath(obj,'$..regionName')
# print(len(city_list))

# returnValue_list = jsonpath.jsonpath(obj,'$.*')
# 查询returnValue所有的元素
# returnValue_list = jsonpath.jsonpath(obj,'$.returnValue.*')
# print(len(returnValue_list))

# 查询returnValue.A最后一组对象
# A_last_city = jsonpath.jsonpath(obj,'$.returnValue.A[(@.length-1)]')
# A_last_city = jsonpath.jsonpath(obj,'$.returnValue..[(@.length-1)]')
# print(A_last_city)

# 查询returnValue.A最后前两组对象
# A_last_city = jsonpath.jsonpath(obj,'$.returnValue.A[0,1]')
# A_last_city = jsonpath.jsonpath(obj,'$.returnValue.A[:2]')
# print(A_last_city)

# 条件查询 加?
# 查询returnValue所有包含key cityName的城市
# city_name_list = jsonpath.jsonpath(obj,'$.returnValue..[?(@.cityName)]')
# print(city_name_list)

# 查询id大于1000的城市
# big_1000_list = jsonpath.jsonpath(obj,'$.returnValue..[?(@.id>1000)]')
# print(len(big_1000_list))

# 正则表达式查询所有包含阳的城市
# yang_city_list = jsonpath.jsonpath(obj,'$.returnValue..regionName')
# yang_city_list = jsonpath.jsonpath(obj,'$.like[?(@.name in ["张三","tom"])]')
# yang_city_list = jsonpath.jsonpath(obj,'$.like[?(@.name =~ /tom)]')
yang_city_list = jsonpath.jsonpath(obj,'$.like[?(/"张三"/.test(@.name))]')
print(yang_city_list)