# recursive reverse String

'''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal

def reverse(s):

    if len(s) <= 1:
        return s
    else:
        # Recursion
        m = int(len(s)/2)
        return  reverse(s[m:]) + reverse(s[:m])

        """
        return reverse(s[1:]) + s[0]
        """

#print(reverse('hello world'))

class TestReverse(object):
    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')

# Run Tests
test = TestReverse()
test.test_rev(reverse)