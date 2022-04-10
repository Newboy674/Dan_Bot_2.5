#Goal - make 2+ lists and play around with mechanics
#Find out how to make it to ask to add things, and u can choose how many u want to add to the list

#Tips: Extend adds a list/phrase where each thing on the list is a seperate part of the list it was added to
#So adding a list will make each piece of the list a seperate thing, and a phrase will be one part of list per letter
#Append adds it all in one ball, so a full list will be a single part of a list, and a full phrase will
# be a single thing



import time
good_list = ["Mark", "Dan", "Fred", "12", "Patrick", "21", "2", "I will be popped"]
naughty_list = ["Grinch", "Greg", "Marcus", "Spongebob"]
undecided = ["Toad", "Mario", "James", "Steve", "Joker"]

print(good_list)

list.pop(good_list)   #pop gets rid of name/number = to the right

print(good_list)

list.sort(good_list)  #Sorts obv

print(good_list)

list.extend(good_list, "joe biden")

print(good_list)

time.sleep(2)

print(naughty_list)

list.extend(good_list, naughty_list)  #Only adds the second list to the first list, so the second list stays same

print(good_list)
print(naughty_list)
print(good_list)

print("\n")

list.index((good_list), "Dan")

list.copy(good_list)



