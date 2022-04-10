from question_class import question
#READ the # in LINE 10

#A list of premade awnsers, following the format of a class
#These are called "Objects"

question_prompt = [
    question("a", "What is the colour of the sky? \n Blue [a] \n Red [b] \n Yellow [c]\n"),    #Called question_prompt[0]
    question("c", "Who invented gravity? \n George [a] \n Newton [b] \n none of these guys [c]\n"),   #Called question_prompt[1]
    question("b", "What is the meaning of life? \n 42 [a] \n food [b] \n subjective to opinion [c]\n")     #Called question_prompt[2]   #TEST If this only works in arrays!!! Cuz normally u need to assign the object with a varible too ( like: question1 = question(dummy code)
]
#print(question_prompt[1].answers)
#n_class.answers)
def run_test(question_prompt): #Runs the
    for object in question_prompt:
        score = 0
        answer_input = input(object.question_prompt)    #I said object.question_prompt because i said "for object in question_prompt"
        if answer_input == object.answers:              #Basically, the word object is there to represent each question that gets called for each iteration, instead of writing question_prompt[0], e.t.c  (which idk if that would even b possible lol) =
            score += 1
        else:
            print("wrong lol")

    return score

score = run_test(question_prompt)
print (("you got a score of ") + (str(score)) + ("out of ") + (str(len(question_prompt))) + ("!"))


