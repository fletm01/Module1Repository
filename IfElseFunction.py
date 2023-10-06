def find_middle_char (my_string):
    length = len(my_string)
   
    if length % 2 == 0:
        return None
    else: return my_string[length //2]
        

print (find_middle_char('abcde'))

# this calculation finds the middle character of a string by working out if the string has:
#   an even number of characters (None will be returned) as can be divided by 2 with no remainder
#   an odd number of characters (the middle character will be returned) has a remainder of 1 when divided by 2
