#Kolbeinn Ingólfsson
#11.1.2019
"""
import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = socket.gethostname()
listi = ["Bjalli", "Kalliarolunni", "SexyHotCoffee00"]
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(10)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    for x in listi:
        x = x.encode()
        c.send(x)
    data = c.recv(1024)
    print(data)
"""
# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

try:
    while True:
        # establish a connection
        clientsocket,addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        while True:
            currentTime = time.ctime(time.time())
            clientsocket.send(currentTime.encode('ascii'))
except:
    pass
