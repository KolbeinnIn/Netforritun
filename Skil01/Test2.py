from os import listdir
import os
from os.path import isfile, join
from re import *

onlyfiles = [f for f in listdir("./") if (isfile(join("./", f)) and match(".*.txt", f))]

print(onlyfiles)

osCommandString = "notepad.exe smakokur.txt"
os.system(osCommandString)



    




