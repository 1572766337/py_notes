#coding=utf8

#测试paramiko

import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.136.128', 22, username='root', password='pass', timeout=4)
stdin, stdout, stderr = client.exec_command('ls /')
for std in stdout.readlines():
	print std,
client.close()
