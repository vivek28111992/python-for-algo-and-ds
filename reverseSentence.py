from nose.tools import assert_equal

def rev_word(str):
    sentence = str.strip()
    sentenceArr = sentence.split()
    resultStr = ''
    i = 0
    for word in reversed(sentenceArr):
        if i == 0:
            resultStr += word
            i += 1
        else:
            resultStr += ' '
            resultStr += word
            i += 1

    #print(resultStr)
    return resultStr

"""
Another solution
def rev_word1(s):
    return " ".join(reversed(s.split()))
    
#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])
"""

#reverseSentence('    This is the best   ')

class ReversalTest(object):
    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word)
