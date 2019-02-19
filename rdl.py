#!/usr/bin/env python
import subprocess
import os
import sys
import getpass
import shlex

gp_version = os.path.expandvars('$CURR_MAP')
path='/dvlp/src_'+gp_version+'/gpsrc/rdl/'

def getusername():
	username= getpass.getuser()
	return ('/home/'+username+'/rdlinfo/')

def makedir(option):
	user=getusername()
	if (option == 1):
		return None
	else:
		try:
			if (os.path.exists(user)):
				makedir(1)
			else:
				os.system('mkdir '+ user)
		except:
			print("Unable to create directory")

if len(sys.argv)==1:
	print('Usage:')
	print('     rinfo  <RDL file_name>')
	sys.exit(1)

if(sys.argv[1].endswith('.rdl')):
	file_name = sys.argv[1]
else:
	file_name = sys.argv[1] + '.rdl'

files = os.listdir(path)
res=filter(lambda x: x.endswith('.rdl'),files)

flag = False
corr_file = None
for file in res:
	if (file == file_name):
		makedir(2)
		flag = True
		corr_file = file
		break

if flag == True:
	os.chdir(getusername())
	p1,p2=corr_file.split('.')
	str1='/dvlp/src_'+gp_version+'/gpsrc/src/com/gp_rdl ' +p1+' -t='+p1+' -b=no'
	subprocess.call(shlex.split(str1))
	os.system('vim ' + p1)
else:
	print("Specified file is not an rdl please try again....")
