try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    result = num1/num2
    print(result)

except ValueError:
    print("You have to insert only integer")
except ZeroDivisionError:
    print("You can not divide a number by 0")

finally:
    print("Thanks!")