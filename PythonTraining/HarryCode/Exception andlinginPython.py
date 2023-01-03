a = input("Enter the Number : ")

print(f"Multiplication of {a} is :")

try:
    for i in range(1, 11):
        print(f"{int(a)} * {i} = {int(a) * i}")

except Exception as e:
    print(e)


print("Some Imp Line Code")

