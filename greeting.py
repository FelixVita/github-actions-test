print('start')
import getpass
import platform

username = getpass.getuser()
hostname = platform.node()

if username.startswith('runners'):
    print('a' + 1)
else:
    print('a' + str(1))

print('finish')
