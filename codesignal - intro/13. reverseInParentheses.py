def reverseInParentheses(inputString):
    # For inputString = "(bar)", the output should be reverseInParentheses(inputString) = "rab";
    # For inputString = "foo(bar)baz", the output should be reverseInParentheses(inputString) = "foorabbaz";
    # For inputString = "foo(bar)baz(blim)", the output should be reverseInParentheses(inputString) = "foorabbazmilb";
    # For inputString = "foo(bar(baz))blim", the output should be reverseInParentheses(inputString) = "foobazrabblim".
    l = len(inputString)
    for i in range(l):
        if inputString[i] == "(":
            a = i
        elif inputString[i] == ")":
            b = i
            return reverseInParentheses(inputString[:a]+ inputString[a+1:b][::-1]+inputString[b+1:])
    return inputString
