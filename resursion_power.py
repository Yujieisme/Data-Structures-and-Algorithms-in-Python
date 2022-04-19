# How to calculate power of a number using recursion
def power(n,m):
    assert m>0 and int(m) == m, "The exponent must be positive integer"
    if m == 0:
        return 1
    else:
        return n*power(n, m-1)
