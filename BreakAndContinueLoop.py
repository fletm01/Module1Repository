for i in range(10):
    print(f'Start loop with i == {i}')
    if i == 3:
        print('Break out')
        break
    if i < 2:
        print(f'Continue')
        continue
    print('End loop')

    # this for loop runs until it hits 3, where it prints 'Break out' and then breaks the loop
    # any value less than 2 will print 'continue' then the loop will restart