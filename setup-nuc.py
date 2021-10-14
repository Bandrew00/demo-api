#
# LO SCRIPT CREA SU FILE SYSTEM,UNA STRUTTURA DI CARTELLE AVENDO COME RADICE
# LA CARTELLA 'DDNS CONFIG'.
# COME PARAMETRO DI INPUT ABBIAMO L'INDIRIZZO IP DELLA NUC DA CONFIGURARE.
# DA TALE INDIRIZZO VERRA' CREATA LA CARTELLA CORRISPONDENTE.
# SUCCESSIVAMENTE VIA SSH, CON IL COMANDO 'ip r', DALLA NUC SI RICAVERANNO
# GLI INDIRIZZI IP DI OGNI SINGOLA NIC DA CUI VERRA' CREATA LA RELATIVA
# SOTTOCARTELLA COME INDICATO NEL SEGUENTE SCHEMA:
# 
#
#                               'DDNS CONFIG'
#                                    /\ 
#                                   /  \
#                                  /    \
#                nuc-192.168.197.10      nuc-192.168.197.20
#                ------------------      ------------------
#                 nic-10.26.26.2 |        nic-10.26.26.2  |
#                 nic-10.26.26.6 |        nic-10.26.26.6  |
#                nic-10.26.26.10 |        nic-10.26.26.10 |
#                nic-10.26.26.14 |        nic-10.26.26.14 |
#                nic-10.26.26.18 |        nic-10.26.26.18 |
#                nic-10.26.26.22 |        nic-10.26.26.22 |
# 
# INFINE PER OGNI SOTTOCARTELLA nic-xx.xx.xx.xx SARA' ASSOCIATO UN
# FILE YAML DI CONFIGURAZIONE PER L'AGGIORNAMENTO DDNS PROCESSATO 
# DALLO SCRIPT './demo/update.py'
#
#
import subprocess as sp
import logging, os, sys

c_ddns_folder  = (os.path.expanduser('~'))+"/2DDNS-CONFIG/"
c_nuc_ssh_user = "tiesse@"
c_num_params   = 1
ERROR 	      = False
error          = "DDNS Fail: numero insufficiente di parametri!\nUso: python setup-nuc.py <parameter1> (parameter1=Indirizzo IP NUC: es 192.168.197.10)"

if __name__ == "__main__":
   logging.basicConfig(filename='setup_nuc.log',
                        filemode='a', #'w',
                        level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s') 

   try:
      if ( len(sys.argv)-1 < c_num_params ):
	      ERROR = True
      else:
         nuc_ip = str(sys.argv[1])                 # parametro indirizzo NUC IP
         ssh    = 'ssh ' + c_nuc_ssh_user + nuc_ip # comando SSH con credenziali utente NUC (ssh tiesse@xx.xx.xx.xx)
         #
         # Path NUC
         #
         nuc_hostname = sp.check_output(ssh + ' hostname',shell=True) # ricavo nome host della nuc
         nuc_folder   = nuc_hostname.replace('\n','')+"_"+nuc_ip+'/'  # cartella NUC da creare
         #
         # ricavo indirizzi NIC dalla tabella di routing della NUC
         #
         cmd = ssh + ' ip r' + ' | awk \'{ print $1 }\' | grep -i \'/30\''
         for ip in sp.check_output(cmd,shell=True).splitlines():
            ip         = ip[0:ip.rfind('/')]
            old_digit  = ip[ip.rfind('.')+1:]    # ultima cifra indirizzo IP xxx.xxx.xxx.nnn
            new_digit  = str(int(old_digit) +2)  # aggiungo 2 all'ottetto lsb per ottenere IP NIC
            ip         = ip.replace('.'+old_digit, '.'+new_digit)
            #
            # Ottengo nome host della NIC via SSH
            #
            nic_hostname = sp.check_output(ssh + ' ssh root@' + ip + ' hostname',shell=True)
            nic_folder   = nic_hostname.replace('\n','')+"_"+ip 
            if not os.path.exists("./" + c_ddns_folder + nuc_folder + nic_folder):
               os.makedirs(c_ddns_folder + nuc_folder + nic_folder)
               logging.info("Nuova cartella: " + c_ddns_folder + nuc_folder + nic_folder)
            pass
   except (Exception) as e:
      pass
   finally:
      pass

