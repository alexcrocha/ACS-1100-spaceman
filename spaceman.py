import random


def load_word():
    """
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    """
    f = open("words.txt", "r")
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(
        " "
    )  # comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    """
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    """

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word


def is_guess_in_word(guess, secret_word):
    """
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    """
    # check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    return False


def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    """

    # TODO: show the player information about the game according to the project spec

    # Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = ''
    game_over = False
    while game_over == False:
        guess = 'False' # :)
        while len(guess) != 1:
            guess = input('Please guess one letter: > ')
        # Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word) == False:
            print("You're out of luck")
        else:
            print('You got it!')
            letters_guessed += guess
        # show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))
        # check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed) == True:
            game_over = True


# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
print(secret_word)

