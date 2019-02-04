#Kolbeinn, Ágúst, Bjarki
#Skilaverkefni 3
import socket
import pickle
import os

#HOST = '10.220.226.55'
HOST = socket.gethostname()
PORT = 12345

while True:
    s = socket.socket()
    s.connect((HOST, PORT))
    tries = 5
    while tries > 0:
        stafur = ""
        strengur1 = s.recv(1024)
        print("Þú hefur %s líf eftir" % tries)
        print(strengur1.decode())
        while len(stafur) != 1:
            stafur = input("Sláðu inn staf: ").encode()
        s.send(stafur)
        lif = s.recv(1024).decode()
        tries = int(lif)

    s.close()



