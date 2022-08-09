
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for w in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []
        pass

    def check_letter(self, letter) -> None:
        if (letter.lower() in self.word):
            index = 0
            for w in self.word:
                if w == letter.lower():
                    self.word_guessed[index] = letter.lower()
                index += 1
            self.num_letters -= 1
            print("Nice! " + letter.lower() + " is in the word!")
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print("Sorry, " + letter.lower() + " is not in the word.")
            print("You have " + str(self.num_lives) + " lives left.")
        pass

    def ask_letter(self):
        letter = ""
        while letter == "" :
            guess = input("Enter a letter you would like to guess: ")
            if len(guess) == 1 and guess.isalpha():
                if guess.lower() not in self.list_letters:
                    self.list_letters.append(guess.lower())
                    letter = guess
                else:
                    print(guess.lower() + " was already tried")
            else:
                print("Please, enter just one character")
        self.check_letter(letter)
        pass

    def hang_the_man(self):
        print("  ________")
        print("  |      |")

        if self.num_lives < 5:
            print("  |      O")
        else:
            print("  |")

        if self.num_lives < 3:
            print("  |     -+-")
        elif self.num_lives < 4:
            print("  |     -+")
        elif self.num_lives < 5:
            print("  |      +")
        else:
            print("  |")

        if self.num_lives < 3:
            print("  |    / | \\")
        elif self.num_lives < 4:
            print("  |    / |")
        elif self.num_lives < 5:
            print("  |      |")
        else:
            print("  |")

        if self.num_lives < 5:
            print("  |      |")
        else:
            print("  |")

        if self.num_lives < 1:
            print("  |     / \\")
        elif self.num_lives < 2:
            print("  |     /")
        else:
            print("  |")

        if self.num_lives < 1:
            print("  |    /   \\")
        elif self.num_lives < 2:
            print("  |    /")
        else:
            print("  |")

        print("__|__")

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()
        game.hang_the_man()
    if game.num_letters == 0:
        print("Congratulations you won!")
    else:
        print("You ran out of lives. The word was " + game.word)
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
