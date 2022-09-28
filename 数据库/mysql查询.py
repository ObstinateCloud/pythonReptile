# 导入pymysql
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     user='root',
                     password='zjy123',
                     database='mytest',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
# data = cursor.fetchall()
# data = cursor.fetchmany(1)
print(data)

print("数据库连接成功！")

# 创建表
sql="""CREATE TABLE test (
          FIRST_  CHAR(20) NOT NULL,
          SECOND_  CHAR(20),
          THIRD_ INT,
          FOURTH_ CHAR(1),
          FIFTH_ FLOAT )"""
# 运行sql语句
# res = cursor.execute(sql)
# print(res)

# insert语句
# try:
#     sql = "insert into test(FIRST_,SECOND_,THIRD_,FOURTH_,FIFTH_) values ('MAC1','MOTH1','20','M','2000')"
#
#     # 运行sql语句
#     res = cursor.execute(sql)
#     print(res)
#     # 修改
#     db.commit()
#     # 关闭游标
#     cursor.close()
#     # 关闭连接
#     # db.close()
#     print("victory!")
# except:
#     print("false")

#  查询语句
# 查询语句
try:
    cursor = db.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(type(data))
        fm_date = '{:%Y-%m-%d %H:%M:%S}'.format(data[len(data)-1])
        print(fm_date)
        print(data)
except Exception:
    print("查询失败")



# 关闭数据库连接
db.close()
print("数据库关闭成功！")
