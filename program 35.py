from random import randint

for x in range( 1, 5) :
 guessNumber = int(input("Enter your guess between 1 to 5 : "))
 randomNumber = randint(1,6)

 if guessNumber == randomNumber :
    print("You have won")
 else :
    print("you have lose")

 print("randomNumber was : ", randomNumber)