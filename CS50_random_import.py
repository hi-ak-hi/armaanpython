#the whole library
import random
#what you need to do if you import the whole library
'''coin_flip = random.choice(["heads","tails"])
print(coin_flip)'''

#spicific
'''from random import choice'''#it means - from library import file

coin_flip=random.choice(["heads","tails"])
print(coin_flip)

random_choice = random.randint(1,10)
print(random_choice)

cards = ["jack","queen","king"]
shuffle_cards=random.shuffle(cards)

for card in cards:
    print(card)