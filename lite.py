import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	print('l')
elif 'aarch' in arc:
	__import__("lite").login()
else:
	__import__("lite").login()
