import getpass
import platform

username = getpass.getuser()
hostname = platform.node()

print(f"Hello there, {username}@{hostname}")

if username.startswith("runner"):
    print("HEY RUNNER!")

import pi