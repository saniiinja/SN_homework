
import random

secret_number = random.randrange(1, 10) #OR random.randint
print(secret_number)

user_guess = int(input("Guess the number between 1 and 30: "))

if user_guess == secret_number:
    print("Way to go, braniac! The secret number is " + str(secret_number) + " :)!")
else:
    print("Try again. The secret number is not " + str(user_guess) + " :(.")
