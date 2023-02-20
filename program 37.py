
NumberOfLetter = 0
NumberOfDigits = 0
NumberOfWord = 0

text = input("Enter a text of numbers : ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        NumberOfLetter = NumberOfLetter + 1

    elif x >= '0' and x <= '9':
        NumberOfDigits = NumberOfDigits + 1

    elif x == ' ':
        NumberOfWord = NumberOfWord + 1

print("Number of letter : ", NumberOfLetter)
print("Number of digits : ", NumberOfDigits)
print("Number of word : ", NumberOfWord)

