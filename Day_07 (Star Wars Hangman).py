import random

the_hanged_man = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
YOU LOSE!!!''']

word_list = ['star wars', 'darth maul', 'darth vader', 'the force',
             'luke', 'leia', 'han solo','chewbacca','palpatine',
             'death star', 'yoda', 'tatooine', 'alderaan', 'naboo',
             'jedi', 'sith', 'empire', 'rebellion', 'lightsaber',
             'millenium falcon', 'jar jar binks', 'padawan', 
             'droid', 'pod racing', 'i am your father',
             'stormtrooper', 'jabba the hutt', 'the dark side',
             'ashoka', 'andor', 'i have a bad feeling about this',
             'never tell me the odds', 'i am your father', 
             'may the force be with you', 'a new hope', 
             'the empire strikes back', 'return of the jedi',
             'the phantom menace', 'attack of the clones',
             'the clone wars', 'revenge of the sith', 
             'the force awakens', 'the last jedi', 
             'the rise of skywalker', 'thats no moon', 'ewok',
             'wookie', 'scruffy looking nerf herder', 'hoth,'
             'coruscant', 'mustafar', 'kamino', 'geonosis',
             'dagobah', 'jakku', 'mon calamari', 'admiral ackbar',
             'its a trap', 'anakin', 'padme', 'the senate', 'grogu',
             'mandalore', 'boba fett', 'django fett', 'mandalorian',
             'beskar', 'darth bane', 'mando', 'darth sidious', 
             'younglings', 'moff gideon', 'grand moff tarkin']

play_again = "y"
while play_again == "y":

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

    print(''.join(chosen_word_progress))

    player_choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z']

    tries = 0
    while tries < 7:

        print(player_choices)

        chosen_letter = input("Choose a letter: ")
        chosen_letter = chosen_letter.lower()

        if chosen_letter in player_choices:
            player_choices.remove(chosen_letter)

        for x in range(word_length):
            if chosen_word_list[x] == chosen_letter:
                new_chosen_word_progress[x] = chosen_letter

        if new_chosen_word_progress != chosen_word_progress:
            chosen_word_progress = new_chosen_word_progress[:]

            print(''.join(chosen_word_progress).upper())

            if ''.join(new_chosen_word_progress) == chosen_word:
                print("You win!")
                tries += 10

        else:
            print(the_hanged_man[tries])
            tries += 1
            print(''.join(chosen_word_progress).upper())

    play_again = input("Would you like to play again? y or n: \n")
