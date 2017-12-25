from nose.tools import assert_equal

def pair_sum(arr, sum):

    if(len(arr) < 2):
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set the target difference
        target = sum - num

        # Add it to set if target hasn't been set
        if target not in seen:
            seen.add(num)
        else:
            # Add a tuple with corresponding pair
            output.add( (min(num, target), max(num, target)) )

    return len(output)
    # Nice one-liner for printing output
    # return print('\n'.join(map(str,list(output))))

#pair_sum([1,3,2,2],4)

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestPair(object):
    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')

# Run tests
t = TestPair()
t.test(pair_sum)