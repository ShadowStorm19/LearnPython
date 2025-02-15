def get_valid_num(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print('Invalid input.')
            print()


def exponent():

    def printNumInOrder(basenum,expnum):   # to print numbers in list for explanation 
        numList = []
        for i in range(expnum):
            numList.append(str(basenum))
        return numList
    
    base = get_valid_num('Enter a number: ')
    exponent = get_valid_num('Enter exponent number: ')
    answer =  base ** exponent
    baseString = ' * '.join(printNumInOrder(base,exponent))   # put list together as string
    
    print('\nBase =',base,'\nExponent =', exponent,'\n')
    print(base, 'raised to the power of', exponent, 'is:', answer)
    print('i.e.(', baseString, '=', answer, ')')    #put explanation together


exponent()