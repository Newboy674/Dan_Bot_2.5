#Me tips: Make something to Check for if the character name was words or a number
#  - figure out how to remove an item from list

accounts = ["Jared", "Danny", "Boner", "Mark", "Steve"]
#              0        1        2       3        4

#(can also be)-5       -4       -3      -2       -1

print(accounts[1]) # Takes 1
print(accounts[1:3]) # Takes 1 to 3
print(accounts[2:]) # Takes 2 and onwards

import time

time.sleep(1)

print(accounts[-2])

time.sleep(1)

print("\n" + (accounts[1]))
accounts[1] = "Zanny"
print (accounts[1] + "\n")

accounts[1] = input("Write what the name u want the character to have \n")
print ("The name of the character is \""+ (accounts[1]) + "\"")
#make the if statement here
