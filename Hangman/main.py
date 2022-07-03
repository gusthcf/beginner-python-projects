import random
from hangmanArt import stages
from hangmanArt import logo
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo)
lives = 6
display = []
for _ in range(word_length):
    display += "_"
while '_' in display:
    print(f"{' '.join(display)}")
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print('You already guessed this letter my friend!')
    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        print(
            f"You missed! Doesn't have the letter {guess} in the word. You lose a life."
        )
        lives -= 1
        print(f'Remaining lives: {lives}')
    if lives == 0:
        print(f"{' '.join(display)}{stages[0]}\nYou were hanged!!!!")
        break
    if not '_' in display:
        print(f"{' '.join(display)}")
        print('You win!!!')
