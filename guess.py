print("welcome to mark's guessing game!")

import random

top_of_range = input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

if top_of_range <= 0:
    print('type a number larger than 0 next time')
    quit()
else:
    print('type a larger number than 0 next time')
    quit()

random_number = random.randint(0, random_number )

while true:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess == random_number:
            print("you got it!")
            continue
        else:
            print("you are wrong!")
            break
