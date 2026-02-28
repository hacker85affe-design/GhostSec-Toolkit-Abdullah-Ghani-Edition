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
