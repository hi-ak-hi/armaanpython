from random import randint
import guessing_game
random_num = randint(1, 1_000_000)
def check(question):
    while True:
        global guess
        guess = input(question)
        try:
            guess = guess.replace(",", "")
            guess = int(guess)
        except:
            print("enter a number please")
            continue
        break

check("Guess a number between 1 and 1,000,000: ")
while guess != random_num:
    if guess>random_num:
        print("guess lower")
    if guess<random_num:
        print("guess heigher")
    guess = input("> ")
    check("> ")
print("good job, you got it")

if __name__ == "__main__":
    guessing_game.py