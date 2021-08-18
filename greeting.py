print('start')
import getpass
import platform

username = getpass.getuser()
hostname = platform.node()

if username.startswith('runner'):
    print('a' + 1)
else:
    print('a' + str(1))

print('finish')
