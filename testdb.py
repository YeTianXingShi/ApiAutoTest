#!/usr/bin/python3

import pymysql

# 打开数据库连接
connection = pymysql.connect(host='10.251.77.27', port=3306, user='ceshi_admin', password='N7fNO98CNOiBu9gb@Wi9',
                             database='yh_test_tool', cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
sql = "INSERT INTO `users` (`email`, `password`) VALUES ('webmaster@python.org', 'very-secret')"
cursor.execute(sql)
connection.commit()

sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
cursor.execute(sql, ('webmaster@python.org',))
result = cursor.fetchone()
print(result)

try:
    # 执行SQL语句
    sql = "INSERT INTO `users` (`email`, `password`) VALUES ('webmaster@python.org', 'very-secret')"
    cursor.execute(sql)
    # 提交到数据库执行
    connection.commit()
except:
    # 发生错误时回滚
    connection.rollback()
