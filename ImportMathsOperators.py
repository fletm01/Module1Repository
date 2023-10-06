
import operator 

# dict to bring in the operators
ops_dict = {
    
    "+":operator.add,
    "-":operator.sub,
    "x":operator.mul,
    "/":operator.truediv}

# function for the calculation 
def maths_fun (operator,y,z): # pass the operator '+' as an example & y & z will be the values.
    return ops_dict[operator](y,z) 
    
# opening the file & splitting the lines into lists
with open('Calculations.txt', 'r') as file_to_read:
    contents = file_to_read.read().splitlines()

# looping through the list & removing the word 'calc' & replacing the whitespace with a comma & then spliting on the comma
# finally passing each list through the function. 
x = 0 
for l in contents:
    i = l[5:].replace(' ', ',').split(",")
    x = x + maths_fun(i[0],int(i[1]),int(i[2]))
    #print(maths_fun(i[0],int(i[1]),int(i[2])))   
print(x)
