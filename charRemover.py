from mymodule import get_valid_num as validNumCheck  # type: ignore
            
def remover():
    string = input('Enter a word: ')
    while True:
        number = validNumCheck('How many letters do want to delete: ')
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