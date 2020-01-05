class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        list = set(A)
        count = 0
        ans = 0
        for item in list:
            if A.count(item)>=2:
                ans = item
                return ans
            else:
                continue
