# Paquetes necesarios (Obligatorio)

import os
import requests
import colorama
import time
import subprocess

# Colores (Ambiental)

BLACK = '\033[30m'
RED = '\033[91m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[97m'
RESET = '\033[39m'
GRAY = "\033[90"

# Sistema de inicio (Obligatorio)

os.system("clear")

# Menu de interacion [1] (Obligatorio)

time.sleep(0.4)
print(RED+"███╗  ██╗██╗   ██╗███╗   ███╗      ██████╗  █████╗ ██╗  ██╗")
print("████╗ ██║██║   ██║████╗ ████║      ██╔══██╗██╔══██╗╚██╗██╔╝")
print("██╔██╗██║██║   ██║██╔████╔██║█████╗██║  ██║██║  ██║ ╚███╔╝ ")
print(WHITE+"██║╚████║██║   ██║██║╚██╔╝██║╚════╝██║  ██║██║  ██║ ██╔██╗ ")
print("██║ ╚███║╚██████╔╝██║ ╚═╝ ██║      ██████╔╝╚█████╔╝██╔╝╚██╗")
print("╚═╝  ╚══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═════╝  ╚════╝ ╚═╝  ╚═╝")

time.sleep(0.2)
print(f"{GRAY}-----------------------------------------------")
time.sleep(0.2)
print(f"{WHITE}Autor    {GRAY}➟{RED}    @Geesy970{RESET}")
time.sleep(0.2)
print(f"{GRAY}-----------------------------------------------")
time.sleep(0.2)
print(f"{BLUE}Discord    {GRAY}➟{RED}    discord.gg/MQpS9BXbpE{RESET}")
time.sleep(0.2)
print(f"{GRAY}-----------------------------------------------")
time.sleep(0.2)
print(f"{MAGENTA}GitHub    {GRAY}➟{RED}    @ProxyCKL{RESET}")
time.sleep(0.2)
print(f"{GRAY}----------------------------------------------- \n")
time.sleep(0.2)

api_key = '6f0f8f7a341f0c0ec2b72f461f7fdb5a'

number = int(input(RED+"Numero de telefono: "+YELLOW))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1">

for key, value in data.json().items():

    print("%s: %s" % (key, value))

exit()
