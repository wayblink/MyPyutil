
#coding: utf-8

import time 

class Log(object):
  path = ""

  def __init__(self,path):
    self.path = path

  def write(self, message):
    log_file = open(self.path,"a")
    log_file.write("\n" + message)
    log_file.close()

  def logInfo(self, message):
    message = get_time + "INFO: " + message
    write(message = message)

  def logError(self, message):
    message = get_time + "ERROR: " + message
    write(message = message)

  def logDebug(self, message):
    message = get_time + "DEBUG: " + message
    write(message = message)
    
  def get_time():
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return time_str
