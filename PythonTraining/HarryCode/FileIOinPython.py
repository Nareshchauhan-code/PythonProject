# Open File
f = open(r'C:\Users\Naresh Chauhan\PycharmProjects\pythonProject\PythonTraining\name.txt')
print(f.read())
f.close()

# Write File

f = open(r'C:\Users\Naresh Chauhan\PycharmProjects\pythonProject\PythonTraining\python.txt', 'w')
print(f.write("Hello world"))
f.close()

# Append File

f = open(r'C:\Users\Naresh Chauhan\PycharmProjects\pythonProject\PythonTraining\python1.txt', 'a')
print(f.write("Hello world"))
f.close()
