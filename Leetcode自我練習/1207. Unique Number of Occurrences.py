class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        a = []
        b = list(set(arr))
        for i in b:
            a.append(arr.count(i))
        a.sort()
        for j in range(len(a)-1):
            if a[j] == a[j+1]:
                return False
        return True
            
