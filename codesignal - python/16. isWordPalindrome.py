def isWordPalindrome(word):
    # For word = "aibohphobia", the output should be isWordPalindrome(word) = true;
    # For word = "hehehehehe", the output should be isWordPalindrome(word) = false.

    return word == word[::-1]
