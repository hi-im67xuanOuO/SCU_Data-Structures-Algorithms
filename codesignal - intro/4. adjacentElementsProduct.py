def adjacentElementsProduct(inputArray):
    # For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21. 7 and 3 produce the largest product.
    x = inputArray[0]*inputArray[1]
    l = len(inputArray)
    for i in range(l-1):
        a = inputArray[i]*inputArray[i+1]
        if a>x:
            x = a
        else:
            x = x
    return x
