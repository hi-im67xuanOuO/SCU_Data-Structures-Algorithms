def listBeautifier(a):
    # Let's call a list beautiful if its first element is equal to its last element, or if a list is empty. Given a list a, your task is to chop off its first and its last element until it becomes beautiful.
    
    #For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be listBeautifier(a) = [4, 38, 4].
    
    #For a = [1, 4, -5], the output should be listBeautifier(a) = [4]
    
    res = a[:]
    while res and res[0] != res[-1]:
        a, *res, b = res
    return res
