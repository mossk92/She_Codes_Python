print("LISTS CLASSWORK")
print("-----------------------------------------------")

chilli_wishlist = ["igloo","chicken","donut toy","cardboard box"]
    #lists are written with square brackets

print(len(chilli_wishlist))
    #finds the number of items in the list

print(chilli_wishlist)
    #prints the whoel list

print(type(chilli_wishlist))
    #prints the type of variable = list

print(chilli_wishlist[0]) 
    #shows first element

print(chilli_wishlist[1]) 
    #shows second element

print(chilli_wishlist[-1]) 
    #shows the last element

print(chilli_wishlist[0:2]) 
    #shows array starting at first element and stopping at second index (not inclusive)

print(chilli_wishlist[1:3])
    #shows array starting at second element and stopping at third index (not inclusive)

chilli_wishlist[1] = "carrot" 
    #changes the second element (first index)
print(chilli_wishlist)

#Add to List
chilli_wishlist.append("Donut Toy") 
    #add an item to the end of the list (best for single elements only)
print(chilli_wishlist)

chilli_wishlist.extend(["Treat","Play date"]) 
    #best to use with multiple elements
print(chilli_wishlist)

chilli_wishlist.insert(1,"Ball") 
    #add an item before a specified point
print(chilli_wishlist)

#Remove from List
chilli_wishlist.pop(2) #removes a specified index
print(chilli_wishlist)

chilli_wishlist.remove("cardboard box") #removes a detailed item from list (not index)
print(chilli_wishlist)

#Lists and If Statements
if "tennis ball" in chilli_wishlist: #looks for if ball is in the list of not
    print("Chilli would like a tennis ball") 
else:
    print("Chilli doesn't fell like playing fetch")

if len(chilli_wishlist) > 8: #counts the number of items in the list
    print("Chill wants a lot of stuff")

#Sublists
dog_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"]
    ["cardboard box", "box", "dig mat"]
]

print(len(dog_wishlist)) #will count the number between commas (so lists are counted as one) 
print(dog_wishlist[2]) #will return the list that is in elemnt 3
print(dog_wishlist[2][1]) #will return the first index from the list in the second index of overall list






print()
print("Division:")



print()
print("Comparing different types:")



print()
print("EXERCISES")
print("-----------------------------------------------")

print("Q1: ")



print()
print("Q2: ")



print()
print("Q3: ")



print()
print("Q4: ")



print()
print('########################################################')
print()