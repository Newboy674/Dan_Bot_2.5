#Refresh on the if statements and upgrade list abilities

question_set = 0
question = 0

while question_set == 0:
    if question == 0:
        ball_input = input("Do u got balls? (Answer with y or n)\n")
        if ball_input == ("Y") or ball_input == ("y"):
            print("U got nice balls bro")
            Balls=True
            question = 1
        elif ball_input == ("n") or ball_input == ("N"):
            print("Its ok, you can have Deez Nutz")
            Balls=False
            question = 1
        else:
            print("Awnser with y or n dumbass")
    elif question == 1:
        boob_input = input("\nU got any boobs on you?\n")
        if boob_input == ("n") or boob_input == ("N"):
            boobs=False
            print("They will grow one day =)")
            question_set = 1
        elif boob_input == ("y") or boob_input == ("Y"):
            boobs=True
            print("Nice boobs bro!")
            question_set = 1
        else:
            print("Awnser with y or n dumbass, u did it once already!!!")

    else:
        print("u stupid or somethin? use y or n...")

# if Balls == True:
#     print ("& U prob a guy")
# else:
#     print("U got no balls bro")
