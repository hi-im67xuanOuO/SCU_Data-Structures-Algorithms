class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        l = len(A)
        
        for i in range(l):
            if A[i]%2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        for j in odd:
            even.append(j)
        return even
