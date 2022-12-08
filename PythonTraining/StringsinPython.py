name = "Naresh"

print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[5])
# print(name[6]) # Throw an error IndexError: string index out of range


fullName = """Thousands of Ukrainians have fled to European
 nations since the Russian invasion in February. Unlike African 
 or Middle Eastern refugees, Ukrainian ones have received a warm reception, revealing a deeply..."""

print(fullName.upper())
print(fullName[3])

for character in fullName:
    print(character)
