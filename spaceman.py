import random
import re
import os


GREEN = "\x1B[38;2;0;186;113m"
RED = "\x1B[38;2;244;53;69m"
WHITE = "\x1B[37m"


def clear():
    """
    A function that clears the terminal.

    """
    os.system("cls||clear")


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


def is_word_guessed(secret_word, correct_guesses):
    """
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        correct_guesses (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in correct_guesses, False otherwise
    """
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in correct_guesses:
            return False
    return True


def get_guessed_word(secret_word, correct_guesses):
    """
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        correct_guesses (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    """

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in correct_guesses and underscores for the letters that have not been guessed yet
    guessed_word = ""
    for letter in secret_word:
        if letter in correct_guesses:
            guessed_word += f"{letter} "
        else:
            guessed_word += "_ "
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


def get_guess(all_guesses):
    """
    A function to ask the player for their guess.

    Args:
        all_guesses (string): All the letters the player has guessed so far.

    Returns:
        string: guessed letter. For the letter guess to be valid, it can only be just one letter, and letter cannot have been guessed before.

    """
    if len(all_guesses) > 0:
        print(f"Guesses so far: {' '.join(sorted(all_guesses))}")
    guess = "False"  # :)
    while len(guess) != 1 or not re.match("^[a-zA-Z]", guess) or guess in all_guesses:
        guess = input("\nGuess one letter: > ").lower()
        if guess in all_guesses:
            print("You already guessed that letter.")
    return guess


def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    """

    # show the player information about the game according to the project spec
    print(
        "Welcome to Spaceman\n\nSpaceman is running out of air!\nHe needs to login to his spaceship computer to fix the air flow but he can't remember his password, and he doesn't use a password manager!\nQuick, help him remember his password before he runs out of guesses."
    )
    correct_guesses = ""
    incorrect_guesses = ""
    incorrect_guesses_left = len(secret_word)
    print(
        f"\nGuess one letter at a time.\nYou have {incorrect_guesses_left} guesses to save Spaceman!"
    )
    game_over = False
    while game_over is False:
        # Ask the player to guess one letter per round and check that it is only one letter and letter hasn't been guessed before
        guess = get_guess(correct_guesses + incorrect_guesses)
        clear()
        # Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word) is False:
            print(f"{RED}Failed! Spaceman was counting on you!{WHITE}\n")
            incorrect_guesses += guess
            incorrect_guesses_left -= 1
            if incorrect_guesses_left == 0:
                print("Spaceman! No! Spaceman! Spaceman..? Spaceman...")
                print(
                    f"\nYou notice something under the keyboard...\nA sticky note with a password written on it: {secret_word}"
                )
                return False
        else:
            print(f"{GREEN}Success! There is still hope...{WHITE}\n")
            correct_guesses += guess
        # show the guessed word so far
        print(get_guessed_word(secret_word, correct_guesses))
        # check if the game has been won or lost
        if is_word_guessed(secret_word, correct_guesses) is True:
            print("\nCongratulations! The password worked! You saved Spaceman!")
            game_over = True
        print(f"\nGuesses left: {incorrect_guesses_left}")


def start_game():
    """
    A function that starts the game of spaceman.

    """
    secret_word = load_word()
    spaceman(secret_word)


def play_again():
    """
    A function that checks if the player wants to play again.

    Returns:
        bool: True if the player choice is yes, False otherwise

    """
    player_choice = ""
    while not re.match("^[yn]", player_choice):
        player_choice = input("\nPlay again? (Y/N) > ").lower()
    if player_choice == "y":
        return True
    return False


# These function calls that will start the game

running = True
while running is True:
    clear()
    start_game()
    running = play_again()
    print("\nGame Over")
