from nose.tools import assert_equal

def compress(compStr):
    charTracker = {}

    for i in compStr:
        if i in charTracker:
            charTracker[i] += 1
        else:
            charTracker[i] = 1

    #print(charTracker)

    resultStr = ''
    for key, value in charTracker.items():
        resultStr += key
        resultStr += str(value)

    return resultStr
    #print(resultStr)

#compress('AAAABBBBCCCCCDDEEEE')

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)