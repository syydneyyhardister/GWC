# Declare variables
mylist = [2,3,1,3,5]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

# TODO: Sort 'myList' (Why do we sort first?)
mylist.sort()
# TODO: Loop through 'mylist' with a for-Loop
#acces the index
print()
for index in range(len(mylist) - 1): # range(5) #goes through the range of NUMBERS 0, 1, 2, 3, 4
    print(index) #index is the index of the elements
    print(mylist[index], mylist[index + 1]) #print the elements
    # TODO: Check if adjacent elements of 'mylist' are the same

        # TODO: if they are the same, set has_duplicates to True
    if mylist[index] == mylist[index + 1]:
        has_duplicates = True
        print("{} is duplicated ".format(mylist[index]))
        # TODO: Exit out of the for-loop (no need to check rest of list)
        break
print(has_duplicates) # Our outputs of the program
