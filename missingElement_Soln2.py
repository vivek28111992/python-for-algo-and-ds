from nose.tools import assert_equal

import collections

def finder(arr1, arr2):

    #Using default dict to avoid key errors
    d = collections.defaultdict(int)

    #Add a count for every instance in Array 1
    for num in arr2:
        d[num] += 1

    # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num
        # Otherwise, subtract a count
        else:
            d[num] -= 1


arr1 = [5,5,7,7]
arr2 = [5,7,7]

result = finder(arr1, arr2)
print(result)