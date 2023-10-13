def greet_user(first_name, last_name = ''):
    full_name = first_name + ' ' + last_name
    print('Hey there, ' + full_name)
 
greet_user('Jane', 'Doe')
greet_user('John')


