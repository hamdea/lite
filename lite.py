import platform,os
os.system('git pull')
os.system('clear')


arc = str(platform.uname().machine)
if 'arm' in arc:
	print('your mobile is 32 bit :)')
elif 'aarch' in arc:
	__import__("lite").login()
else:
	__import__("litexx").login()
