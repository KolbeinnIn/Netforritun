# Ágúst, Bjarki, Kolbeinn
# Skilaverkefni 4


import socket
import urllib.request


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#dæmi 1 og 2
#url = input("Sláðu inn vefslóð: ")
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
print("Dæmi 1 og 2")
while True:
    data = mysock.recv(1024).decode()
    count = len(data)
    if len(data) > 3000:
        data = data[:3000]
    if len(data) < 1:
        break
    print(data, end="")
    print("fjöldi stafa:", count)


mysock.close()

#Dæmi 3
print("\nDæmi 3")
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
teljari = 0
for line in fhand:
    line = line.decode().strip()
    if teljari > 3000:
        break
    print(line)
    teljari += len(line)


