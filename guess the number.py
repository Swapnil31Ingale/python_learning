import random

print("I am thinking of a number between 1 and 20.")
secretGuess = random.randint(1, 20)

for i in range(1, 6):
    print("Take a guess")
    guessTaken=int(input())
    if secretGuess < guessTaken:
        print("Your guess is too high!")
    elif secretGuess > guessTaken:
        print("Your guess is too low!")
    else:
        break

if secretGuess == guessTaken:
    print("Good Job!! You guess the correct number in " + str(secretGuess) +" guessess.")
else:
    print("Nope! The number I was thinking of was " + str(secretGuess) + ".")

