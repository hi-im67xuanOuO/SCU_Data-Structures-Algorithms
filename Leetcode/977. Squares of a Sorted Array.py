class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        list = []
        
        for i in A:
            a = i*i
            list.append(a)
        
        list_ans = sorted(list)
        return list_ans
