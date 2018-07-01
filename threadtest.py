
#coding: utf-8

import threading

class aThread(threading.Thread):
    def __init__(self,threadID,arg1,arg2,arg3):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def run(self):
        #do some thing
        print self.arg1 + self.arg2 + self.arg3

if __name__ == '__main__':
    #初始化线程
    thread1 = aThread("thread1" , arg1 = 1, arg2 = 2, arg3 = 3)
    thread2 = aThread("thread2" , arg1 = 4, arg2 = 5, arg3 = 6)
    
    #加入到线程组中，方便管理
    threads = []
    threads.append(thread1)
    threads.append(thread2)
    
    #执行线程
    thread1.start()
    thread2.start()

    #等线程执行完
    for t in threads:
        t.join()
        t.join()

    print "Finished"
