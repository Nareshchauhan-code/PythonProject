listMethods = [1, 10, 23, 2, 5, 2]
print(listMethods)

listMethods.append(100)
print(listMethods)

listMethods.sort()
print(listMethods)

listMethods.sort(reverse=True)
print(listMethods)

listMethods.reverse()
print(listMethods)

print(listMethods.index(2))

print(listMethods.count(2))
# Copy method
m = listMethods.copy()
m[0] = 1200
print(m)

# extend method

s = [100, 200, 300, 400]

listMethods.extend(m)
print(listMethods)
