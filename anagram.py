import re

def anagram(str, cmpStr):
    str = re.sub('[\s+]', '', str)
    cmpStr = re.sub('[\s+]', '', cmpStr)

    if (len(str) != len(cmpStr)):
        return print('Not an anagram')

    strArray = list(str)

    for i in range(len(strArray)):
        s = cmpStr[i]
        for j in range(len(strArray)):
            if(s == strArray[j]):
                strArray.pop(j)
                break

    if(len(strArray) == 0):
        return print('Anagram')
    else:
        return print('Not an anagram')

anagram('clint eastwood', 'old west action')
# n*(n)^2 ---> Brute Force method
