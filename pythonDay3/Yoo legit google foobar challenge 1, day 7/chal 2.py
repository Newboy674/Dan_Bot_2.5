

#list.sort(array_powers)
#list.reverse(array_powers)
#print (array_powers)

#Basis --- Multiply 3 highest numbers in a list

def solution(xs):
    list.pop(xs)               #popping the ends because of the "[" and "]" ruining the math
    list.reverse(xs)
    list.pop(xs)
    list.sort(xs)
    list.reverse(xs)
    formula_0 = 0
    formula_1 = 0
    formula_2 = 0
    iteration_number = -1
    for list_number in xs:
        iteration_number += 1
        if iteration_number == 0:
            formula_0 = list_number
        elif iteration_number == 1:
            formula_1 = list_number
        elif iteration_number == 2:
            formula_2 = list_number
        else:
            solution = int(formula_0)*int(formula_1)*int(formula_2)
            solution = str(solution)

    return solution

#  example... array_powers = [8,7,1,6,2]            ####examples  ## xs = array_powers
array_powers = list(input())
print((str(solution(array_powers)))+(" yee dis a string"))