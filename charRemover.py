def get_valid_num(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print('Invalid input.')
            print()
            
def remover():
    string = input('Enter a word: ')
    while True:
        number = get_valid_num('How many letters do want to delete: ')
        if number > len(string):
            print('Sorry word is not that long')
            continue
        else:
            break
    
    stringExtend = list(string)
    del stringExtend[0: number]
    result = ''.join(stringExtend)
    print(result)

remover()