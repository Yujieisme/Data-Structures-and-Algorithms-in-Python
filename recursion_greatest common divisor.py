#How to find the greatest common divisor of two numbers using recursion?
def find_GCD(n, m):
    assert int(a) == a and int(b) == b and a > 0 and b > 0, "The numbers must be positive integer"
    if m == 0:
        return n
    else:
        return find_GCD(m, n%m)
