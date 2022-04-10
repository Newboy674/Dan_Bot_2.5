print (5 ** 3)

def raisepower(base,power):
    return int(base)**int(power)

base_input = input("Input base to power by\n")
power_input = input("Input the power value\n")

result = raisepower(base_input,power_input)
print(result)


