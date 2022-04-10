employee_list = open("employee.list", "r")
#
#The r means read. w means write, This will overwrite the WHOLE file with whatever you type into it
##a means append, which only lets u add stuff
##r+ means read and write, again, write OVERWRITES the file

print(employee_list.readable())       #Checks if the line is readable
for each_line_in_list in employee_list:
    print(employee_list.readline())    #Make sure its readlines and not read line
employee_list.close()
try:
    print(employee_list.readable())
except ValueError:
    print("\n The list is closed so u cant read it")



employee_list = open("employee.list", "r")
print(employee_list.readable())
for each_line_in_list in employee_list:
    print (employee_list.readlines())    #Make sure its readlines and not read line
employee_list.close()
try:
    print(employee_list.readable())
except ValueError:
    print("\n The list is closed so u cant read it")