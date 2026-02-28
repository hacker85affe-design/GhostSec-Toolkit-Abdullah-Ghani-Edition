nano scanner.py
import os
from colorama import Fore, init
init(autoreset=True)

path = input("Enter directory to scan: ")

print(Fore.CYAN + f"\nScanning {path}...\n")

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith((".exe", ".sh", ".bat")):
            print(Fore.RED + "[!] Suspicious File Found:", os.path.join(root, file))

print(Fore.GREEN + "\nScan Completed")
print(Fore.YELLOW + "Created by Abdullah Ghani")
input("Press Enter to return...")

nano hasher.py
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

nano sysinfo.py
import platform
from colorama import Fore, init
init(autoreset=True)

print("\nSystem Information\n")

print("OS:", platform.system())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("Processor:", platform.processor())

print(Fore.YELLOW + "\nCreated by Abdullah Ghani")
input("\nPress Enter to return...")
nano portscanner.py
import socket
from colorama import Fore, init
init(autoreset=True)

target = input("Enter target IP: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(Fore.RED + f"Port {port} is OPEN")
    sock.close()

print(Fore.YELLOW + "\nCreated by Abdullah Ghani")
input("\nScan Finished. Press Enter...")
nano banner.py
from colorama import Fore, init
init(autoreset=True)

def show_banner():
    print(Fore.RED + """
   ██████  ██   ██  ██████  ███████ ███████ ███████  ██████
  ██       ██   ██ ██    ██ ██      ██      ██      ██
  ██   ███ ███████ ██    ██ █████   ███████ █████   ██
  ██    ██ ██   ██ ██    ██ ██           ██ ██      ██
   ██████  ██   ██  ██████  ███████ ███████ ███████  ██████
    """)
    print(Fore.GREEN + "GhostSec Toolkit - Abdullah Ghani Edition\n")
    print(Fore.YELLOW + "Created by Abdullah Ghani\n")
nano main.py
import os
from banner import show_banner

def menu():
    print("""
    [1] File Scanner
    [2] File Hasher
    [3] System Info
    [4] Port Scanner
    [5] Exit
    """)

while True:
    os.system("clear")
    show_banner()
    menu()

    choice = input("Select Option ➤ ")

    if choice == "1":
        os.system("python tools/scanner.py")
    elif choice == "2":
        os.system("python tools/hasher.py")
    elif choice == "3":
        os.system("python tools/sysinfo.py")
    elif choice == "4":
        os.system("python tools/portscanner.py")
    elif choice == "5":
        break
    else:
        print("Invalid Option")
        input("Press Enter to continue...")
nano requirements.txt
colorama

