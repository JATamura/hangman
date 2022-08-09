# Hangman Project Documentation

> AiCore project documentation for creating a text based replication of the game hangman where the user tries to guess a word, letter by letter, within 5 mistakes. Built using Python, Github, and ran in command line.

## Milestone 1: Set up the environment

- The hangman project was programmed in Python, making it easy to  use object oriented programming to create a class of the game. This allowed steps of the game (choosing a word, guessing a letter, and checking said letter) to be separated into different functions to be called when necessary. Github was also used to save and share the progress.

```python
class Hangman:

    def __init__(self, word_list, num_lives=5):

    def check_letter(self, letter) -> None:    
        
    def ask_letter(self):
```

## Milestone 2: Ask the user for an input
- As the choosing of the word was given, the first task was to get the user to input a letter they would want to guess. A while loop using a String to track the guess was used to iteratively get the user to keep guessing until a **alphabetic single letter that hasn't been guessed before** was given.

```python
def ask_letter(self):
    letter = ""
    while letter == "" :
        guess = input("Enter a letter you would like to guess: ")
        if guess.lower() not in self.list_letters:
            self.list_letters.append(guess.lower())
            letter = guess
        else:
            print("Please, enter just one character")
    print("You guessed " + letter.lower())
    pass
```

- In the while loop, it would check the condition above using an if statementthat would check if it was a single letter that was in the alphabet. Errors would keep the while loop going, printing *"Please, enter just one character"* before asking for another input. If it was a valid guess, it would print *"You guessed {letter}"*.

> Case 1: No error
> ```
> Enter a letter you would like to guess: a
> You guessed: a
> ```

> Case 2: Error
> ```
> Enter a letter you would like to guess: '
> Please, enter just one character
> ```

## Milestone 3: Define the initialiser 

- The next step was to initialise the class so it contained all the values needed for a single game of hangman. These were given in the docstring of the class. A random word from a list was chosen for the word to be guessed. A for loop was used to create a list of each letter in said word replaced with the character '_'. The set() and len() functions were used to select and count all the unique letters in the chosen word respectively. The number of guessed letters were intialized as an empty list.

```python
def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ["_" for w in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.list_letters = []
    pass
```

## Milestone 4: Complete the 'ask_letter' method

- After initilising the class, the ask_letter method could be updated to check for prior letters guessed. An additional if statement was added to check if the guessed letter was in the list_letters list. If not, it would be added into the list and the while loop would end like before. Instead of printing a message, the method was also updated to run the check_letter method using the guessed letter as the parameter.

```python
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
```

> Case 1: Error
> ```
> Enter a letter you would like to guess: a
> Enter a letter you would like to guess: A
> a was already tried
> ```

- The check_letter method uses an if statement to check if the inputted letter was in the chosen word. The lower() function was used to account for higher and lower case letters. 

- If the letter was in the word, a for loop was used to look through each letter of the word, replacing each corresponding value in the word_guessed list with the letter. It would then reduce 1 from the num_letters list and also print *"Nice! {letter} is in the word!"* followed by the word_guessed list.

- If the letter was not in the word, it would reduce the number of lives by 1 nd print *"Sorry {letter} in not in the word."* followed by *"You have {number of lives} lives left."*.

```python
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
        print("You have " + str(self.num_lives) + " left.")
    pass
```

> Case 1: 2 rounds of hangman (word = banana)
> ```
> Enter a letter you would like to guess: a
> Nice! a is in the word!       
> ['_', 'a', '_', 'a', '_', 'a']
> Enter a letter you would like to guess: f
> Sorry, f is not in the word.
> You have 4 lives left.
> ```

## Milestone 5: Putting it all togehter

- To complete the game, the fundamental logic of guessing until the word is fully guessed or the user reaches 0 lives. To do this, the play_game method was used. It would take in a list of words to randomly choose a word from and initialise the hangman game. A while loop was then used to continuously ask the user to input a letter until the conditions above were met. If the user correctly guessed the word, it would print *"Congratulations you won!"* while if they ran out of lives it would print *"You ran out of lives. The word was {word}"*.

```python
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()
    if game.num_letters == 0:
        print("Congratulations you won!")
    else:
        print("You ran out of lives. The word was " + game.word)
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
```

- In order to add realism to the game, a simple text based image was used to replicate a hanged man that would typically be drawn in a normal game of hangman. This method, hang_the_man, used simple if statements to check how many lives the user had and displayed the correct parts of the body accordingly.

> Case 1: Game win
> ```
> Enter a letter you would like to guess: g
> Nice! g is in the word!
> ['o', 'r', 'a', 'n', 'g', '_']
>   ________
>   |      |
>   |      O
>   |      +
>   |      |
>   |      |
>   |
>   |
> __|__
> Enter a letter you would like to guess: e
> Nice! e is in the word!
> ['o', 'r', 'a', 'n', 'g', 'e']
>   ________
>   |      |
>   |      O
>   |      +
>   |      |
>   |      |
>   |
>   |
> __|__
> Congratulations you won!
> ```

> Case 2: Game loss
> ```
> Enter a letter you would like to guess: b
> Sorry, b is not in the word.
> You have 1 lives left.
>   ________
>   |      |
>   |      O
>   |     -+-
>   |    / | \
>   |      |
>   |     /
>   |    /
> __|__
> Enter a letter you would like to guess: r
> Nice! r is in the word!
> ['_', 'e', '_', 'r']
>   ________
>   |      |
>   |      O
>   |     -+-
>   |    / | \
>   |      |
>   |     /
>   |    /
> __|__
> Enter a letter you would like to guess: m
> Sorry, m is not in the word.
> You have 0 lives left.
>   ________
>   |      |
>   |      O
>   |     -+-
>   |    / | \
>   |      |
>   |     / \
>   |    /   \
> __|__
> You ran out of lives. The word was pear
> ```

## Conclusion

This was a great introductory project into Python and object oriented programming in general as it allowed for the use of a variety of basic functions while also presenting a good challenge. In the future, a fully functional graphic user interface would make the game more interactive. In addition, having a second player input a word they have thought of would make the game authentic to a real hangman experience. It would also be useful to be able to see what letters the user has guessed in the past. 
