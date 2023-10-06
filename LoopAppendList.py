full_list = ['the mouse', 'some cats', 'a dog', 'people']

def find_strings_containing_a(strings):
    result = []
    for string in strings:
        if 'a' in string:
            result.append(string)
    return result

result = find_strings_containing_a(full_list)
print(result)

#this function loops through a list to find the entries which contain an 'a', then adds'appends the entries to the result