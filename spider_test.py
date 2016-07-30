#coding:utf8

'''
说明：简易爬虫，爬取了一个python教学的网站
	使用系统库，SGMLParser也是很强大的
	只能在命令行里运行，windows下双击不会生成文件夹
'''

import urllib

from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []
    def start_a(self,attrs):
        href = [v for k,v in attrs if k=='href' or k=='src']
        if href:
            self.urls.extend(href)

url = r'http://www.ziqiangxuetang.com/python3/python3-tutorial.html'
sock = urllib.urlopen(url)
htmlSource = sock.read()
sock.close()

f = file('python3/python3-tutorial.html','w')
f.write(htmlSource)
f.close()

mypath = r'http://www.ziqiangxuetang.com'

parser = URLLister()
parser.feed(htmlSource)

for url in parser.urls:
    if url.startswith('/') and url.endswith('.html'):
        myurl = mypath + url
        print 'get:' + myurl
        sock = urllib.urlopen(myurl)
        htmlSource = sock.read()
        sock.close()

        url = url.split('/').pop()
        print u"save as：" + url
        f = file('python3/'+url,'w')
        f.write(htmlSource)
        f.close()
