
#coding: utf-8

import pymysql.cursors

#连接配置信息
config = {
          'host':'10.8.52.95',
          'port':3336,
          'user':'user_name',
          'passwd':'{passwd}',
          'db':'{db_name}',
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }

def query(sql):
    # 创建连接
    connection = pymysql.connect(**config)
    cur = connection.cursor()
    #执行sql
    cur.execute(sql)
    rows = cur.fetchall()
    #关闭连接
    cur.close()
    connection.close()
    #获取结果
    return rows
