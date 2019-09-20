from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)
        for i in range(l):
            if x[i] != x[-1-i]:
                return False
        return True
        
