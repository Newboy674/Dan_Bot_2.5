
# "For" Statement Tech

Cool_videogames = ["Minecraft", "Fortnite", "Garfield Cart Racing","amogus", "big chungus the movie", "beans"]

    # this can be named whatever
#     |
#     |
#     v
for vgame in Cool_videogames:
    print(vgame)



print("\n")

for index in range(10):     #Prints out numbers in specified range starting from 0, one before number specified
    print(index)

print("\n")

#The range (or whatever value is there) is the amount of times to repeat whatever is below the for statement!
#"For" is what I should default to, if i know how many times i have to repeat something.
# And instead, I should Use a while loop if I dont know... based off of what ppl say on the internet that is...
for iteration_number in range(6,20):
    print(index)

for index in range(len(Cool_videogames)):
    print(Cool_videogames[index])


#For loops seem to actually function slightly different then while loops, for example...
list_of_lists = [[1,2,3],[4,5,6],[7,8,9],]
for induvidual_list_number in list_of_lists:
    print(induvidual_list_number)

#Yeah sure I could code this using a while loop... But thats inefficient, and will take way more time so
#I should learn the "for" stuff
#An example of me using the while loop for the same purpose...

print("\n")
list_done = False
while list_done == False:
    print(list_of_lists[0])
    print(list_of_lists[1])
    print(list_of_lists[2])
    list_done = True

print("working?")
    #U can manipulate each iteration in both of them, but its harder for the while loop... for example


#IMPORTANT--- FIGURE OUT HOW TO MANIPULATE A RANGE OF ITERATIONS USING FOR, its 5 am and im tired so i didnt do
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ]
iteration_number = -1
for induvidual_list_number in list_of_lists:
    iteration_number += 1
    if iteration_number <= 1:            #will affect both 0 and 1 because its in the range of >=1
        print(induvidual_list_number)
        print("cool code stuff")
    else:
        print(induvidual_list_number)
        print("This is the third iteration btw")

    #Basically, you can manipulate iterations in chunks, like, for the 4 to the 27th iteration, I want something to
    #happen to the iteration, and I can do that with induvidual_list_number >= 1 and induvidual_list_number <= 27
    #A while loop will look like this:

list_done_2 = False
while list_done_2 == False:
    print(list_of_lists[0])
    print("cool code stuff")
    print(list_of_lists[1])
    print("cool code stuff")
    print(list_of_lists[2])
    list_done_2 = True

    #This exact example wasnt bad, but imagine this with 50 iterations, 6000 iterations!!! You know what im talking
    #about, the "for" loop is cleaner aslong as u use it in the right way at the right time.
