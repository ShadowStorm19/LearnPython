def get_valid_num(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print('Invalid input.')
            print()