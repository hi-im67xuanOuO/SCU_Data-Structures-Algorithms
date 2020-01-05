class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        
        for i in range(len(A)):
            if A[i]%2 ==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        
        for j in range(len(A)):
            if j%2 == 1:
                ans.append(odd.pop())
            else:
                ans.append(even.pop())
        return ans
