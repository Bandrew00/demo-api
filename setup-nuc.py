import subprocess as sp
import logging, os, sys

# LO SCRIPT CREA UNA STRUTTURA DI CARTELLE SU FILE SYSTEM AVENDO COME RADICE
# LA CARTELLA 'DDNS CONFIG'.
# COME PARAMETRO DI INPUT ABBIAMO L'INDIRIZZO IP DELLA NUC DA CONFIGURARE.
# DA TALE INDIRIZZO VERRA' CREATA LA CARTELLA CORRISPONDENTE.
# SUCCESSIVAMENTE VIA SSH, TRAMITE IL COMANDO 'ip r' DALLA NUC SI RICAVERANNO
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
# FILE YAML DI CONFIGURAZIONE PER L'AGGIORNAMENTO DDNS ESEGUITO 
# TRAMITE LO SCRIPT './demo/update.py'
#
c_ddns_config_folder = './DDNS-CONFIG/'
c_nuc_ssh_user 	     = "tiesse@"

if __name__ == "__main__":

   NUM_PARAMS 	= 1
   ERROR 	= False
   error        = None

   logging.basicConfig(filename='setup-nuc.log',
                        filemode='a', #'w',
                        level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s') 
   try:
       if ( len(sys.argv)-1 < NUM_PARAMS ):
          error ="DDNS Fail: numero insufficiente di parametri!\nUso: python setup-nuc.py <parameter1> (parameter1=Indirizzo IP NUC: es 192.168.197.10)"
	  ERROR = True
       else:
          nuc_ip       = str(sys.argv[1])                 # parametro indirizzo NUC IP
	  nuc_folder   = "nuc-{}/".format(nuc_ip)         # cartella NUC da creare
	  ssh_command  = 'ssh ' + c_nuc_ssh_user + nuc_ip # comando SSH con credenziali utente NUC (ssh tiesse@xx.xx.xx.xx)
          # Path NUC

          # ricavo indirizzi NIC dalla tabella di routing della NUC
          cmd = ssh_command + ' ip r' + ' | awk \'{ print $1 }\''
          try:
	     for ip in sp.check_output(cmd,shell=True).splitlines():
     	        if ip.endswith('/30'): # maschera relativa all'indirizzo IP NIC       
		   ip         = ip[0:ip.rfind('/')]
                   offset     = ip.rfind('.')
                   old_digit  = ip[offset+1:] 
                   new_digit  = str(int(old_digit) +2) # aggiungo 2 all'ottetto lsb per ottenere IP NIC
                   ip         = ip.replace('.'+old_digit, '.'+new_digit)
                   nic_folder = "nic-"+ip 
                   if not os.path.exists("./" + c_ddns_config_folder + nuc_folder + nic_folder):
             	      os.makedirs(c_ddns_config_folder + nuc_folder + nic_folder)
                      logging.info("Nuova cartella: " + c_ddns_config_folder + nuc_folder + nic_folder) 
                   
          except (Exception) as e:
 	      error = "DDNS Fail: {}".format(e)
              logging.error(error)
   except (Exception) as e:
 	  error = "DDNS Fail: {}".format(e)
          ERROR = True
   finally:
          if ERROR:
             print(error)
             logging.error(error)
             sys.exit(1)

