#coding=utf8

'''
多线程，加锁，装饰器综合使用案例
'''

from time import ctime,sleep
import threading

mylock = threading.Lock()

def lock(func):
    def wrapper(*args,**kw):
        mylock.acquire()
        func(*args,**kw)
        mylock.release()
    return wrapper

def music(func):
    for i in range(10):
        music1(func)
        sleep(1)

@lock
def music1(func):
    print "I am listening to %s. %s" %(func,ctime())

def movie(func):
    for i in range(10):
        movie1(func)
        sleep(2)

@lock
def movie1(func):
    print "I am watching a %s. %s" % (func,ctime())
    
def player(name):
    r=name.split('.')[1]
    if r=='mp3':
        music(name)
    else:
        if r=='mp4':
            movie(name)
        else:
            print 'Format Error'

list=['music.mp3','movie.mp4']

threads = []
filelist=range(len(list))

for i in filelist:
    t=threading.Thread(target=player,args=(list[i],))
    threads.append(t)

if __name__ == "__main__":
    for i in filelist:
        threads[i].start()
    for i in filelist:
        threads[i].join()
    print "all over %s" %ctime()
    
