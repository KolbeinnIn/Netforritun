# Kolbeinn Ingólfsson
# Skilaverkefni 4


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#dæmi 1 og 2
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024).decode()
    count = len(data)
    if len(data) > 3000:
        data = data[:3000]
    if len(data) < 1:
        break
    print(data)
    print("fjöldi stafa:", count)


mysock.close()

#Dæmi 3
