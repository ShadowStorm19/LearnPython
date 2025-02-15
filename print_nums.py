#...
def get_valid_num(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print('Invalid input.')
            print()

num = [0]
rangeNum = get_valid_num('Enter range number: ') 
print('Printing current and previous number sum in a range(' + str(rangeNum) + ')')
for i in range(rangeNum):
    lastNum = num[-1]   
    num.append(i)
    currentSum = i + lastNum
    print('Current number:', str(i), 'Previous number:', lastNum, 'Sum:', currentSum)