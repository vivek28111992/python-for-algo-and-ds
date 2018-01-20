# recursion digit sum

def sum_func(n):

    # Base Case
    if len(str(n)) == 1:
        return n

    else:
        return n%10 + sum_func(n//10)

print(sum_func(1235))