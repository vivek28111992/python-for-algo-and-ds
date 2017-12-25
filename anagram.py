import re
from nose.tools import assert_equal

def anagram(str, cmpStr):
    str = re.sub('[\s+]', '', str)
    cmpStr = re.sub('[\s+]', '', cmpStr)

    if (len(str) != len(cmpStr)):
        #return print('Not an anagram')
        return False

    strArray = list(str)

    for i in range(len(strArray)):
        s = cmpStr[i]
        for j in range(len(strArray)):
            if(s == strArray[j]):
                strArray.pop(j)
                break

    if(len(strArray) == 0):
        #return print('Anagram')
        return True
    else:
        #return print('Not an anagram')
        return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class AnagramTest(object):
    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)

#anagram('clint eastwood', 'old west action')
# n*(n)^2 ---> Brute Force method
