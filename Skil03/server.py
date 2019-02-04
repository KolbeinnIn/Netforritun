import pickle
import socket
from random import *
from os import listdir
from os.path import isfile, join
from re import *

HOST = socket.gethostname()
PORT = 12345

s = socket.socket()
s.bind((HOST,PORT))
s.listen(2)
with open ("ord.txt","r",encoding="ISO-8859-1") as f:
    skra=f.read().split("\n")

stafalisti = []

while True:
    c, addr = s.accept()
    ord=skra[randint(0,len(skra)-1)]
    ord1=""
    print(ord)
    for x in range(len(ord)):
        ord1=ord1+"_ "
    c.send(ord1.encode())
    buinn=False
    lif=5
    while lif>0 or buinn==False:
        ord2=""
        staf=pickle.loads(c.recv(1024))
        staf = staf.lower()
        if staf not in stafalisti:
            stafalisti.append(staf)
            if staf not in ord:
                lif-=1
        print(stafalisti)
        for x in ord:
            if x in stafalisti:
                for i in stafalisti:
                    if x == i:
                        ord2 += x + " "
            else:
                ord2 += "_ "
        if ord==ord2.replace(" ", ""):
            print("U von")
            lif=6
            c.send(str(lif).encode())
            c.send(ord2.encode())
            break

        c.send(str(lif).encode())
        if lif==0:
            c.send(ord.encode())
            break
        else:
            c.send(ord2.encode())
        print(ord2)
    stafalisti = []
