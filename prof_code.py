import os
import subprocess
import urllib2
import requests,json

list_of_account = ['anuj','sanket','aakash']
path = "/home/ubuntu"

def publish_container(path):
	print "******Enter the container name to be published to all the accounts*********"
	container = raw_input()
	for account in list_of_account:
#		print account	
		bashcom =  'curl -s https://172.31.0.154:8080/v1/AUTH_'+account+'/'+container+ ' -X PUT -H "Content-Length: 0" -H "X-Auth-Token: AUTH_tk21f9d21ca2d24ab390003e6ed28032a4" --insecure'
		output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        	output1 = output.communicate()[0]
	print "Containers created for all the account!!!"


def list_files(path):
	print "********The file in the local directory are: ***********"
	i = 1
	for file in os.listdir(path):
		if not file.startswith('.') and os.path.isfile(os.path.join(path, file)):
			print i,file
			i = i+1
def download_files(path):
	print "******Enter the container name from which the files are to be downloaded*********"
        container = raw_input()
#	print "*******************Enter 0 to download all files from the container**********************"
#	print "******************************************OR*********************************************"
#	print "********Enter the number besides the file for downloading from the repository ***********"
	for account in list_of_account:
#		print account
		bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_'+account+'/'+container+'?format=json -X GET -H "X-Auth-Token: AUTH_tk21f9d21ca2d24ab390003e6ed28032a4" --insecure'
#		print bashcom
        	output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        	output1 = output.communicate()[0]
        	j = json.loads(output1)
        	i = 1
        	list1= []
        	for row in j:
                	list1.append(row['name'])
#              	 	print i,row['name']
                	i = i+1
#	index = input()
#	if index == 0:
		list_len = len(list1)
		for i in range(0,list_len):
			file_to_download = list1[i]
			bashcom ='curl -s -o '+account+'_'+file_to_download+'  https://172.31.0.154:8080/v1/AUTH_'+account+'/'+container+'/'+file_to_download+ ' -H "X-Auth-Token: AUTH_tk21f9d21ca2d24ab390003e6ed28032a4" --insecure'
#			print bashcom
             		output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
                	output1 = output.communicate()[0]	
#	else:
#		file_to_download = list1[index-1] 
#		bashcom ='curl -s -O https://172.31.0.154:8080/v1/AUTH_'+account+'/'+container+'/'+file_to_download+ ' -H "X-Auth-Token: AUTH_tk3b0737acb4d44d2398f8ed2469974564" --insecure'
#		output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
#		output1 = output.communicate()[0] #subprocess.check_output(['bash','-c',bashcom]) 


while(True):
	print "****************Menu********************"
	print "Enter 1 for publishing container to all the accounts"
	print "Enter 2 for listing all files in the local directory"
	print "Enter 3 to download a specific file to the repository"
	number = input();
	if number == 1:
		publish_container(path)
		print 
		print
	if number == 2:
		list_files(path)
		print
		print
	elif number == 3:
		download_files(path)
		print
		print
	else:
		exit()
	