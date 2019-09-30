def almostIncreasingSequence(sequence):
    # For sequence = [1, 3, 2, 1], the output should be almostIncreasingSequence(sequence) = false
    # For sequence = [1, 3, 2], the output should be almostIncreasingSequence(sequence) = true.
    for i in range(len(sequence)):
        c = sequence.pop(i)
        if sequence == sorted(sequence):
            for item in sequence:
                if sequence.count(item) != 1:
                    break
            else:
                return True
        sequence.insert(i, c)
    return False
