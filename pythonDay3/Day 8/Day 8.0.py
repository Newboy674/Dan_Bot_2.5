#Make something that will format my list
#Make something that can make a copy of the list
#Make something so you can get rid of, or edit things on the list

valid_pokemon_types = ["Bug","Dark","Dragon","Electric","Fairy","Fighting","Fire","Flying","Ghost","Grass","Ground","Ice","Normal","Poison","Phychic","Rock""Steel","Water"]
pokemon_txt_lines_list = open("pokemon.txt", "r").readlines()
pokemon_txt = open("pokemon.txt", "a+") #Opens pokedex file
pokemon_type_input = ("placeholder")
pokemon_name_input = input("What is the name of this pokemon?\n")
while pokemon_type_input not in valid_pokemon_types:
    pokemon_type_input = input("What type is this pokemon?\n")
    if pokemon_type_input not in valid_pokemon_types:
         print("Thats not a valid pokemon type! Try again...\n")

pokemon_description_input = input("Describe this pokemon?\n")

def add_pokemon(name, type, description):
    pokedex_number = (int(len(pokemon_txt_lines_list))) + 1
    pokemon = (("(") + (str(pokedex_number)) + (") ") + (" Name: ") + (str(name)) + ("     Type: ") + (str(type)) + ("     Description: ") + (str(description)))

    return pokemon


pokemon = add_pokemon(pokemon_name_input, pokemon_type_input, pokemon_description_input)



pokemon_txt.write(("\n") + (pokemon))

pokemon_txt.close()
