from mymodule import get_valid_num as validNumCheck  # type: ignore

def multiplicationTable():
    userNum = validNumCheck('Enter number for table to go up to: ')
    rangeMultiple = validNumCheck('Enter multiple number: ') # e.g. 12 times multiplication table
    userNum += 1
    rangeMultiple += 1
    for number in range(1, userNum):   #number goes from 1 to users input number
        print(number, end = '-  ')
        for time in range(1, rangeMultiple):
            multiplication  = number * time
            print(multiplication, end=' ')
        print()

multiplicationTable()