#TODO: import the random module since you  will need it in your game functions
import random
#TODO: define function guess_the_num
def guess_the_num():
    numb = random.randint(1, 100)
    guess = int(input("Guess a number between 1 - 100"))
    tries = 0
    for tries in range (0,3):
        if guess < numb:
            guess = int(input("Guess higher: "))
        elif guess > numb:
            guess = int(input("Guess lower: "))
        else: continue

    print("The number is {}".format(numb))

#TODO: define function rock_paper_scissors
########### Starter code for Rock Paper Scissors ############
def rock_paper_scissors():
    import random;
    player = input("Enter your choice (rock/paper/scissors): ")
    player = player.lower()
    while (player != "rock" and player != "paper" and player != "scissors"):
        print(player);
        player = input("That choice is not valid. Choose 'rock', 'paper', or 'scissors'")
        player = player.lower()

    computerInt = random.randint(0,2)
    if (computerInt == 0):
        computer = "scissors"
    elif (computerInt == 1):
        computer = "rock";
    elif (computerInt == 2):
        computer = "paper"
    else:
        computer = "What? Error...";
    if player == computer:
        print("Draw!")
    elif (player == "rock"):
        if (computer == "paper"):
            print("Computer Wins")
        else:
            print("You win!")
    elif (player == "paper"):
        if (computer == "rock"):
            print("You Win!")
        else:
            print("Computer wins :(")
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer Wins:(")
        else:
            print("You Win!")

    print("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!")
    input("Enter any key to exit.")
    #TODO: define function madlibs

#TODO: define function riddle
# Starter code for a riddle game
# The user has N tries to guess the answer to a riddle
# After the first attempt, give the user a hint for each attempt



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

def hangman():
    print_beginning_of_game()

    phrase = "girls who code"

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


#End game if the user gets all the right letters in the word/phrase
def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd?")
    if ((computer_value%2) == 0) and (user_input == "even"):
        print("YA DID IT! YOU SO SMORT\n")
    elif ((computer_value%2) != 0) and (user_input == "odd"):
        print("YA DID IT BOII!!!.\n")
    else:
        print("Wrong")
