class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        count = 0
        while n >= i:
            n -= i
            i += 1
            count+=1
        return count
            
