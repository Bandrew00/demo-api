1) Installare FLASK tramite PIP INSTALL

2) lanciare in background lo script nic_info.py
   con il comando:

	 nohup python /home/tiesse/demo-api/nic_info.py > log.txt 2>&1 &
   
         Per renderlo attivo allo startup aggiungere il comando con crontab -e:
         @reboot /home/tiesse/demo-api/demo-api-startup.sh 

   Si mette in ascolto sulla porta http://localhost:8080
   e crea il file di log 'log.txt' x info ed eventuali errori

3) Arresto Server API:
   ps -ef | grep -i nic_info 
   ottieni il PID (es. 7089) per poi fare:
   kill -9 7089 

3) Per andare sul browser e digitare:
   http://nuc:8080 

   per ottenere visione del JSON locale tramite GET, digitare:
   http://nuc:8080/info
 
   per cpiare con HTTP POST il JSON file digitare il comando curl:
   curl -X POST -H "Content-Type: application/json" -d @"C:\Users\andreab\PROGETTI\Esempio Flask\copia.json" "http://localhost:8080/Info"   
