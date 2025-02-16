from mymodule import get_valid_num as validNumCheck  # type: ignore

def exponent():

    def printNumInOrder(basenum,expnum):   # to print numbers in list for explanation 
        numList = []
        for i in range(expnum):
            numList.append(str(basenum))
        return numList
    
    base = validNumCheck('Enter a number: ')
    exponent = validNumCheck('Enter exponent number: ')
    answer =  base ** exponent
    baseString = ' * '.join(printNumInOrder(base,exponent))   # put list together as string
    
    print('\nBase =',base,'\nExponent =', exponent,'\n')
    print(base, 'raised to the power of', exponent, 'is:', answer)
    print('i.e.(', baseString, '=', answer, ')')    #put explanation together


exponent()