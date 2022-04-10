# def solution(xs):
#     list.pop(xs)
#     list.reverse(xs)
#     list.pop(xs)
#     list.sort(xs)
#     list.reverse(xs)
#     formula_0 = 0
#     formula_1 = 0
#     formula_2 = 0
#     iteration_number = -1
#     for list_number in xs:
#         iteration_number += 1
#         if iteration_number == 0:
#             formula_0 = list_number
#         elif iteration_number == 1:
#             formula_1 = list_number
#         elif iteration_number == 2:
#             formula_2 = list_number
#         else:
#             solution = int(formula_0)*int(formula_1)*int(formula_2)
#             solution = str(solution)
#     return solution
#
# xs = list(input())
# print(str(solution(xs))

def solution(xs):
    list.pop(xs)
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
            solution = abs(solution)
            solution = str(solution)
    return solution

xs = list(input())
#print
(str(solution(xs)))