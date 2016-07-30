#coding=utf8

'''
菜菜初学python时候的笔记，现在看看，不就是函数式编程吗
'''

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print '2013-12-25'

now()
