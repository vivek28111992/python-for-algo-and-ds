# fibonacci

'''
 recursive function
'''

def fib_rec(n):

    if n == 1 or n == 0:
        return int((n+1)/2)
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    pass

print(fib_rec(12))

'''
 dynamic function
'''

# Instantiate Cache information
n = 11
cache = [None] * (n+1)
print(cache)

def fib_dyn(n):
    if cache[n] is not None:
        return cache[n]

    if n == 1 or n == 0:
        cache[n] = int((n+1)/2)
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]
    pass

print(fib_dyn(11))

'''
    iterative function
'''

def fib_iter(n):

    #Set Starting point
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a+b
    return a

print(fib_iter(13))