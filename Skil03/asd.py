with open("ord.txt", "r", encoding="ISO-8859-1") as f:
    skra = f.read()
    skra = skra.split("\n")



ord = "vatn"
ord2 = ""

stafalisti = ["a", "v", "s"]

for x in ord:
    if x in stafalisti:
        for i in stafalisti:
            if x == i:
                ord2 += x + " "
    else:
        ord2 += "_ "

print(ord2)
