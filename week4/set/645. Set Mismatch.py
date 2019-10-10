class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        holder = [0]*len(nums)
        repeat_num = 0
        for i in range(len(nums)):
            if holder[nums[i]-1] != 0:
                repeat_num = nums[i]
            holder[nums[i]-1] = nums[i]
        return [repeat_num,holder.index(0)+1]
