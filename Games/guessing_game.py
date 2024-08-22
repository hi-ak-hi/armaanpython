from random import randint
guess = input("Guess(1 to 1 million): ")
guess = guess.replace(",", "")
guess = int(guess)
random_num = randint(1, 1_000_000)

while int(guess) != random_num:
    if int(guess)>random_num:
        print("guess lower")
    if int(guess)<random_num:
        print("guess heigher")
    guess = input("Guess again: ")
    guess = guess.replace(",", "")
print("good job, you got it")