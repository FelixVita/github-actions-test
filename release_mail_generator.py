import sys

print("argument {}".format(sys.argv[1]))
print("changelog 1")
print("changelog 2")
print("changelog 3")
print("howdy doody")
x = 3
print(f"awesome {str(x)}")

import getpass
import platform
username = getpass.getuser()
hostname = platform.node()
print(f"Hello there, {username}@{hostname}")
if username.startswith("runner"):
    print("HEY RUNNER!")