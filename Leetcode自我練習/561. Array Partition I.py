class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        num = sorted(nums)
        for i in range(0,len(num)-1,2):
            ans += min(num[i],num[i+1])
        return ans
