# Open File
f = open(r'C:\Users\Naresh Chauhan\PycharmProjects\pythonProject\PythonTraining\name.txt')

while True:
    line = f.readline()
    if not line:
        break
    print(line)
