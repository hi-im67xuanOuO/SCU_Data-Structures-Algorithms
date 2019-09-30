def checkPalindrome(inputString):
    # For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
    # For inputString = "abac", the output should be checkPalindrome(inputString) = false;
    # For inputString = "a", the output should be checkPalindrome(inputString) = true.
    l = len(inputString)
    for i in range(l):
        if inputString[i] != inputString[-1-i]:
            return False
    return True
