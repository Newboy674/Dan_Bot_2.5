# People = {
#     "James":"Gamer, Unemployed, 32",
#     "Marcus":"Gun Seller, 32",
#     "Travis": "Child, 12, Likes to eat paper",
#     "Spongebob": "Cartoon Character, 32, Likes to blow bubbles",
#     "George": "Sex Offender, 32",
#     "Henry": "Sex Offender, 32",
#     "Gill": "Sex Offender, 32",
#
# }

People = {
    "0": "James - Gamer, Unemployed, 32",
    "1": "Marcus - Gun Seller, 32",
    "2": "Travis - Child, 12, Likes to eat paper",
    "3": "Spongebob - Cartoon Character, 32, Likes to blow bubbles",
    "4": "George - Sex Offender, 32",
    "5": "Henry - Sex Rebounder, 32",
    "6": "Gill - Sex Defender, 32",

}

#how in the???
#print('\n'.join("{}: {}".format(k, v) for k, v in People.items()))
People_input = input("Name somebody on the list to get a description \n")
print(People[(People_input)])