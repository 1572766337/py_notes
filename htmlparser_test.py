#coding=utf8

'''
没错，就是htmlparser的简单用法
'''

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('starttag:<%s>' % tag)

    def handle_endtag(self, tag):
        print('endtag:</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('startendtag:<%s/>' % tag)

    def handle_data(self, data):
        print('data:'+data)

    def handle_comment(self, data):
        print('<!--'+data+'-->')

    def handle_entityref(self, name):
        print('entityref:&%s;' % name)

    def handle_charref(self, name):
        print('charref:&#%s;' % name)

parser = MyHTMLParser()
htmlstr = u'<html><head><br/></head><body><!-- 注释 -->&nbsp;<p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>'
print 'htmlsrc:'+htmlstr
parser.feed(htmlstr)
