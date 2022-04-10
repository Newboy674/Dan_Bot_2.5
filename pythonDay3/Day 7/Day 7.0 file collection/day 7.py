#Make it into a varible when u open it

employee_file = open("employee.list", "r")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())


print("So if a line was already read, the next line will be read instead... (even if you specify which line to read)\n")
print("putting a number in the \"readlines([])\" command really just skips however many lines u put in")

print(employee_file.readlines()[1])
#for each_line_in_document in employee_file.readlines
