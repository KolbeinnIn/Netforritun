# Ágúst, Bjarki, Kolbeinn
# Skilaverkefni 4


import socket
import urllib.request as req
import urllib.parse as p


print("Dæmi 1 og 2")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

response = True
request = True
while response:
    url = input("Sláðu inn vefslóð: ")
    try:
        request = req.Request(url)
        response = req.urlopen(request)
        break

    except:
        print("URL ekki rétt, reyndu aftur")

#url til að copy-a
#http://data.pr4e.org/romeo.txt
mysock.connect((request.host, 80))


# dæmi 1 og 2
cmd = ('%s %s %s/1.0\r\n\r\n' % (request.get_method().upper(), request.full_url, request.type.upper())).encode()
mysock.send(cmd)


fjStafa = 3000
tel = 0
while True:
    data = mysock.recv(1024).decode()
    if tel == 0:
        data2 = data.split("\n")
        for x in data2:
            if "Content-Length:" in x:
                stafir = int(x.strip("Content-Length: ").strip("\r"))
        tel = 1
    count = len(data)
    if len(data) > fjStafa:
        fjoldi = fjStafa - count
        # ef of margir stafir eru í fhand þá eru auka stafirnir dregnir frá teljaranum sést ef fjStafa2 er 533 sjá línu fyrir neðan
        count -= len(data) - len(data[:fjoldi])
        data = data[:fjoldi]
    if len(data) < 1:
        break
    print(data, end="")
    print("\nfjöldi stafa samtals:", count)
    #ATH! stafir inniheldur líka \n og \r.
    print("fjöldi stafa í skrá:", stafir)


mysock.close()

# Dæmi 3
print("\nDæmi 3")
fhand = req.urlopen(request.full_url)
teljari = 0
fjStafa2 = 3000
for line in fhand:
    line = line.decode().strip()
    teljari += len(line)
    if teljari > fjStafa2:
        fjoldi2 = fjStafa2 - teljari
        # ef of margir stafir eru í fhand þá eru auka stafirnir dregnir frá teljaranum. sést ef fjStafa2 er 160 sjá línu fyrir neðan
        teljari -= len(line) - len(line[:fjoldi2])
        line = line[:fjoldi2]
        print(line)
        break
    else:
        print(line)

print("fjöldi stafa:", teljari)
