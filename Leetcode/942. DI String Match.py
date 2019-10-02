class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        a = 0
        b = len(list(S))
        s = list(S)
        ans = []
        for i in s:
            if i == "I":
                ans.append(a)
                a+=1
            else:
                ans.append(b)
                b-=1
        ans.append(b) #這裡append a 或 b 都可以
        return ans
