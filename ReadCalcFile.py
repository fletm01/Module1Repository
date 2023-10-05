opened_file = open ('Calculations.txt')

with open('Calculations.txt','r') as file_to_read:
    contents = file_to_read.read().splitlines()

running_total = 0

for calculation in contents:
    calculation_parts = calculation.split()
    maths_operation = calculation_parts[1]
    first_number = int(calculation_parts[2])
    second_number = int(calculation_parts[3])

    print (calculation)


    if maths_operation == '+':
        result = first_number + second_number
    elif maths_operation == '-':
        result = first_number - second_number
    elif maths_operation == 'x':
        result = first_number * second_number
    else:
        result = first_number / second_number

    print(result)

    running_total += result

print(running_total)





