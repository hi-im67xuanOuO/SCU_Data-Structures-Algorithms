def shapeArea(n):
    x = 1
    if n == 1:
        return x
    else:
        for i in range(2,n+1):
            a = 4*(i-1)
            x = x+a
        return x
