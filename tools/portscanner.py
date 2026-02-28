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
