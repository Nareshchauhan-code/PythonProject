def average(a, b, n):
    print("The Average of numbers is :", (a + b) / n)


average(10, 10, 2)


# default argument

def average(a=10, b=10, n=2):
    print("The Average of numbers is :", (a + b) / n)


average()


# Return Function

def average(a, b, n):
    return ((a + b) / n)


c = average(50, 50, 2)
print(c)
