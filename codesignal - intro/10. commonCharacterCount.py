def commonCharacterCount(s1, s2):
    # For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3. Strings have 3 common characters - 2 "a"s and 1 "c".
    x = 0
    for i in set(s1):
        m = min(s1.count(i),s2.count(i))
        x += m
    return x
