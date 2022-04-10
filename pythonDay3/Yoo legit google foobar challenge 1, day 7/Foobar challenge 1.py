#make code that translates a to z,   b, to x, and so on.
# translation = ""
# def solution(x):
#     translation = ""
#     for letter in x:
#         if letter == "a":
#             translation = translation + "z"
#         if letter == "b":
#             translation = translation + "y"
#         if letter == "c":
#             translation = translation + "x"
#         if letter == "d":
#             translation = translation + "w"
#         if letter == "e":
#             translation = translation + "v"
#         if letter == "f":
#             translation = translation + "u"
#         if letter == "g":
#             translation = translation + "t"
#         if letter == "h":
#             translation = translation + "s"
#         if letter == "i":
#             translation = translation + "r"
#         if letter == "j":
#             translation = translation + "q"
#         if letter == "k":
#             translation = translation + "p"
#         if letter == "l":
#             translation = translation + "o"
#         if letter == "m":
#             translation = translation + "n"
#         if letter == "n":
#             translation = translation + "m"
#         if letter == "o":
#             translation = translation + "l"
#         if letter == "p":
#             translation = translation + "k"
#         if letter == "q":
#             translation = translation + "j"
#         if letter == "r":
#             translation = translation + "i"
#         if letter == "s":
#             translation = translation + "h"
#         if letter == "t":
#             translation = translation + "g"
#         if letter == "u":
#             translation = translation + "f"
#         if letter == "v":
#             translation = translation + "e"
#         if letter == "w":
#             translation = translation + "d"
#         if letter == "x":
#             translation = translation + "c"
#         if letter == "y":
#             translation = translation + "b"
#         if letter == "z":
#             translation = translation + "a"
#         if letter == "A":
#             translation = translation + "Z"
#         if letter == "B":
#             translation = translation + "Y"
#         if letter == "C":
#             translation = translation + "X"
#         if letter == "D":
#             translation = translation + "W"
#         if letter == "E":
#             translation = translation + "V"
#         if letter == "F":
#             translation = translation + "U"
#         if letter == "G":
#             translation = translation + "T"
#         if letter == "H":
#             translation = translation + "S"
#         if letter == "I":
#             translation = translation + "R"
#         if letter == "J":
#             translation = translation + "Q"
#         if letter == "K":
#             translation = translation + "P"
#         if letter == "L":
#             translation = translation + "O"
#         if letter == "M":
#             translation = translation + "N"
#         if letter == "N":
#             translation = translation + "M"
#         if letter == "O":
#             translation = translation + "L"
#         if letter == "P":
#             translation = translation + "K"
#         if letter == "Q":
#             translation = translation + "J"
#         if letter == "R":
#             translation = translation + "I"
#         if letter == "S":
#             translation = translation + "H"
#         if letter == "T":
#             translation = translation + "G"
#         if letter == "U":
#             translation = translation + "F"
#         if letter == "V":
#             translation = translation + "E"
#         if letter == "W":
#             translation = translation + "D"
#         if letter == "X":
#             translation = translation + "C"
#         if letter == "Y":
#             translation = translation + "B"
#         if letter == "Z":
#             translation = translation + "A"
#         else:
#             translation = translation + letter
#     return translation
#
# print(solution("xywrgfds"))
translation = ""


# def solution(x):
#     translation = ""
#     for letter in x:
#         if letter == "a":
#             translation = translation + "z"
#         if letter == "b":
#             translation = translation + "y"
#         if letter == "c":
#             translation = translation + "x"
#         if letter == "d":
#             translation = translation + "w"
#         if letter == "e":
#             translation = translation + "v"
#         if letter == "f":
#             translation = translation + "u"
#         if letter == "g":
#             translation = translation + "t"
#         if letter == "h":
#             translation = translation + "s"
#         if letter == "i":
#             translation = translation + "r"
#         if letter == "j":
#             translation = translation + "q"
#         if letter == "k":
#             translation = translation + "p"
#         if letter == "l":
#             translation = translation + "o"
#         if letter == "m":
#             translation = translation + "n"
#         if letter == "n":
#             translation = translation + "m"
#         if letter == "o":
#             translation = translation + "l"
#         if letter == "p":
#             translation = translation + "k"
#         if letter == "q":
#             translation = translation + "j"
#         if letter == "r":
#             translation = translation + "i"
#         if letter == "s":
#             translation = translation + "h"
#         if letter == "t":
#             translation = translation + "g"
#         if letter == "u":
#             translation = translation + "f"
#         if letter == "v":
#             translation = translation + "e"
#         if letter == "w":
#             translation = translation + "d"
#         if letter == "x":
#             translation = translation + "c"
#         if letter == "y":
#             translation = translation + "b"
#         if letter == "z":
#             translation = translation + "a"
#         if letter == "A":
#             translation = translation + "Z"
#         if letter == "B":
#             translation = translation + "Y"
#         if letter == "C":
#             translation = translation + "X"
#         if letter == "D":
#             translation = translation + "W"
#         if letter == "E":
#             translation = translation + "V"
#         if letter == "F":
#             translation = translation + "U"
#         if letter == "G":
#             translation = translation + "T"
#         if letter == "H":
#             translation = translation + "S"
#         if letter == "I":
#             translation = translation + "R"
#         if letter == "J":
#             translation = translation + "Q"
#         if letter == "K":
#             translation = translation + "P"
#         if letter == "L":
#             translation = translation + "O"
#         if letter == "M":
#             translation = translation + "N"
#         if letter == "N":
#             translation = translation + "M"
#         if letter == "O":
#             translation = translation + "L"
#         if letter == "P":
#             translation = translation + "K"
#         if letter == "Q":
#             translation = translation + "J"
#         if letter == "R":
#             translation = translation + "I"
#         if letter == "S":
#             translation = translation + "H"
#         if letter == "T":
#             translation = translation + "G"
#         if letter == "U":
#             translation = translation + "F"
#         if letter == "V":
#             translation = translation + "E"
#         if letter == "W":
#             translation = translation + "D"
#         if letter == "X":
#             translation = translation + "C"
#         if letter == "Y":
#             translation = translation + "B"
#         if letter == "Z":
#             translation = translation + "A"
#         if letter in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
#             translation = translation
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(solution(input()))
# translation=""
# def solution(x):
#     translation=""
#     for letter in x:
#         if letter == "a":
#             translation = translation + "z"
#         if letter == "b":
#             translation = translation + "y"
#         if letter == "c":
#             translation = translation + "x"
#         if letter == "d":
#             translation = translation + "w"
#         if letter == "e":
#             translation = translation + "v"
#         if letter == "f":
#             translation = translation + "u"
#         if letter == "g":
#             translation = translation + "t"
#         if letter == "h":
#             translation = translation + "s"
#         if letter == "i":
#             translation = translation + "r"
#         if letter == "j":
#             translation = translation + "q"
#         if letter == "k":
#             translation = translation + "p"
#         if letter == "l":
#             translation = translation + "o"
#         if letter == "m":
#             translation = translation + "n"
#         if letter == "n":
#             translation = translation + "m"
#         if letter == "o":
#             translation = translation + "l"
#         if letter == "p":
#             translation = translation + "k"
#         if letter == "q":
#             translation = translation + "j"
#         if letter == "r":
#             translation = translation + "i"
#         if letter == "s":
#             translation = translation + "h"
#         if letter == "t":
#             translation = translation + "g"
#         if letter == "u":
#             translation = translation + "f"
#         if letter == "v":
#             translation = translation + "e"
#         if letter == "w":
#             translation = translation + "d"
#         if letter == "x":
#             translation = translation + "c"
#         if letter == "y":
#             translation = translation + "b"
#         if letter == "z":
#             translation = translation + "a"
#         if letter in "abcdefghijklmnopqrstuvwxyz":
#             translation = translation
#         else:
#             translation = translation + letter
#     return translation
#
# print(solution(input()))

def solution(x):
    translation=""
    for letter in x:
        if letter == "a":
            translation = translation + "z"
        if letter == "b":
            translation = translation + "y"
        if letter == "c":
            translation = translation + "x"
        if letter == "d":
            translation = translation + "w"
        if letter == "e":
            translation = translation + "v"
        if letter == "f":
            translation = translation + "u"
        if letter == "g":
            translation = translation + "t"
        if letter == "h":
            translation = translation + "s"
        if letter == "i":
            translation = translation + "r"
        if letter == "j":
            translation = translation + "q"
        if letter == "k":
            translation = translation + "p"
        if letter == "l":
            translation = translation + "o"
        if letter == "m":
            translation = translation + "n"
        if letter == "n":
            translation = translation + "m"
        if letter == "o":
            translation = translation + "l"
        if letter == "p":
            translation = translation + "k"
        if letter == "q":
            translation = translation + "j"
        if letter == "r":
            translation = translation + "i"
        if letter == "s":
            translation = translation + "h"
        if letter == "t":
            translation = translation + "g"
        if letter == "u":
            translation = translation + "f"
        if letter == "v":
            translation = translation + "e"
        if letter == "w":
            translation = translation + "d"
        if letter == "x":
            translation = translation + "c"
        if letter == "y":
            translation = translation + "b"
        if letter == "z":
            translation = translation + "a"
        if letter in "abcdefghijklmnopqrstuvwxyz":
            translation = translation
        else:
            translation = translation + letter

        #solution = translation
    return translation#solution
print(solution(input()))
