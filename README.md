# Student-portal-using-OpenStack

Goal - Create student portal using OpenStack Swift.

Project flow-
1.)6 instances are instantiated both manually and using Python in the OpenStack UI.

- Instances/Nodes - Professor Node(1 instance), Student Node(3 instances), Proxy Server (1 instance), Object Server (1 instance)
- Containers/Subjects - Student nodes can access objects in their own container only whereas the admin node can access the objects in all containers or subjects of students.
- Objects/Files - A combination of REST API call-methods and curl commands are used to perform object actions such as file upload or file download.

2.) Edit the proxy configuration file -
Student account - Admin privileges (create, delete, modify objects in its container)
Professor account - Reseller admin privileges (provides admin privileges to non-admin privileges in OpenStack Swift)

3.) Process -
- Professor node instantiates the containers and publishes these containers to the student nodes that are enrolled in the course. The professor node has been assigned reseller admin privileges, thus giving the professor node privileges to generate and assign containers to other student nodes. The student nodes have been assigned admin privileges, hence, on creation of a container in the student's account by the professor node, the student can access that container due to the assigned admin privileges.
- Student and professor nodes upload/delete/view objects from containers using REST API methods as described in point 1. To avoid ambiguity in file names, append file name with account_user_names. 


A diagram of how everything works.

![OpenStack1](https://user-images.githubusercontent.com/22990797/124118337-115f4200-da26-11eb-9cb8-f94148ba9f22.PNG)


Part 2:

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
