try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    result = num1/num2
    print(result)

except (ValueError,ZeroDivisionError):
    print("You have entered incorrect input")

finally:
    print("Thanks!")