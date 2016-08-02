#coding=utf8

import time
import threading

lock = threading.Lock()

def func():
	for i in range(10):
		lock.acquire()
		print threading.currentThread().name,i
		lock.release()
		time.sleep(1)
		
threading.Thread(target=func,name='thread-1').start()
threading.Thread(target=func,name='thread-2').start()