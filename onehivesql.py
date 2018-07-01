
# coding: utf-8

import sys
import getopt
from pyutil.hiveserver2.client import connect


def onesql(sql,ip,port,username):
  try:
    with connect('hive', host=ip, port=int(port), username=username) as client:
      with client.cursor() as cursor:
        try:
          cursor.execute(sql, configuration={'mapreduce.job.name': 'spark_one_sql_' + username,
                                                   'mapreduce.job.priority': 'NORMAL'})
        except:
          print 'fail to execute sql'
        try:
          print cursor.fetchall()
        except:
          print 'fail to fetch results for sql-%s' % (sql)
  except:
    print "fail"

if __name__ == '__main__':
  print sys.argv
  opts,args = getopt.getopt(sys.argv[1:],'hi:p:s:u:',['help','ip','post','sql','user'])
  ip = "10.10.170.74"
  port = 9231
  username = "wanganyang"
  sql = ""
  for name, value in opts:
    if name in ("-h","--help"):
      print 'python onesql.py -i {ip} -p {port} -s {sql} -u {user}'
      sys.exit()
    if name in ("-i","--ip"):
      ip = value
      print ip
    if name in ("-p","--port"):
      port = value
      print port
    if name in ("-s","--sql"):
      sql = value
      print sql
    if name in ("-u","--user"):
      username = value
      print username
  onesql(ip=ip,port=port,sql=sql,username=username)
