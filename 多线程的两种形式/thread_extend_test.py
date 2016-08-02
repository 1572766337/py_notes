#encoding=UTF-8
#description:
'''
Created on 2015年10月29日

@author: Admin-陕晨阳
'''
import time
import threading

lock = threading.Lock()

class my_thread(threading.Thread):
	def __init__(self,threadname):
		threading.Thread.__init__(self,name=threadname)
	def run(self):
		for i in range(10):
			lock.acquire()
			print self.name,i
			lock.release()
			time.sleep(1)
		
my_thread('thread-1').start()
my_thread('thread-2').start()