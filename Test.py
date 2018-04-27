#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector
import time
try:
    config={
        'host': '',
        'port': 3306,
        'user': 'bjtest',
        'password': 'abcd1234qaz',
        'database': 'pdc',
        'charset': 'utf8'
    }
    con=mysql.connector.connect(**config)
    print (con.connection_id)
    time.sleep(5)
    cursor = con.cursor()
    querytemp=(" SELECT * FROM task WHERE keyword2='2001111427'")
    cursor.execute(querytemp)
    # 取出字段名称集合
    columns = cursor.column_names
    # 取出全部数据
    result = cursor.fetchall()
    print ('数据表字段名称：{0}'.format(columns))
    print ('查询结果如下：')
    i=0
    while i<len(result):
        print(result[i])
        i+=1
    print(con)
    #断开
    con.close()
except mysql.connector.Error as e:
    print (e.message)
print("done")