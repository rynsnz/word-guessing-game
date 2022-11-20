import random
word_list = ["apple", "orange", "banana"]

# randomly choose a word from the word_list and assign it to a variable
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)

# establish a prompt for the length of the word with spaces
prompt = ['_' for n in chosen_word]

# Ask the user to guess a letter and assign their answer to a variable
print(f"Psst... the word is {chosen_word}")

guess = input("Guess a letter: ").lower()

# is the letter in the random word?
# guess in chosen_word

for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
        prompt[position] = guess

print(prompt)