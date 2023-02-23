
num1 ={1, 2,3,4,5,5,6}
num2 = set([2,3,4,5])
num2.add(7)
num2.remove(5)

print(num2)
print(7 in num1)

print(num1 & num2)
print(num1 | num2)
print(num1 - num2)