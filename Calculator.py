operator_list = ["+","-","*","/"]

maths_operation = input (f"Please enter maths operation:{operator_list}")

first_number_string = input("Please enter the first number:")
first_number = int(first_number_string)

second_number_string = input("Please enter the second number:")
second_number = int(second_number_string)


if maths_operation == '+':
    print (first_number + second_number)
elif maths_operation == '-':
    print (first_number - second_number)
elif maths_operation == '*':
    print (first_number * second_number)
else:
    print (first_number / second_number)
