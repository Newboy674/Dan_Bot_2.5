# def multiply_by_2(x):
#     return 2*int(x)
#
# x = input()
# x = multiply_by_2(x)
#
# print

print("awnser these with y/n pls ")



def questions1():
    is_gamer = input("Are you a gamer? \n")

    if is_gamer == ("y") or is_gamer == ("Y"):
        print("You are a gamer!")
        is_gamer = True
    elif is_gamer == ("n") or is_gamer == ("N"):
        print("You are not a gamer!")
        is_gamer = False
    else:
        print("that was neither y or n, try again...")
        questions1()
    return

questions1()




# print("Alright")
# monkey = input("Are you a monkey")
# if is_gamer == ("y"):
#     print("You are a gamer!")
# elif is_gamer == ("n")
#     print("You are not a gamer!")
#
#
#  = True
# monkey = False
#
# if is_gamer or monkey:
#     print("You have 2 hands")
# else:
#     print("You probably dont have 2 hands")
#
# print("\n")
# if monkey == False:
#     print("You are not monke :(")
