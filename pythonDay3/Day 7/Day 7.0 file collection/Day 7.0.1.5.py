#This file is me messing around with how documents work with the for statement

#Although this "reads" the file, it does not make it into a list like the other code in 7.0.2 does

employee_list_txt = open("employee.list","r")

for employee in employee_list_txt:
    print(employee)



#employee_list_list = list.copy(employee_list_txt)
#The code hashed aboce dosent work because its not a list, so I cant make a copy

employee_list_txt.close()

print("\npart 2 below\n")

#Theory time... ( I think that readline dosnt work (as in, it makes skips a line each line in the output)
# because by reading a line with "readline" it goes to the next line in the document, cuz when the line is finished
# reading, it automatically just places the reader to the next line, thats just how it works
# And because of the "for" statement, it also
# wants to go to the next line each iteration, making it happen twice, causing the print out to skip a line

employee_list_txt = open("employee.list","r")

for each_line_in_list in employee_list_txt:
    print(employee_list_txt.readline())


employee_list_txt.close()

print("\npart 3 below\n")

#This code seems to work now...
#It also seems to be equivilent to whats on 7.0.2...

employee_list_txt = open("employee.list","r")

for each_line_in_list in employee_list_txt:
    print(each_line_in_list)

employee_list_txt.close()

print("\npart FOUR below\n")

employee_list_txt = open("employee.list","r")

def add_to_list(name, occupation)
    for each_line_in_list in employee_list_txt:
    print(each_line_in_list)
    #(each_line_in_list) #= ??? + ???? = something??? #Can prob do some funky stuff here but cant think of anything
    # worth coding


employee_list_txt.close()
