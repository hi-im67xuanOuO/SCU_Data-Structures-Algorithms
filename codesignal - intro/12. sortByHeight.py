def sortByHeight(a):
    # For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
    list = []
    b = []
    for i in range(len(a)):
        if a[i] == -1:
            list.append(i)
        else:
            b.append(a[i])
    
    x = sorted(b)
    for j in list:
        x.insert(j,-1)
    return x
        

