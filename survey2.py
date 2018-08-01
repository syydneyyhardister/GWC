import json
#file = open("new_data.json", "r")
##data = json.load(file)
#data
#for response in data:
    # print(response)



with open("data.json", "r") as f:
    # Load our json data into our json object
    data = json.load(f)

    # Loop through and print
    for d in data:
        print(d)
    print()

    # Find the most common homestate
    state_count = {} # hold the counts for each state
    for d in data:
        # Add 1 count for each state seen
        state_count[d["home"]] =  state_count.get(d["homes"], 0) + 1
    print("Home by percentage of participants")
    for state, count in state_count.items():
        print("{}: {}%".format(state, 100 * count/ len(data)))
    print()

    # Find the youngest and oldest age of participants
    print("Youngest and oldest participants")
    age_sort = sorted(data, key=lambda k: int(k['age'])) # sort from young to old
    print("Youngest: {}, age {}".format(age_sort[0]["name"], age_sort[0]["age"]))
    print("Oldest: {}, age {}".format(age_sort[-1]["name"], age_sort[-1]["age"]))
