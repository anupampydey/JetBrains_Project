import socket
import sys
import itertools
import string


def pwd_generator():    # function made for stage 2 test, not implemented in this stage
    global message
    for i in range(1, 5):
        # generates keys of length from 1 to 4 for matching with password
        for key in itertools.product(alph_num, repeat=i):
            pwd = ''.join(key)
            client_socket.send(pwd.encode())
            message = client_socket.recv(1024).decode()
            if message == "Connection success!":
                print(pwd)
                return True


def passwords_dict():
    global message
    with open('passwords.txt', 'r') as pass_file:
        lines = pass_file.readlines()
        for strng in lines:
            pwd = strng.strip()
            if pwd.isnumeric():
                client_socket.send(pwd.encode())
                message = client_socket.recv(1024).decode()
                if message == "Connection success!":
                    print(pwd)
                    return True
            else:
                word_permut = set(map(''.join, itertools.product(*zip(pwd.lower(), pwd.upper()))))
                for word in word_permut:
                    client_socket.send(word.encode())
                    message = client_socket.recv(1024).decode()
                    if message == "Connection success!":
                        print(word)
                        return True

args = sys.argv
hostname = str(args[1])
port = int(args[2])
alph_num = string.ascii_lowercase + string.digits
message = ""

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    # hacked = pwd_generator() # Stage 2 Test
    hacked = passwords_dict()
    if not hacked:
        print(message)
