import pickle
import socket
from os import listdir
from os.path import isfile, join
from re import *

HOST = socket.gethostname()
PORT = 12345

s = socket.socket()
s.bind((HOST, PORT))
s.listen(2)

onlyfiles = [f for f in listdir("./") if (isfile(join("./", f)) and match(".*.txt", f))]
while True:
    data = pickle.dumps(onlyfiles)
    c, addr = s.accept()
    c.send(data)
    recieve = c.recv(1024)
    try:
        svar = pickle.loads(recieve)
        print(svar)
        uppsk = onlyfiles[svar - 1]
        f = open(uppsk, 'rb')
        print('Connected by', addr)
        data = f.read(1024)
        c.send(data)
        f.close()
    except:
        pass
