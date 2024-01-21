#!/bin/bash
FILE="/tmp/out.$$"
GREP="/bin/grep"
clear

if [[ $EUID -ne 0 ]]
then
   clear
   echo -e "Zəhmət olmasa *root* icazəsi ilə yenidən yoxlayın!"
else
   clear
   echo -e "AzI DDoS yüklənir :)"
   apt-get -y install python-pip > /dev/null 2>&1
   apt-get -y install python3-pip > /dev/null 2>&1
   python3 -m pip install --upgrade pip > /dev/null 2>&1
   pip install tqdm > /dev/null 2>&1
   pip install pyfiglet==0.7 > /dev/null 2>&1
   echo -e "AzI DDoS yükləndi. python3 aziddos.py yazaraq proqramı başlada bilərsiniz :)"
fi
exit
