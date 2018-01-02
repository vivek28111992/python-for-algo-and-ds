from nose.tools import assert_equal

def finder(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in tha arrays
    for num in arr1+arr2:
        #print(num)
        result ^= num
        #print(result)

    return result

arr1 = [5,7,7,5]
arr2 = [5,7,7]

result = finder(arr1, arr2)
#print(result)


class TestFinder(object):
    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


# Run test
t = TestFinder()
t.test(finder)