#Convert a number from Decimal to Binary
def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n//2)
    return n % 2
