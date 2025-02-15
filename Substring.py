def wordOccurenceNumber():
    string = input('Enter a sentence:\n').lower()
    wordList = {}
    SplitWord = string.split()
    for word in SplitWord:
        wordList.setdefault(word, 0)
        wordList[word] += 1

    anyPrinted = 0
    for k,v in wordList.items():
        if v > 1:
            print('word ', k, ' is repeated', v ,' times.',sep= '--')
            anyPrinted += 1
    
    if anyPrinted == 0:
        print('Sorry, no multiple word occurences detected.')

print('''This counts the occurence of word multiple times in a sentence.
Please add spaces between words and full stops.''')

wordOccurenceNumber()