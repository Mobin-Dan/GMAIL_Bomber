import os
from colorama import Fore
import time
from pyngrok import ngrok
from subprocess import Popen
x = input("enter your password =>")
if x=="t.me/termux_learning":
        pass
else:
        print("password is t.me/termux_learning")
print(Fore.CYAN)
os.system("clear")
print("""

                                                     
 _____           _ _     _____           _           
|   __|_____ ___|_| |___| __  |___ _____| |_ ___ ___ 
|  |  |     | .'| | |___| __ -| . |     | . | -_|  _|
|_____|_|_|_|__,|_|_|   |_____|___|_|_|_|___|___|_|  
                                                     
-----------------------------------
|   Coding By Mobin-Dan |mr_ngrok ‌ ‌|
|           T.me/Termux_learning   |
-----------------------------------
""")
""")
re =input(Fore.RED+"[PORT]"+" =>")
with open("server","w") as phplog:
    Popen(("php","-S","localhost:"+re),stderr=phplog ,stdout=phplog)
print(Fore.GREEN)
link=ngrok.connect(re,"http")
print(link)
print(Fore.RED+"Just "+Fore.GREEN+"Open"+Fore.CYAN+"Link:)")
input("")

