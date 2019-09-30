def allLongestStrings(inputArray):
    # For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"]
    x = []
    y = 0
    for i in range(len(inputArray)):
        l = len(inputArray[i])
        if l>y:
            y = l
        else:
            y = y
    for i in range(len(inputArray)):
        if len(inputArray[i])==y:
            x.append(inputArray[i])
    return x
            
