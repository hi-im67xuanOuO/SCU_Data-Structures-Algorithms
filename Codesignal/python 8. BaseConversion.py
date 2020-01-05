def baseConversion(n, x):
    # given an integer number n and a base x, converts n from base x to base 16.
    return hex(int(n, x))[2:]
