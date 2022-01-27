# Input_Number = input("Sex?\n")

#This is to solve the fuzz bizz thing (made my urs truely), tomm scott said its bad doe
for numbers in range(1001):
    numbers_result_3 = numbers % 3
    numbers_result_5 = numbers % 5
    if numbers_result_3 == 0 and numbers_result_5 == 0:
         print(f'{numbers} zoinks scoob')
    elif numbers_result_3 == 0:
        print(f'{numbers} zoinks')
    elif numbers_result_5 == 0:
        print(f'{numbers} scoob')

    else:
        print(f'{numbers}')

