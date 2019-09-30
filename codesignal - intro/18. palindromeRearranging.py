def palindromeRearranging(inputString):
    # For inputString = "aabb", the output should be palindromeRearranging(inputString) = true.
    # We can rearrange "aabb" to make "abba", which is a palindrome.
    for s in inputString:
        if inputString.count(s) % 2 == 0:
            inputString = inputString.replace(s,'')
    if len(inputString) == 0 or len(inputString) == 1:
        return True
    elif len(inputString) % 2 == 1:
        return  inputString.count(inputString[0]) == len(inputString)
    else:
        return False
