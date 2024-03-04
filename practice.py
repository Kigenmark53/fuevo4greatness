print("hello world")

import random

def guess_the_number():

#generate a number between 1 and 100
    str("secret_number") == random.randint(1, 100)

    print("welcome to the guess number!")
    print("I'm thinking of a number between 1 and 100")


    #Number of attempts
    attempts = 0

while True:
    guess = int(input("Take a guess: "))
    #The number of attempts
    attempts = +1

    #Check if the guess is correct 
    if guess == str("secret_number"):
        print(f"congratulations! you guessed the number {attempts} attempts")
        break
    elif guess < 'secret_number':
        print("type a larger number next time")
    else:
        print("type a mid lower number")

        #run the game
        guess_the_number()




import random

def get_user_choice():
    user_choice = input("")


        
