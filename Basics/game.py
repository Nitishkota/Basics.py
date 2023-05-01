import random
upper = 10
lower = 1
guessed = random.randint(lower,upper)
guess = 0
while  guessed != guess:
    guess = int(input("Enter a number"))
    if guess == 0:
        print("thanks you are given up")
        break
    elif guess > guessed:
        print("The number is too large")
    elif guess<guessed:
        print("The number is too small")
    else:
        print("You won")