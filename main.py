import random

word_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
word_list = [element.lower() for element in word_list]
'''
Set up the game
'''
# randomly choose a word from the word_list and assign it to a variable
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)

# establish a comparison list
winning = list(chosen_word.strip())

# establish a prompt for the length of the word with spaces
prompt = ['_' for n in chosen_word]

# Game in play
print("Guess the state name!")
chances = ['1', '2', '3', '4', '5', '6']
while prompt != winning:
    '''
    Check to see if the letter in the random word?
    If true, replace the guessed letter in the prompt
    '''
    print(f"You have {chances[-1]} chances left!\n")
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            prompt[position] = guess
    
    if guess not in chosen_word:
        chances.pop()
    
    print(prompt)

    if len(chances) < 1:
        break

if len(chances) < 1:
    print('\nYou Lost!')
else: print('\nYou Won!')