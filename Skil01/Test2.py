from os import listdir
from os.path import isfile, join
from re import *

onlyfiles = [f for f in listdir("./") if (isfile(join("./", f)) and match("^[a-zA-Z0-9_ ]*.txt", f))]

print(onlyfiles)
    




