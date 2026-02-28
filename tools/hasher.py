import hashlib
import os
from colorama import Fore, init
init(autoreset=True)

file = input("Enter file path: ")

if not os.path.isfile(file):
    print("File does not exist!")
else:
    try:
        with open(file, "rb") as f:
            data = f.read()
            print("MD5:", hashlib.md5(data).hexdigest())
            print("SHA256:", hashlib.sha256(data).hexdigest())
    except:
        print("Error reading file")

print(Fore.YELLOW + "Created by Abdullah Ghani")
input("\nPress Enter to return...")
