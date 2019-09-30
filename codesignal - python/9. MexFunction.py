def mexFunction(s, upperBound):
    # For the given set s and given an upperBound, implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found
