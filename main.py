from random import *


with open(file="words.txt", mode="r") as data:
    list_words = [word.rstrip('\n') for word in data]

random_word = choice(list_words)
print(random_word)

len_word = len(random_word)
life = 6
display = ["_" for _ in range(len_word)]

num_blank = len(display)
game_is_on = "_" in display

while game_is_on:
    print(display)
    chosen_letter = input("Guess a letter: ").lower()

    for position in range(len_word):
        letter = random_word[position]
        if letter == chosen_letter:
            display[position] = letter
    if chosen_letter not in random_word:
        life -=1

    if life == 0:
        game_is_on = False
    print(life)
