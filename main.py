import random
word_list = ["dog", "cat", "horse"]

'''
randomly choose a word from the word_list and assign it to a variable
called chosen_word
'''
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

'''
Ask the user to guess a letter and assign their answer to a variable
called guess. Make guess lowercase.
'''
guess = input("Guess a letter: ").lower()

'''
Check if the letter the user guessed (guess) is one of the letters
in the chosen_word
'''
guess in chosen_word