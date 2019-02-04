#Kolbeinn, Ágúst, Bjarki
#Skilaverkefni 1
import socket
import pickle

HOST = '10.220.226.55'
PORT = 12345

s = socket.socket()
s.connect((HOST, PORT))
data = pickle.loads(s.recv(1024))
for x in range(len(data)):
    print(x+1, data[x])


numer = int(input("Veldu númer: "))
s.send(pickle.dumps(numer))
f = open(data[numer-1], 'wb')

data = s.recv(1024)
f.write(data)
f.close()
