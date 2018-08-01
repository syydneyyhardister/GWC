
def display(word, already_guessed_letters):
    new_str = ""
    for letter in word:
        if letter in already_guessed_letters:
            new_str += letter
        elif letter == " ":
            new_str += "  "
            # the letter in our phrase has not been guessed yet
        else:
            new_str += "_ "
    return new_str

def main():
    print_beginning_of_game()

    phrase = "turtles are cool"

    #Keep track of user's guesses
    guessed_letters = []
    game_over = False


    beginning = display(phrase, guessed_letters)
    print(beginning)

    while game_over != True:
#Allow user to give input to computer
        guess = input("Enter a letter: ")
    #Tell the user if they get the right letters
        #Add the good letter to the good letter list
        if guess in phrase:
            print("You got a letter: {}".format(guess))

        else:
            print("{} is not in the phrase".format(guess))

    guessed_letters.append(guess)

    wakeup = display(phrase, guessed_letters)
    print(wakeup)

    if "_" in display:
        game_over = False
    else:
        game_over = True
print("END OF GAME")#Tell the user if they get the wrong letters
    #Add the bad letter to the bad letter list
if __name__ == "__main__":
    main()
#End game if the user gets all the right letters in the word/phrase
