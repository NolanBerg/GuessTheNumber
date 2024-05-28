import random 

maxval = input("Enter a number for the high end value: ")

if maxval.isdigit():
    maxval = int(maxval)
else:
    print("The value entered must be a NUMBER that's greater than 0... RESTART")
    quit()

randnum = random.randint(1, maxval)
totalguesses = 0

while True:
    totalguesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit(): 
        if int(guess) == randnum:
            print(f"Correct! The random number was {randnum}.")
            break
        elif int(guess) > randnum:
            print("Your guess is too high...")
        else:
            print("Your guess is too small...")
    else:
        print(f"Your guess must be an integer between 1 and {maxval}.")

print(f"Total Guesses: {totalguesses}")