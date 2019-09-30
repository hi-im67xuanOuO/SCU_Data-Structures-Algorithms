def arrayChange(inputArray):
    # For inputArray = [1, 1, 1], the output should be arrayChange(inputArray) = 3.
    moves = 0
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            a = inputArray[i] - inputArray[i+1] +1
            inputArray[i+1] += a
            moves += a
    return moves
