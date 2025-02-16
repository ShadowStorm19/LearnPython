#sum of previous and current number
from mymodule import get_valid_num as validNumCheck  # type: ignore

num = [0]
rangeNum = validNumCheck('Enter range number: ') 
print('Printing current and previous number sum in a range(' + str(rangeNum) + ')')
for i in range(rangeNum):
    lastNum = num[-1]   
    num.append(i)
    currentSum = i + lastNum
    print('Current number:', str(i), 'Previous number:', lastNum, 'Sum:', currentSum)