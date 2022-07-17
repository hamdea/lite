import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	print('your mobile is 32 bit :)')
elif 'aarch' in arc:
	__import__("lite").login()
else:
	__import__("litexx").login()
