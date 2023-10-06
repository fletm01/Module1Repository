for letter in ['A', 'B', 'X', 'C', 'D', 'E']:

    if letter == 'X':
        continue
    if letter == 'D':
        break

    print(letter)

    # This loop runs and prints letters (A & B) until it reaches X where it will 'Continue' the loop 
    #   from the start before it reaches print.
    # When the loop reaches D it will break the loop altogether
    # This will print A B C    