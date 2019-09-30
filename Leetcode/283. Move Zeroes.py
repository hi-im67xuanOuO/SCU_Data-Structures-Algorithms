class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)
        return nums
