with open("ord.txt", "r", encoding="ISO-8859-1") as f:
    skra = f.read()
    skra = skra.split("\n")



asd = ["b", "s", "n"]

ord = "vatn"
for x in asd:
    print(x)
    for i in ord:
        if i != x:
            ord = ord.replace(i, "_")
            break

#ord = ord.replace(" ", "")


print(ord)
