dic = {"Name": "Naresh", "Age": 10}

print(dic["Name"])
print(dic.get("Name"))

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])


print(dic.items())
