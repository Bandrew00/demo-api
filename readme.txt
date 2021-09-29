1) Installare FLASK tramite PIP INSTALL

2) lanciare in background lo script nic_info.py
   con il comando:

	 nohup python /home/tiesse/demo-api/nic_info.py param1 param1.txt 2>&1 &
         es. nohup /usr/bin/python nic_info.py 10.26.26.5 > nic_info_10.26.26.5.log 2>&1 &   
         Per renderlo attivo allo startup aggiungere il comando con crontab -e:
         @reboot /home/tiesse/demo-api/demo-api-startup.sh parama1 > param1.log 2>&1 $

   Si mette in ascolto sulla porta http://localhost:8080
   e crea il file di log 'log.txt' x info ed eventuali errori

3) Arresto Server API:
   ps -ef | grep -i nic_info 
   ottieni il PID (es. 7089) per poi fare:
   kill -9 7089 

3) Per andare sul browser e digitare:
   http://<host ip>:8080 

   per ottenere visione del JSON locale tramite GET, digitare:
   http://<host ip>:8080/info?ip=nic-ip
 
   per cpiare con HTTP POST il JSON file digitare il comando curl:
   curl -X POST -H "Content-Type: application/json" -d @"C:\Users\andreab\PROGETTI\Esempio Flask\copia.json" "http://localhost:8080/Info"   

 ######## GitHub
 sudo apt update && sudo apt install git

##########################################################
DOWNLOAD
##########################################################
git clone  https://github.com/Bandrew00/demo-api.git 
git clone  https://github.com/Bandrew00/demo.git

When you clone or pull a Git repository, the entire contents 
of that repository are downloaded by default.

To download an individual file from a repository, first navigate 
to the file you want to download on the GitHub website. Then, 
click the “Raw” download button that appears on the top right 
corner of the file explorer window on your page:
When we click “Raw”, we are directed to a plain-text version of our file.

This takes us to the following URL:
es:
https://raw.githubusercontent.com/Career-Karma-Tutorials/ck-git/master/README.md

Download a Single File Using Wget
We can download a single file from the command line using the wget command. 
This is because we can write the URL for the file we want to retrieve.

Like the last approach, you can only download a single file using wget if that file is public.

All we have to do to download a single file using wget is write a wget command:

wget -L https://raw.githubusercontent.com/Career-Karma-Tutorials/ck-git/master/main/app.py
curl \
  -H 'Authorization: token $YOUR_TOKEN' \
  -H 'Accept: application/vnd.github.v3.raw' \
  -O \
  -L 'https://api.github.com/repos/:owner/:repo/contents/:path'
The -O will save the contents in a local file with the same name as the remote file name. 
For easier use you can wrap it in a script

references
https://stackoverflow.com/questions/9159894/download-specific-files-from-github-in-command-line-not-clone-the-entire-repo
https://careerkarma.com/blog/git-download-a-single-file-from-github/


##########################################################
UPLOAD
##########################################################
 add repository  GitHub
 Upload file da local host su GitHub tramite comando: 


1) Initialize Local Directory
   Now we will intialize our project. 
   Use the below command to initialise the local directory as Git repository.
   $ git init

2) Add Local repository
   Add all the files in the local directory to staging using the command below.
	$ git add . 
   or a file
        $ git add README.md

4) Commit Repository
     
        $ git commit -m "Initial commit"
 
5) Add Remote Repository url
   Now, copy the remote repository URL provided by github to you when you 
   published (created) your repository on GitHub.

        $ git remote add origin https://github.com/Bandrew00/demo-api.git

6) Push Local Repository to github
   In the last step, use the below command line in your terminal to push 
   the local repository to GitHub. 
   It will upload the file or project on github.

	$ git push origin master

   If you use -u in the command, it will remember your preferences 
   for remote and branch and you can simply use the command git 
   push next time.

        $ git push -u origin master

7) Pull Repository from github
   Pull the desired branch from the upstream repository. 
   This method will retain the commit history without modification.

        $ git pull origin master

brief:
 1- git init
 2- git add .
 3- git commit -m "Add all my files"
 4- git remote add origin https://github.com/USER_NAME/FOLDER_NAME
 5- git pull origin master --allow-unrelated-histories
 6- git push origin master

references:
https://stackoverflow.com/questions/12799719/how-to-upload-a-project-to-github
https://www.tutsmake.com/upload-project-files-on-github-using-command-line/
https://www.dunebook.com/upload-files-to-github-from-the-command-line/
