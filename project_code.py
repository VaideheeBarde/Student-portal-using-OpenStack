import os
import subprocess
import urllib2
import requests,json

path = "/home/ubuntu"
def list_files(path):
	print "********The file in the local directory are: ***********"
	i = 1
	for file in os.listdir(path):
		if not file.startswith('.') and os.path.isfile(os.path.join(path, file)):
			print i,file
			i = i+1
def upload_files(path):
	print "*******Enter the number besides the container for uploading the file*********"
	bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_anuj?format=json -X GET -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'
	output = subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
	output1 = output.communicate()[0]
	j = json.loads(output1)
	i=1
	listcontainer = []
	for row in j:
		listcontainer.append(row['name'])
		print i,row['name']
		i = i+1
	index = input()
	container = listcontainer[index-1]
	print "********Enter the number besides the file for uploading to the repository ***********"
	i = 1
	list1 = []
	for file in os.listdir(path):
		if not file.startswith('.') and os.path.isfile(os.path.join(path, file)):
			list1.append(file)
			print i,file
			i = i+1
	index = input()
	file_to_upload = list1[index-1]	 	
	bashcom ='curl -s https://172.31.0.154:8080/v1/AUTH_anuj/'+container+'/ --upload-file '+file_to_upload+ ' -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'
	output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
	output1 = output.communicate()[0] #subprocess.check_output(['bash','-c',bashcom]) 
	print "File uploaded successfully!!!"
def list_uploaded_files(path):
	print "*******Enter the number besides the container to list the file of that container*********"
        bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_anuj?format=json -X GET -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'
        output = subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        output1 = output.communicate()[0]
        j = json.loads(output1)
        i=1
        listcontainer = []
	for row in j:
                listcontainer.append(row['name'])
                print i,row['name']
                i = i+1
        index = input()
        container = listcontainer[index-1]
	bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_anuj/'+container+'?format=json -X GET -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'	
        output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        output1 = output.communicate()[0]
	j = json.loads(output1)
	i = 1
	print "Files present in "+container+" are: " 
	for row in j:
		print i,row['name']		
		i = i+1
	
def delete_uploaded_files(path):
	print "*******Enter the number besides the container in which the file is to be deleted*********"
        bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_anuj?format=json -X GET -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'
        output = subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        output1 = output.communicate()[0]
        j = json.loads(output1)
        i=1
        listcontainer = []
        for row in j:
                listcontainer.append(row['name'])
                print i,row['name']
                i = i+1
        index = input()
        container = listcontainer[index-1]
	bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_anuj/'+container+'?format=json -X GET -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'
        output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        output1 = output.communicate()[0]
        j = json.loads(output1)
        i = 1
	list1= []
        for row in j:
		list1.append(row['name'])
                print i,row['name']
                i = i+1	
	print "***************Enter the number besides the file to delete from the repository **************"
	index = input()
	file_to_delete = list1[index-1]
	print file_to_delete
	bashcom = 'curl -s https://172.31.0.154:8080/v1/AUTH_anuj/'+container+'/'+file_to_delete+ ' -X DELETE -H "X-Auth-Token: AUTH_tk381d832d92c74828af7ba220d739e7b8" --insecure'
        output =  subprocess.Popen(bashcom, stdout=subprocess.PIPE, shell=True)
        output1 = output.communicate()[0]
	print "File deleted!!!"
while(True):
	print "****************Menu********************"
	print "Enter 1 for listing all files in the local directory"
	print "Enter 2 to upload a specific file to the repository"
	print "Enter 3 for listing files uploaded to repository"
	print "Enter 4 to delete a specific file from the repository"
	number = input();
	if number == 1:
		list_files(path)
		print
		print
	elif number == 2:
		upload_files(path)
		print
		print
	elif number == 3:
		list_uploaded_files(path)
		print
		print
	elif number == 4:
		delete_uploaded_files(path)
		print
		print	
	else:
		exit()