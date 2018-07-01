import sys
import opt

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
