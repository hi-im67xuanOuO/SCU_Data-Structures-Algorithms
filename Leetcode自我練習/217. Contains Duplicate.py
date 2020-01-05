class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = sorted(nums)
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                return True
        return False
