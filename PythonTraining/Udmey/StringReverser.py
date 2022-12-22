user_string = input("Please enter a string.")
reversedString = ""

for item in range(len(user_string) - 1, -1, -1):
    reversedString += user_string[item]

print(reversedString)