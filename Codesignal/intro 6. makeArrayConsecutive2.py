def makeArrayConsecutive2(statues):
    # For statues = [6, 2, 3, 8], the output should be makeArrayConsecutive2(statues) = 3. Ratiorg needs statues of sizes 4, 5 and 7.
    count = 0
    for i in range(min(statues),max(statues)):
        if i not in statues:
            count+=1
    return count

