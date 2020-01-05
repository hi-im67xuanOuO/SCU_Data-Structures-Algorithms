def alternatingSums(a):
    # For a = [50, 60, 60, 45, 70], the output should be alternatingSums(a) = [180, 105].
    x = 0
    y = 0
    l = len(a)
    for i in range(l):
        if i%2!=0:
            x+=a[i]
        if i%2==0:
            y+=a[i]
    return[y,x]
            

