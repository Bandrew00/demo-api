from flask import Flask, request
import json, logging, os# , sys

c_host 		    = "localhost" # None  # Server flask
c_ddns_folder	= (os.path.expanduser('~'))+"/DDNS-CONFIG/"
c_nic_info_url  = 'http://{}:8080/Info?id={}' 
#c_setup_folder = 'SETUP-DDNS/'
def TestFolder(folder,l_folder):
    
    for subdir, dirs, files in os.walk(folder):
        
       # for f in files:
       #     l_file.append(f)
       #     pass 
        
        for folder in dirs:   
            l_file = [f for f in os.listdir(os.path.join(subdir,folder))]
            if len(l_file)>0:
                d_file= {}
                d_folder= {}
                for file in l_file :
                    d_file[file]=c_nic_info_url.format(c_host,os.path.join(subdir,folder))
                
                d_folder[folder] = d_file
                l_folder.append(d_folder)
            else:l_folder.append(folder)
            
            
            TestFolder(os.path.join(subdir,folder),l_folder) 
    pass

app = Flask(__name__)

################################################################
# Pagina iniziale
################################################################
@app.route("/")
def Info():
    try:
        d_folder = {}
        d_item   = {}
        l_folder = []
        ddns_folder=[]
        nic_info_url = 'http://{}:8080/Info?id={}' 
        # ricavo la lista delle cartelle in DDNS
        # for folder in next(os.walk(c_ddns_folder))[1]:
        #     d_item[folder]= nic_info_url.format(c_host,folder)
        #     l_folder.append(d_item) 
        #     d_item={}
       
        for folder in next(os.walk(c_ddns_folder))[1] :
                       
            TestFolder(os.path.join(c_ddns_folder,folder),l_folder)
            d_item[folder]=l_folder
            ddns_folder.append(d_item)
            l_folder = []
            d_item   ={}
        
        d_folder =  {"DDNS LIST" : l_folder }
        nic_list = json.dumps( ddns_folder,indent=4)
        return nic_list,200
    except (Exception) as e:
	    return "DDNS Fail: {}".format(e), 404

################################################################
# Ottieni il contenuto del file JSON da visualizzare
# Add URL endpoints
################################################################
@app.route("/Info")
def Get():
    try:
        # es. http://nuc:8080/Info?id=<nomehost>-10.26.26.2
        id 	  = request.args.get("id")
        json_file = c_ddns_folder + id + '/data.json'
    	# Opening JSON file
    	with open(json_file, 'r') as f:
	        json_data = json.load(f)
    	json_formatted_str = json.dumps(json_data,indent=4)
 	return json_formatted_str,200
    except (Exception) as e:
	    return "DDNS Fail: {}".format(e), 500
################################################################
# Copia e sostituisci file JSON su C_HOST
################################################################
##@app.route("/Info", methods=["POST"])
##def Post():
##    try:
##    	json_data = request.json
##    	# Prelevo chiave composta da NAME + LAN per ricavare la cartella in DDNS
##    	nic_name   = json_data["NAME"].replace('\n','')
##    	nic_lan    = json_data["LAN"].replace('\n','')
##    	nic_folder = c_ddns_folder + nic_name + '-' + nic_lan
##    	# Path dove scaricare il Data JSON
##    	if not os.path.exists(nic_folder):os.makedirs(nic_folder)
##    	with open(nic_folder + '/data.json', 'w') as f:
##             json.dump(json_data, f, indent=4)
##    	return "OK",201
##    except (Exception) as e:
##	    return "DDNS Fail: {}".format(e), 500
##
################################################################
# Creo struttura ad albero su file system (Mappatura NUC + NIC)
################################################################
##@app.route("/Add", methods=["POST"])
##def Add():
##    try:
##        json_data    = request.json
##    	# Prelevo chiave NUC per creare la cartella radice in SETUP-DDNS
##        nuc_name_key = json_data.keys()[1] #.replace('\n','')
##        nuc_folder   = c_setup_folder + nuc_name_key + '/'
##        if not os.path.exists(nuc_folder):os.makedirs(nuc_folder)
##	    # ciclo la lista delle nic con chiave nuc_name_key
##        # e creo struttura su file system
##        for nic_name in json_data[nuc_name_key]:
##            nic_folder = nuc_folder + nic_name
##            if not os.path.exists(nic_folder):os.makedirs(nic_folder)
##        return "OK",201
##    except (Exception) as e:
##        return "DDNS Fail: {}".format(e), 500
##	  
##
##
##
if __name__ == '__main__':

    #NUM_PARAMS 	= 1
    #ERROR 	    = False
    #error       = None
    logging.basicConfig(filename='nic_info.log',
                        filemode='a', #'w',
                        level=logging.ERROR,
                        format='%(levelname)s: %(asctime)s: %(message)s') 
    
    try:
        pass
        # if ( len(sys.argv)-1 < NUM_PARAMS ):
        #    error ="DDNS Fail: numero insufficiente di parametri!\nUso: python nic_inf <parameter1> (Web API Host Ip es. 10.26.26.13)"
        #    ERROR = True
        # else:
        #    c_host = str(sys.argv[1])
        #    # Path dove scaricare il Data JSON
        if not os.path.exists(c_ddns_folder):
	            os.makedirs(c_ddns_folder)
    	app.run(host=c_host,port=8080)
    except (Exception) as e:
        pass
    finally:
        pass
