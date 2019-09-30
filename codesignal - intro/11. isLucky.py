def isLucky(n):
    # For n = 1230, the output should be isLucky(n) = true;
    # For n = 239017, the output should be isLucky(n) = false.
    x = str(n)
    l = len(x)
    s = 0
    w = 0
    for i in range(l):
        if i< l/2:
            s+=int(x[i])
        else:
            w+=int(x[i])
            
    if s == w:
        return True
    else:
        return False

