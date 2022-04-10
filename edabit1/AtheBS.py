import time
from math import *
spam = 'Hello'
print(spam)
'Hello'

spam = 'Goodbye'
print(spam)
'Goodbye'


print("Hello World!!!")
print("Whats ur name")
name = input()

print("Its good to see you " + name)

time.sleep(2)
print("The length of your name is")
print(len(name))

print("What is your age?")
age = input()
print("you will be " + str(int(age) + 1) + " in a year")    # Only add int when doing math to it

print("What is your age? test")
age_2 = input()
print("you will be " + age_2 + " in a year")   # The number is considered a string so u dont need to add str

# print (int(7.7))
# print (int(7.7) + 1)  #Rounds stuff???
# print (7.7 + 1)
# print(int(7.7))  #Yee rounds stuff
# print(int(7.4)) #Always round up too

print("Aight, its tiem 2 convert \n Input a cent amount and ill convert it to dollars (no decimals pls)")
money = input()



print("Wowza, you would have " + (str(floor(int(money) / 100))) + " dollars huh? and) ")
print (str(float(money) % 100) + " cents? broke ass")
#Add str if u did math to it because it gets rid of it being a string when u do that
# print ("Wowza, you would have " + (round(str(int(money) / 100))) + " dollars huh? and "
# + str(int(money) % 100) + " cents? broke ass") # Make sure to do it LAST because when u make it a string again u cant do math to it

money = input ("Aight, its tiem 2 convert again \n Input a cent amount and ill convert it to dollars (do decimals pls)") # using money again will reset the old varible btw
#print ("Wowza, u would have " + (str(floor(money)) / 100) + "Dollars, and ")
print ("\n Wow, Thats a cool " + str((len(money)) - 1) + " Digit number!!")
print ("Wowza, you would have " + (str(floor(float(money) / 100))) + " dollars huh? and " + (str(round(float(money) % 100))) + " cents? And also " + str((float(money) % 100) - floor(float(money) % 100)) + " of a cent??? \n (how do u even do that lol) broke ass x2")
#print (str(float(money) % 100) + "Cents? Broke ass x2")

