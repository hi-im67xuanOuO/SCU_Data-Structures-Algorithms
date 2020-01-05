class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = []
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                a.remove(i)
        return a.pop()
