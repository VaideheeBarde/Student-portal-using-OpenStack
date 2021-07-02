# Student-portal-using-OpenStack

Goal - Create student portal using OpenStack Swift.

6 instances are instantiated both manually and using Python in the OpenStack UI. 3 instances represent students, 1 instance represents admin i.e the professor, 1 instance is the proxy server and the remaining instance is the object server where the assignment files (objects) are stored. All the files are uploaded and downloaded through the proxy server. A combination of REST API call-methods and curl commands are used to perform file actions such as upload or download.

Admin node privileges - The admin node can access the files in all the containers (subjects) of the students. 
Student node privileges - The three student nodes can access files in their own container only. They cannot access files from the containers of other students.
In this project, containers are subjects and files that are uploaded/downloaded/deleted are the objects within each container. Thus, it makes it easier to divide the container as per the subject and the objects within each container as files.
A diagram of how everything works.

![OpenStack1](https://user-images.githubusercontent.com/22990797/124118337-115f4200-da26-11eb-9cb8-f94148ba9f22.PNG)

Figure of System Architecture

The proxy configuration file was edited. This included certain student accounts having admin privileges and the professor account having reseller admin privileges.
Admin privileges – user can create, delete and modify objects in its container. 
Reseller admin privileges – This gives admin privileges to non-admin users in swift. 
Part 1 :
The implementation of the architecture starts with a python script in which professor node having the reseller admin privileges creates containers and publishes these containers to all student nodes who are enrolled in the course.
Students have admin privileges of their own account. They can see the containers created by the professor in his/her account.
Part 2:
Now, through the python script for student node, the student having file or assignment (object) can upload it to the object store node. That means the file is uploaded to the storage instance that we created. The student can also delete the file the file from the store node such that the file wouldn’t be retrieved by the professor node.
After the assignment deadline, the professor can download all the files uploaded by the students. 
All the uploads and downloads happen using basic APIs like GET and PUT. The professor can view/list all the files uploaded by all the students and can download all of them.
Also, a new technique has been added wherein the name of the file has been appended by the name of the account user. This avoids ambiguity if two students upload the file using the same file name.
Deleting the files is also possible. Authentication of http requests is done by a feature in Swift using ‘TempAuth’. This generates a key for every session.
Professor code:
Initially, we have an array which contains the list of accounts
Publish containers to all accounts–
We use CURL commands and REST API “PUT” command to create containers in each account. HTTP request and replies are authenticated using the ‘TempAuth’ feature of Swift API by generating a unique session key.
For every HTTP request and reply a unique session key is generated which can be found manually in the OpenStack containers that are created.
Subprocess.popen and subprocess.pipe commands (these are two commands used for subprocesses) are used for the container creation alongwith the CURL commands. Since we are using shell scripting, we also make shell=True
Subprocess.popen → The underlying process creation and management in the subprocess module is handled by Popen class.
Subprocess.pipe → It is a special value that is used as stdout (in our project, it is stdout. It can also be used as stdin, stderr) to Popen. It indicates that the pipe to the standard stream should be opened. It is most useful with Popen.communicate().
The popen.communicate() interacts with the process. It sends data to stdin.
This is how a container for a subject is created.

List files in the local directory –
For listing the files in the local directory, we use os.listdir(path) function. The path is initialized at the beginning of the code to whatever path name we want. In this code, it is “home/ubuntu/”
The listdir(path) tells us all the files in that directory.
We now use os.path.join(path, file) and join the path name to the file name. The accuracy of the obtained path is now checked with os.path.isfile function. Thus, all the files in the local directory are listed.

Download a specific file to the repository –
Initially, we go to a container from which file is to be downloaded. Container = subject name. Now, we scroll through all the accounts using a for loop. Thus, we can see all the files uploaded in this container by an account holder using the subprocesses popen and pipe to communicate. In order to load the files, we use json.loads command.
We can download all the files using the GET command of HTTP request and response (use the unique authentication key). Also, the curl commands are used.
Student code:
List all files in the local directory –
Similar to the list files in the professor code.

Upload a specific file to the repository –
List all the files uploaded to the repository –
Delete a specific file from the repository – 
