#Missing Element Solution
from nose.tools import assert_equal

def finder(arr1, arr2):
    #Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1, arr2):
        if(num1 != num2):
            return num1

    # Otherwise return last element
    return False

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestFinder(object):
    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 5, 7, 7]), False)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)