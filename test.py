import subprocess as sp
import json
import socket
from datetime import datetime

c_json_file      = '_test.json'
c_web_api_host   = "10.26.26.13"

if __name__ == "__main__":

   cmd   	 = 'ip -o route get 1.1.1.1 | cut -d \" \" -f 7'
   lan_ip	 = sp.check_output(cmd,shell=True).replace('\n','')
   lan_interface = "eno1.2"
   cmd	         = 'ip addr show | grep -i ' + lan_interface + ' | grep -i inet| awk \'{ print $2 }\' | awk -F \"/\" \'{ print $1 }\''
   l_ip          = []
   #d_ip          = {}
   for ip in sp.check_output(cmd,shell=True).splitlines():
     o = ip.rfind('.')
     old_digit = ip[o+1:]
     new_digit = str(int(old_digit) +1)
     ip = ip.replace('.'+old_digit, '.'+new_digit)
     l_ip.append('nic-'+ip)

   json_file = {"Date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), socket.gethostname() + "-" + lan_ip : l_ip }


   #print(list(json_file.items())[0])
   key = json_file.keys()[1]
   print(key)

   for ip in json_file[key]:
      print(ip) 



   with open(c_json_file, 'w') as f:
             json.dump(json_file, f, indent=4)



   # INVIO Tramite Rest API  il risultato del
   # JSON file
   cmd = 'wget -L "Content-Type: application/json" -d @"' + c_json_file + '" "http://' + c_web_api_host + ':8080/Add"'
   #cmd = 'curl -X POST -H "Content-Type: application/json" -d @"' + c_json_file + '" "http://' + c_web_api_host + ':8080/Info"' 

   print (cmd)
   post = sp.check_output(cmd,shell=True)
   print(post)


   # preparo JSON

