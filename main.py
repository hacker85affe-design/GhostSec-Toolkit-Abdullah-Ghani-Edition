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
