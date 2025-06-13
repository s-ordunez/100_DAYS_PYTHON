import random
from Day_07_ascii_art import (starwars, hangman, the_hanged_man, word_list,
                              vader, alphabet)
play_again = "y"
print(starwars)
print(hangman)
while play_again == "y":

    player_choices = alphabet.copy()
    chosen_word = random.choice(word_list)
    chosen_word_list = []

    for x in chosen_word:
        chosen_word_list += x

    word_length = len(chosen_word)
    chosen_word_progress = []
    new_chosen_word_progress = []

    for x in range(word_length):
        if chosen_word[x] == " ":
            chosen_word_progress.append(" ")
            new_chosen_word_progress.append(" ")
        else:
            chosen_word_progress.append("_")
            new_chosen_word_progress.append("_")

    print("Word to guess: " + ''.join(chosen_word_progress))

    tries = 0
    while tries < 7:

        chosen_letter = input("Choose a letter: ")
        chosen_letter = chosen_letter.lower()

        for x in range(word_length):
            if chosen_word_list[x] == chosen_letter:
                new_chosen_word_progress[x] = chosen_letter

        if new_chosen_word_progress != chosen_word_progress:
            chosen_word_progress = new_chosen_word_progress[:]
            player_choices.remove(chosen_letter)

            print(''.join(chosen_word_progress).upper())

            if ''.join(new_chosen_word_progress) == chosen_word:
                print("You win!")
                tries += 10

        elif chosen_letter not in player_choices:
            if chosen_letter not in chosen_word:
                print(the_hanged_man[tries])
                tries += 1
                print("Hey that's cheating!")
                if tries == 7:
                    print(vader)
                    print("The word was " + ''.join(chosen_word).upper())
            else:
                print("You already chose that.")
        else:
            player_choices.remove(chosen_letter)
            print(the_hanged_man[tries])
            tries += 1
            print(''.join(chosen_word_progress).upper())
            if tries == 7:
                print(vader)
                print("The word was "+''.join(chosen_word).upper())

        print("****************************"+str(7-tries)+"/7 LIVES LEFT****************************")
        print(player_choices)

    play_again = input("Would you like to play again? y or n: \n")
