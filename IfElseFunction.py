def find_middle_char (my_string):
    length = len(my_string)
   
    if length % 2 == 0:
        return None
    else: return my_string[length //2]
        

print (find_middle_char('abde'))


