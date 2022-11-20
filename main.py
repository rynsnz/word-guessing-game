import random
word_list = ["dog", "cat", "horse"]

# randomly choose a word from the word_list and assign it to a variable
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)

# Ask the user to guess a letter and assign their answer to a variable
guess = input("Guess a letter: ").lower()

# is the letter in the random word?
# guess in chosen_word
for letter in chosen_word:
    if letter in guess:
        print("Right")
    else:
        print("Wrong")