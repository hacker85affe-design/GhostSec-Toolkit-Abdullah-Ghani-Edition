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
