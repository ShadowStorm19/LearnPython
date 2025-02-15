keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]
numDict= {}

for i in range(len(keys)):
    try:
        numDict[keys[i]] = values[i]
    except IndexError:
        numDict[keys[i]] = ''

print(numDict)