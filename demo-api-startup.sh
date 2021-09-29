#!/bin/bash
#cd /home/tiesse/demo-api/
#
# Pulizia: Elimino file di log
python <<BT
import os
list=os.listdir(".")
for file in list:
  if file.endswith(".log"):os.remove(file)
BT


# Rete NIC
#nohup 
/usr/bin/python nic_info.py 10.26.26.5 > nic_info_10.26.26.5.log 2>&1 &
#nohup 
/usr/bin/python nic_info.py 10.26.26.13 > nic_info_10.26.26.13.log 2>&1 &
# Rete NUC
#nohup 
/usr/bin/python nic_info.py 192.168.196.85 > nic_info_192.168.196.85.log 2>&1 &
exit 0
