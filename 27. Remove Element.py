class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        while n<len(nums):
            if val == nums[n]:
                nums.pop(n)
            else:
                n+=1
        return len(nums)
