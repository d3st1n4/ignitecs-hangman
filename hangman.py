print("\033c")

# Graphics representing the hangman stages
# Each stage corresponds to the number of incorrect guesses
# Students may copy this variable to their own code
graphic = [
            """
                +-------+
                |
                |
                |
                |
                |
             ==============
            """
                ,
            """
                +-------+
                |       |
                |       O
                |
                |
                |
             ==============
            """
                ,
            """
                +-------+
                |       |
                |       O
                |       |
                |
                |
             ==============
            """
                ,
            """
                +-------+
                |       |
                |       O
                |      -|
                |
                |
             ==============
            """
                ,
            """
                +-------+
                |       |
                |       O
                |      -|-
                |
                |
             ==============
            """
                ,
            """
                +-------+
                |       |
                |       O
                |      -|-
                |      /
                |
             ==============
            """
                ,
            """
                +-------+
                |       |
                |       O
                |      -|-
                |      / \ 
                |
             ==============
           
           
            """]  
           
# Function to check if the user has won
def win(user_list, guess_list):
    if guess_list == user_list:
        return True
    else:
        return False

# Function to check if the user has lost
def lose(incorrect_guesses, current_incguesses):
    if current_incguesses == incorrect_guesses:
        return True
    else:
        return False

# Main function for the Hangman game
def hangman():
    user_list = [] # list for user selected word
    guess_list = [] # list of user guessed characters
    incorrect_guesses = 6 # maximum incorrect guesses allowed
    current_incguesses = 0 # counter for incorrect guesses
    user_word = input("Please enter a word: ")
    print("\033c")
   
    # Converts each character in user_word to a list of dashes
    for char in user_word:
        user_list.append(char)
    for char in user_word:
        guess_list.append("_")
    print(guess_list)
   
    # Loops through the game until the user either wins or loses
    while current_incguesses < incorrect_guesses:
        user_guess = input("Guess a character: ")
        print("\033c")

        # Ensures that user guesses each character only once
        if user_guess in guess_list:
            print(f"You already guessed '{user_guess}'. Try again.")
            continue

        # Checks that the user's guessed character is valid and populates guess_list with correct guess
        if user_guess in user_list:
            for idx, letter in enumerate(user_word):
                if user_guess == letter:
                    guess_list[idx] = letter

        # Otherwise, increments the number of incorrect guesses and updates the graphic
        else:
            current_incguesses += 1
            print(graphic[current_incguesses])
            print(f"Incorrect guesses: {current_incguesses}")

        print(guess_list)
   
    # Checks for win or lose conditions
        if win(user_list, guess_list):
            print(f"You won! The word was: {user_word}")
            break
    
    if lose(incorrect_guesses, current_incguesses):
        print(f"You lost! The word was: {user_word}")

hangman()
