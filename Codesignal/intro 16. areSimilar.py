def areSimilar(a, b):
    # For a = [1, 2, 3] and b = [1, 2, 3], the output should be areSimilar(a, b) = true.
    # For a = [1, 2, 3] and b = [2, 1, 3], the output should be areSimilar(a, b) = true.
    # For a = [1, 2, 2] and b = [2, 1, 1], the output should be areSimilar(a, b) = false.
    
    list_a = []
    list_b = []
    count = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            count+=1
            list_a.append(a[i])
            list_b.append(b[i])
    if count == 0:
        return True
    elif count == 2:
        return set(list_a)==set(list_b)
    else:
        return False
