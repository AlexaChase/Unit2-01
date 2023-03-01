print("Hello, World!")
username = input("What is your name?")
print("Nice to meet you,", username)
import random
secretNumber = random.randint(1, 100)
print("I'm thinking of a number between 1 and 10...")
while True:
    guess = int(input("What is your guess? "))
    if (guess == secretNumber):
        break
    if (guess > secretNumber):
        print("Sorry, your guess is too high.")
    if (guess < secretNumber):
        print("Sorry, your guess is too low.")
print("You got it!")