employee_list_txt = open("employee.list", "r")


print(employee_list_txt.readable())   #True because it is infact readable

employee_list_list = (employee_list_txt.readlines())    #Make sure its readlines and not read line

print(employee_list_list)
employee_list_2 = list.copy(employee_list_list)  #This makes a list copy of the first document


#Theory time... (Moved to 7.0.1.5) I think that readline dosnt work because by reading a line it goes to the next line in the document
#And because the for statement also goes to the next line each iteration, it causes the print out to skip a lin
#

employee_list_txt.close()
# try:
#     print(employee_list_txt.readable())
# except ValueError as error:
#     print(error)    #This is prob just saying that u cant do anything cuz its a closed file
