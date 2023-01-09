marks = [20, 60, 40, 50, 77, 98, 30]

for index, mark in enumerate(marks):
    print(mark)
    if index == 5:
        print("Naresh you got 98 marks")

for index, mark in enumerate(marks, 1):
    print(mark)
    if index == 5:
        print("Naresh you got 98 marks")
