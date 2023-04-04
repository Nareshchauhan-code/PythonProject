value = int(input("Please enter the value: "))

match value:
    case 1:
        print("This is case 1")

    case 2:
        print("This is case 2")
    case 3:
        print("This is case 3")

    case _:
        print("Not found")
