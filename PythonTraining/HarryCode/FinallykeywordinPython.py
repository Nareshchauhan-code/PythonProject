def func():
    try:
        l = [1, 3, 5, 67, 8]

        i = int(input("Enter the Index: "))
        print(l[i])
        return 1
    except:
        print("Some Error accord")
        return 0
    finally:
        print("I am always executed")


x = func()
print(x)
