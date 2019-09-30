def modulus(n):
    #given a number n, returns -1 if this number is not an integer and n % 2 otherwise. 
    if type(n)==int:
        return n % 2
    else:
        return -1
