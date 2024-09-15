def print_body(stage):
    if stage == 1:
        print(r'''
--------
|      |
|      
|     
|      
|     
-
''')
    if stage == 2:
        print(r'''
--------
|      |
|      O
|      
|      
|     
-
''')
    if stage == 3:
        print(r'''
--------
|      |
|      O
|     \|
|      
|     
-

''')
    if stage == 4:
        print(r'''
--------
|      |
|      O
|     \|/
|      
|     
-

''')
    if stage == 5:
        print(r'''
--------
|      |
|      O
|     \|/
|      |
|     
-
''')
    if stage == 6:
        print(r'''
--------
|      |
|      O
|     \|/
|      |
|     /
-
''')
    if stage == 7:
        print(r'''
YOU FAILED!!!!!
--------
|      |
|      O
|     \|/
|      |
|     / \
-
RIP!!!!
''')
        print("The word was", word)
        quit()

from wonderwords import RandomWord
word = RandomWord()

word = word.word()
word = word.upper()
word = "SIGMA"
word_list = word
word_completion = len(word) * "_"
word_list = list(word_list)
word_completion =list(word_completion)
words_guessed= []
stage = 1
ending = 1
while True:
    if list(word) == word_completion:
        break
    print_body(stage)
    print("--------Word--------")
    for x in word_completion:
        if ending != len(word):
            print(x, end=" ")
        if ending == len(word):
            print(x)
        ending += 1
    print("--------Leters Guessed--------")
    print(words_guessed)
    guess= input("Guess: ").upper()
    if guess in words_guessed:
        print("You already guessed that")
    elif guess not in words_guessed:
        if guess in word:
            words_guessed.append(guess)
            indices = [i for i, x in enumerate(word_list) if x == guess]
            for index in indices:
                word_completion[index] = guess
        elif guess not in word:
            print("That's not in the word")
            words_guessed.append(guess)
            stage += 1
print("good job, you guesed it!!!")