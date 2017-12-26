from nose.tools import assert_equal

def finder(arr1, arr2):
    num = 0
    for i in range(len(arr1)):
        num += arr1[i]

    for j in range(len(arr2)):
        num -= arr2[j]

    return num
    pass

finder([5,5,7,7],[5,7,7])

# Complexity -> O(2n-1)

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestFinder(object):
    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


# Run test
t = TestFinder()
t.test(finder)