# Ágúst, Bjarki, Kolbeinn
# Skilaverkefni 4


import socket
import urllib.request as req
import urllib.parse as p

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

response = True
request = True
while response:
    url = input("Sláðu inn vefslóð: ")
    try:
        request = req.Request(url)
        print(request.host)
        response = req.urlopen(request)
        print(request.full_url)
        print(request.get_method())
        print(request.type)
        break

    except:
        print("URL ekki rétt, reyndu aftur")

mysock.connect((request.host, 80))
print("__________________")
#dæmi 1 og 2
#url = input("Sláðu inn vefslóð: ")
cmd = ('%s %s %s/1.0\r\n\r\n' % (request.get_method().upper(),request.full_url, request.type.upper())).encode()
mysock.send(cmd)
print("Dæmi 1 og 2")
fjStafa = 3000
while True:
    data = mysock.recv(1024).decode()
    count = len(data)
    if len(data) > fjStafa:
        fjoldi = fjStafa - count
        count -= len(data) - len(data[:fjoldi])  # ef of margir stafir eru í fhand þá eru auka stafirnir dregnir frá teljaranum sést ef fjStafa2 er 533
        data = data[:fjoldi]
    if len(data) < 1:
        break
    print(data, end="")
    print("\nfjöldi stafa:", count)


mysock.close()

#Dæmi 3
print("\nDæmi 3")
fhand = req.urlopen('http://data.pr4e.org/romeo.txt')
teljari = 0
fjStafa2 = 3000
for line in fhand:
    line = line.decode().strip()
    teljari += len(line)
    if teljari > fjStafa2:
        fjoldi2 = fjStafa2 - teljari
        teljari -= len(line) - len(line[:fjoldi2]) #ef of margir stafir eru í fhand þá eru auka stafirnir dregnir frá teljaranum. sést ef fjStafa2 er 160
        line = line[:fjoldi2]
        print(line)
        break
    else:
        print(line)

print("fjöldi stafa:", teljari)


