from colorama import Fore, Style
import platform, os

OsName = platform.uname()[0]

def banner():
    if OsName == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(Fore.RED + "   ███████╗████████╗ ██████╗ ███╗   ███╗    ██████╗ ██████╗ ███████╗██╗  ██╗")
    print(Fore.YELLOW + "   ██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║    ██╔══██╗██╔══██╗██╔════╝██║  ██║")
    print(Fore.LIGHTYELLOW_EX + "   █████╗     ██║   ██║   ██║██╔████╔██║    ██████╔╝██████╔╝█████╗  ███████║")
    print(Fore.LIGHTRED_EX + "   ██╔══╝     ██║   ██║   ██║██║╚██╔╝██║    ██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██║")
    print(Fore.RED + "   ███████╗   ██║   ╚██████╔╝██║ ╚═╝ ██║    ██║     ██║     ███████╗██║  ██║")
    print(Fore.YELLOW + "   ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝")
    print(Fore.LIGHTRED_EX + "")
    print(Fore.RED + "      ███████╗████████╗ ██████╗ ███╗   ███╗    ██████╗ ██████╗ ███████╗██╗  ██╗")
    print(Fore.YELLOW + "      ██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║    ██╔══██╗██╔══██╗██╔════╝██║  ██║")
    print(Fore.LIGHTYELLOW_EX + "      █████╗     ██║   ██║   ██║██╔████╔██║    ██████╔╝██████╔╝█████╗  ███████║")
    print(Fore.LIGHTRED_EX + "      ██╔══╝     ██║   ██║   ██║██║╚██╔╝██║    ██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██║")
    print(Fore.RED + "      ███████╗   ██║   ╚██████╔╝██║ ╚═╝ ██║    ██║     ██║     ███████╗██║  ██║")
    print(Fore.YELLOW + "      ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝")
    print(Fore.RED + "                     S T O R M   B R E A K E R")
    print(Fore.YELLOW + "                     A blazing firestorm of power!")
    print(Style.RESET_ALL)

banner()
