task_finished = False

def add_to_employees(name, occupation, salary,):
    #employee_list2 = open("employee.list2","a")    #Try to fix this in next version
    #global employee_list2
    try:
        new_employee = str( (str(name)) + (" - ") + (str(occupation)) + (" - ") + (str(salary)) + ("$/hr"))
    except:
        print("Make sure you answer is in the format I specified")
        #task_finished = False

    return new_employee


if task_finished == False:
    name_input = input("Whats your name?\n")
    occupation_input = input("Who do you work for\n")
    salary_input = input("How much do you make (just give a number you make per hour)\n")
    new_employee = add_to_employees(name_input,occupation_input,salary_input) #p.s, will go past 19 after done
    #sooo figure that out in version 7.2.2

print (new_employee)

employee_list2 = open("employee.list2","a")
employee_list2.write(("\n")+(new_employee))