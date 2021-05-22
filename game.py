import random
from ufo import x, encouragement

with open("nouns.txt", "r") as nouns_list:
    nouns = nouns_list.readlines()
   

def guess_is_correct(guess, word):
    return guess in word

def update_board(guess, word, board):
    for i in range(len(word)):
        if word[i] == guess:
            board = board[0:i] + guess + board[i+1:]
    return board

def UFO():
    words = ["apple", "berry", "cherry", "blave"]
    chosen_word = random.choice(nouns).replace('\n', '').upper()
    used_letters = []
    wrong_guesses = 0

    board = chosen_word
    for i in range(len(board)):
        board = board[0:i] + "_" + board[i+1:]
    print('Codeword: ' + " ".join(board))

    while board != chosen_word:
        if wrong_guesses >= 6:
            print("Oh no, you lost!")
            return
        
        guess = input("Please guess a letter in the codeword:  ")
        guess = guess.upper()

        if len(guess) != 1:
            print('Invalid Input: Please enter one guess at a time.')
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('Invalid Input: Please only choose letters.')
        elif guess in used_letters:
            print("Invalid Input: You already guessed that.")
        else:
            used_letters.extend(guess)
        
        if guess_is_correct(guess, chosen_word):
            board = update_board(guess, chosen_word, board)
            print('That is correct!')
        else:
            wrong_guesses +=1
            print(random.choice(encouragement))
            
        print(x[wrong_guesses])   
        print('Codeword: ' + " ".join(board))
        print(f"Letters Used: {' '.join(used_letters)}")
        print(f"Wrong guesses: {wrong_guesses}")

    print('You win!')

def replay():
    print('Would you like to play again? Y/N')
    play_again = input(">   ")
    play_again = play_again.lower()
    if play_again == "y":
        UFO()
        replay()
    elif play_again == "n":
        print('Thanks for playing!  Goodbye!')
    else:
        print('Invalid Input.  Goodbye.')

def game():
    print(x[0])
    print('Invaders from outer space have arrived and are abducting humans using tractor beams.  Earn your medal of honor by cracking the codeword to stop the abduction!')
    print()
    print('How to play:')
    print()
    print('Guess one letter at a time of a codeword represented by blank placeholders for each letter. If the letter does not exist in the codeword, the person is pulled in closer to the UFO by the tractor beam. If the letter exists, the blanks that correspond to the position of those letters in the codeword are replaced by the letter. If all the letters of the codeword are revealed before the person is pulled into the UFO, you win. Otherwise, the UFO abducts the person and you lose.')
    print()

    UFO()
    replay()

game()
