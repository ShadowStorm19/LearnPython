numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def checkList(list1):
    print('Given list:', list1)
    if list1[0] == list1[-1]:
        print('Result is True')
    else:
        print('Result is False')
    print()
    
checkList(numbers_x)
checkList(numbers_y)