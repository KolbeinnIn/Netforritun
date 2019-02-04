#Kolbeinn, Ágúst, Bjarki
#Skilaverkefni 3
import socket
import pickle
import os

HOST = '10.220.226.55'
PORT = 12345
stafalisti = []
s = socket.socket()
s.connect((HOST, PORT))
tries = 5
while tries > 0:
    stafur = ""
    strengur1 = s.recv(1024).decode()
    print("Þú hefur %s líf eftir" % tries)
    print("Þú ert búin/n að prufa:")
    for x in stafalisti:
        print(x, end=" ")
    print()
    print(strengur1)

    while True:
        stafur = input("Sláðu inn staf: ")
        if len(stafur) == 1:
            break
        else:
            print("aðeins einn stafur!!!")
    stafalisti.append(stafur)
    s.send(pickle.dumps(stafur))
    lif = s.recv(1024).decode()
    tries = int(lif)

    if tries == 6:
        print("Til hamingju, þú vannst!")
        print("Oðrið var: %s" % s.recv(1024).decode().replace(" ", ""))
        break
if tries == 0:
    print("Til hamingju, þú tapaðir")
    print("Oðrið var: '%s'" % s.recv(1024).decode().replace(" ", ""))
s.close()


