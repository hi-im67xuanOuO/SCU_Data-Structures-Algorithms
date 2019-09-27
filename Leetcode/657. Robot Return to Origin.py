class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        
        for i in moves:
            if i == "U":
                y+=1
            elif i == "D":
                y-=1
            elif i == "R":
                x+=1
            elif i == "L":
                x-=1
        if x==0==y:
            return True
        else:
            return False
