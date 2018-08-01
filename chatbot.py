# --- Define your functions below! ---
def Intro():
    print("Hello! Welcome to the chatbot!")
def greeting():
    print("Let's have a deep conversation")
    p = input("Would you like to hear a poem?")
    print("You're going to hear one anyway")
    poem()
def dating():
    print("I am 105 years old. I am a Fashion Nova Instagram Model in my free time.")
    print("During the day, I am a cereal killer. At night I am Batman.")
    rep = input("Soooo, come here often?")
    print("I was talking with your cousin >;)")
def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False
def joke():
    k = input("Knock Knock")
    n = input("Nana")
    b = input("Nana business")
def art():
    print("""
          _____                    _____                _____ \n
         /\    \                  /\    \              /\    \ \n
        /::\    \                /::\    \            /::\    \ \n
       /::::\    \              /::::\    \           \:::\    \ \n
      /::::::\    \            /::::::\    \           \:::\    \ \n
     /:::/\:::\    \          /:::/\:::\    \           \:::\    \ \n
    /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \ \n
   /::::\   \:::\    \      /::::\   \:::\    \          /::::\    \ \n
  /::::::\   \:::\    \    /::::::\   \:::\    \        /::::::\    \ \n
 /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\      /:::/\:::\    \ \n
/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |    /:::/  \:::\____\ \n
\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|   /:::/    \::/    /\n
 \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /   /:::/    / \/____/ \n
          \::::::/    /         |:::::::::/    /   /:::/    / \n
           \::::/    /          |::|\::::/    /   /:::/    /\n
           /:::/    /           |::| \::/____/    \::/    /\n
          /:::/    /            |::|  ~|           \/____/\n
         /:::/    /             |::|   | \n
        /:::/    /              \::|   | \n
        \::/    /                \:|   | \n
         \/____/                  \|___| \n

                                                                       """)
def poem():
    print("Roses are red,\n pizza sauce is too,\n I ordered a large,\n and none of it is for you!")
# --- Put your main program below! ---
def main():
    valid_input = ['Hi!', 'Hello ;)', 'love me', 'Come here often?', 'I need a partner in crime', 'art', 'draw pls', 'I like to paint', 'joke', 'haha', 'funny']
    Intro()
    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input) :
            if answer == "Hi!":
                greeting()
            elif answer in  ['Hello ;)','love me','Come here often?','I need a partner in crime']:
                dating()
            elif answer in ['art', 'draw pls', 'I like to paint']:
                art()
            elif answer in ['joke', 'haha', 'funny']:
                joke()
        else:
            print("These are the inputs I understand: ")
            for vi in valid_input:
                print(vi)
            print("...I don't understand anything else")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
