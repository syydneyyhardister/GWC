start = '''
You're walking one day and as you pass infront of a building you run into a
stranger.'''

print(start)
print("Hey, I'm Peter Parker")
name=input("What's your name?")
print("Hello",name)
type(name)
print("I'm in front of Oscorp. Should I go inside or leave?")
print("Type 'inside' to go inside or 'leave' to leave.")
user_input = input()
if user_input == "inside":
        print("You and Peter decide to go inside and you find yourselves in an empty hallway with two doors.")
        print("The doors are numbered 1 and 2. Peter then turns to you and asks,'Which door should we go into?'")
        print("Type '1' or '2'.")
        user_input = input()
        if user_input == "1":
            print("There is a red spider in the room, and as Peter gets close to it, it bites him and he becomes Spiderman.")
            print("As you both stand in awe at the sight of Peter's new found powers, you hear a scream from outside the building.")
            print("You both rush outside to investigate, and find none other than the Green Goblin. Peter immediately tries to fight Green Goblin, but it's clear he needs help")
            print("Peter looks to you for hope, but you see people dying and you're not sure about that.")
            print("Do you help Peter save the city, or do you run?")
            print("Type 'stay' or 'run'")
            user_input = input()
            if user_input == 'stay':
                print("You've stayed with Peter and are helping to evacuate citizens. Peter is defeating the Green Goblin and it looks like the fight will be over soon.")
                print("You stand there with a smile on your face and give Peter a thumbs up, only to be hit by a bus and DIE!")
                print("THE END")
            elif user_input == 'run':
                print("You ran away from the scene, leaving Peter all alone.")
                print("You later watch the news and realize that everyone died but you.")
                print("THE END")
        elif user_input == "2":
            print("There is a black spider in the room, and as Peter gets close to it, it bites him and he becomes Venom.")
            print("You're paralyzed by fear at the sight of Peter as Venom, and then you hear a scream from outside the building")
            print("You both rush outside to investigate and find none other than the Green Goblin, but as you stand and watch Peter rushes to help Green Goblin in his reign of terror")
            print("No one can stop the combined forces of Green Goblin and Venom, do you run away or join them?")
            print("Type 'run' or 'join'")
            user_input = input()
            if user_input == 'run':
                print("You've chosen to run, but Venom spots you from above the crowd. Angered by your betrayal he targets you in particular.")
                print("Venom covers you in black sludge, and you suffocate to death.")
                print("THE END")
            elif user_input == 'join':
                print("You joined Green Goblin and Venom, and with their supernatural abilities and your devious mind, all three of you conquer the world, killing everything in your paths.")
                print("THE END")
elif user_input == "leave":
        print("You chose to leave and you and Peter walk down to school.")
        print("Mr. Devon, your history teacher, is waiting outside glaring at you and Peter.")
        print("Mr. Devon says, 'Aren't you two supposed to be in class?'")
        print("Type 'yes' or 'no'")
        user_input = input()
        if user_input == 'yes':
            print("You say, 'Yes sir' as you and Peter rush to class.")
            print("You're nearly bored to death during the school day, your only happiness being lunch, and as you walk home, you hear screams and turn around only to see the Green Goblin terrorizing Mr. Devon.")
            print("Do you try to help Mr. Devon or run away?")
            print("Type 'stay' or 'run'")
            user_input = input()
            if user_input == 'stay':
                print("You help free Mr. Devon, but in this act, you yourself are kidnapped by the Green Goblin. The Green Goblin flies to the top of the school and drops you to your death.")
                print("THE END")
            elif user_input == 'run':
                print("You flee from the scene, leaving Mr. Devon behind to die. You keep running until you think you're safe, and decide to take a break because this running thing is hard. But as you take a break, the ghost of Mr. Devon comes up and stabs you in the back and you die.")
                print("THE END")
        elif user_input == 'no':
            print("You say, 'No' and Mr. Devon gives you both detention. During detention, you meet a strange kid with green skin, who transforms into Green Goblin. He then begins to attack Mr. Devon and asks you to join him.")
            print("Do you join him or try to help Mr. Devon?")
            print("Type 'join' or 'help'")
            user_input = input()
            if user_input == 'join':
                print("You and Green Goblin kill Mr. Devon and conquer the universe.")
                print("THE END")
            elif user_input == 'help':
                print("Despite hating Mr. Devon, you don't want to see him die, so you try to protect him from the Green Goblin, only to be killed by Mr. Devon, who was a double agent the whole time.")
                print("THE END")
