#encoding:utf-8
import logging
import threading
from datetime import datetime
import  os
class Log:
    def __init__(self):
        global proDir,resultPath
        resultPath = os.path.join(proDir,'result')
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath,str(datetime.now().strftime('%Y%M%D%H%S%M')))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
class myLog:
    log = None
    def get_log(self):
        #creat lock
        self.mutex = threading.Lock()
        #线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。互斥锁为资源引入一个状态：锁定/非锁定。
        # 某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，
        # 将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，
        # 从而保证了多线程情况下数据的正确性。
        #acquire lock
        self.mutex.acquire()
        self.mutex.release()
        return myLog.Log
