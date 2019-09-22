class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        while n < len(nums)-1:
            if nums[n] == nums[n+1]:
                nums.pop(n+1)
            else:
                n+=1
        return(len(nums))
