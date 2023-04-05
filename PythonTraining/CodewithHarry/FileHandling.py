s = "Naresh is good boy"

with open("test.txt", "w") as g:
    g.write(s)

with open("naresh.txt", "r") as k:
    s = k.read()
    print(s)
