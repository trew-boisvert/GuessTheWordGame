import random

def is_guess_correct(guess):

def UFO():
    words = ["apple", "berry", "cherry", "blave"]
    chosen_word = random.choice(words)
    used_letters = []
    wrong_guesses = 0

    board = chosen_word
    for i in range(len(board)):
        board = board[0:i] + "_" + board[i+1:]
    print(" ".join(board))

    while board != chosen_word:
        if wrong_guesses >= 6:
            return "Oh no, you lost!"
        
        guess = input("Please guess a letter in the codeword:  ")
        guess = guess.lower()

        if guess in used_letters:
            print("Invalid Input: You already guessed that.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Invalid Input: Please only choose letters.')
        else:
            used_letters.extend(guess)
            print(f"Letters Used: {used_letters}")

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    board = board[0:i] + guess + board[i+1:]
        else:
            wrong_guesses +=1
            
        print(board)
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
    print('Invaders from outer space have arrived and are abducting humans using tractor beams.  Earn your medal of honor by cracking the codeword to stop the abduction!')
    print()
    print('How to play:')
    print()
    print('Guess one letter at a time of a codeword represented by blank placeholders for each letter. If the letter does not exist in the codeword, the person is pulled in closer to the UFO by the tractor beam. If the letter exists, the blanks that correspond to the position of those letters in the codeword are replaced by the letter. If all the letters of the codeword are revealed before the person is pulled into the UFO, you win. Otherwise, the UFO abducts the person and you lose.')
    print()

    UFO()
    replay()


game()
