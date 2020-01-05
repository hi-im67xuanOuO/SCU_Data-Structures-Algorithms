class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s2 = s.rstrip()
        n = 0
        if len(s) == 0:
            return 0
            
        for i in s2:
            if i != " ":
                n += 1
            else:
                n = 0
        return n
