word = input('Enter word: ')
print('Orginal String is ', word, '\nPrinting only even index characters')
# spellOutList = list(word)
evenLetterList = []
for i in range(len(word)):
    if i % 2 == 0:
        evenLetterList.append(word[i])

for h in range(len(evenLetterList)):
    print(evenLetterList[h]) 