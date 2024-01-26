import random
import hangman_art as h_art
import hangman_words as h_words
import os



choose_word = random.choice(h_words.word_list)
game_over = False
lives = 6

display = []
for i in range(len(choose_word)):
  display.append('_')

def output():
  os.system('clear')
  print(h_art.logo)
  print(h_art.stages[lives])


while lives > 0 and not game_over:
  output()
  print(display)

  guess = input("Guess a letter: ").lower()
  num_guess_matched = 0

  if guess in display:
      print(f"You've already guessed {guess}.")

  for position in range(len(choose_word)):

    if (guess == choose_word[position]):
      display[position] = guess
      num_guess_matched += 1

# Check if player lost
  if num_guess_matched == 0:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
  if lives == 0:
    output()
    print("You lost")

# Check if player won
  if '_' not in display:
    print(display)
    print("Congratulations! You Won")
    game_over = True
