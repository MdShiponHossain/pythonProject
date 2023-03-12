try:
    list = [20, 0, 30]
    result = list[0]/list[1]
    print(result)
    print("Done")

except ZeroDivisionError:
    print("Dividing by zero is not possible")