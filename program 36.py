n = input("Enter text number : ")
# 10 20 30 40

list = n.split()
sum = 0
for num in list:
    sum = sum + int (num)
    print(sum)