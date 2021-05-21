import random

def game():
    print('Invaders from outer space have arrived and are abducting humans using tractor beams.  Earn your medal of honor by cracking the codeword to stop the abduction!')
    print()
    print('How to play:')
    print()
    print('Guess one letter at a time of a codeword represented by blank placeholders for each letter. If the letter does not exist in the codeword, the person is pulled in closer to the UFO by the tractor beam. If the letter exists, the blanks that correspond to the position of those letters in the codeword are replaced by the letter. If all the letters of the codeword are revealed before the person is pulled into the UFO, you win. Otherwise, the UFO abducts the person and you lose.')
    print()

    words = ["apple", "berry", "cherry", "blave"]
    character = "_"
    chosen_word = random.choice(words)
    used_letters = []
    wrong_guesses = 0

    board = chosen_word
    for i in range(len(board)):
        board = board[0:i] + "_" + board[i+1:]
    print(" ".join(board))

    while board != chosen_word:
        guess = input("Please guess a letter in the codeword:  ")
        guess = guess.lower()

        used_letters.extend(guess)
        print(f"Letters Used: {used_letters}")

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                board = board[0:i] + guess + board[i+1:]
        print(board)

game()
