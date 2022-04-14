#How to find the sum of digits of a positive integer number using recursion?
def sum_digit(n):
    assert n>=0 and int(n) == n, "The number has to be a positive integer only!"
    if n <= 10:
        return n
    return (sum_digit(n//10) + n%10)
