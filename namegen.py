from random import *

aList = ["Spaghetti", "Pizza", "Hamburgers", "Chicken"]
bList = ["Bread", "Fries", "Onion Rings", "Chips"]
cList = ["Cake", "Ice cream", "Cupcakes", "Cookies"]
response = input("Would you like to eat?(Y/N?)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(aList)-1)
        bRandomIndex = randint(0, len(bList)-1)
        cRandomIndex = randint(0, len(cList)-1)
        print("{}, {}, {}.".format(aList[aRandomIndex], bList[bRandomIndex], cList[cRandomIndex]))
    else :
        print("{} is an invalid input".format(response))
    response = input("Would you like to eat?(Y/N?)")
