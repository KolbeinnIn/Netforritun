import socket

#HOST = socket.gethostname()
HOST = '10.220.226.55'
PORT = 12345

#with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
s = socket.socket()
s.connect((HOST,PORT))
#s.sendall('Hello, World')
#data = s.recv(1024)
#print(data)
#s.send(b'au')
f = open('b.txt','wb')
data = s.recv(1024)
f.write(data)
f.close()
#print('Recived', repr(data))
