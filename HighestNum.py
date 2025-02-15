print('This program claculates the highest number in a list of numbers')
def findHighest():
    numList = []
    while True:
        try:
            num = input('Enter numbers. Press enter to stop: ')
            if num == '':
                break
            numList.append(int(num))
        except ValueError:
            print('Invalid input.')
            print()
            continue
    
    highestNum = 0
    for i in numList:
        if i > highestNum:
            highestNum = i
    print(highestNum)

findHighest()