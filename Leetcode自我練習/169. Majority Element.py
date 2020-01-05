class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            a = nums.count(i)
            if a>(len(nums)/2):
                return i
