
import socket
import sys
import time
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes



while True:
    tm = s.recv(1024)
    sys.stdout.write('\r' + 'The time got from the server is: ' + str(tm.decode("ascii")))
    #print("\rTime:", tm.decode("ascii"), end="\b")
    #sys.stdout.flush()


