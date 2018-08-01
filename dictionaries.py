def pretty_print_dict(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

#Key = student name; value = disney character
students = {
"Annamarie" : "Baymax",
"Adriana" : "Rapunzel",
"Sydney" : "Ariel",
"Lisette" : "Mulan"
}
pretty_print_dict(students)

Mimi = {"height": "5 foot 4",
        "born": "Taiwan",
        "birthday": "February 26"}
print(Mimi["born"])

def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

shorthand = {
"wow" : "world of warcraft",
"lol" : "league of legend",
"wtf" : "what the fuck",
"smh" : "shaking my head",
"btw" : "by the way",
"lmao" : "laugh my ass off",
"gwcsip" : "girls who code summer immersion program",
"imo" : "in my opinion"
}
translate_shorthand(shorthand)

story = """
Stacy was texting. She said lol noobs such smh. imo wow is are you going to gwcsip?
"""
story_list = story.split()

new_story_list = []
for word in story_list:
    if word in shorthand.keys():
        new_story_list.append(shorthand[word])
    else:
        new_story_list.append(word)
print(new_story_list)
print(" ".join(new_story_list))

def letter_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency.keys():
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

    print(frequency)

letter_frequency("pen pineapple apple pen")
