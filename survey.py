import json
import os
list_of_responses = []
cont = True
while cont:

    questions = {
    "name" : "What is your name?",
    "birthday" : "What is your date of birth? (MM/DD/YYYY)",
    "age" : "What is your age?",
    "home" : "Where do you call home? (City, State, Country)",
    "highschool" : "What's the name of your high school?",
    "fav tv show" : "What's your favorite tv show?",
    "pet" : "Do you have a pet?",
    "hero" : "Who's your favorite superhero?",
    "movie" : "What's your favorite movie?"
    }

    response = {}
    for key, value in questions.items():
        response[key] = input(value)

    list_of_responses.append(response)

    to_cont = input("Continue? Y/N Don't press N unless you're the last person")
    if to_cont == "Y":
            cont = True
    else:
            cont = False

if os.path.isfile("data.json"):
    file = open("data.json", "r+")
    old_data = json.load(file)
    old_data.extend(data)
    file.write(json.dumps(old_data))
    file.close()
else:
    file = open("data.json", "w")
    file.write(json.dumps(json_data))
    file.close()

print(json_data)
print(list_of_responses)
json_data = list_of_responses
