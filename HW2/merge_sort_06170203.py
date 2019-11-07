class Solution(object):
    
#1. 先做list的分割，這裡是left的部分～

    def halfcut_left(self,List):
        if len(List)>=1: #若list長度>=1時則進行分割
            mid = len(List)//2 #取mid中間值
            left = List[0:mid]  #left這個list為list對半切割後的左半邊（從第一個到我們取的中間值mid）
        return left
    
    
#1. 先做list的分割，這裡是right的部分～

    def halfcut_right(self,List):
        if len(List)>=1: #若list長度>=1時則進行分割
            mid = len(List)//2 #取mid中間值
            right = List[mid:len(List)+1]  #right這個list為list對半切割後的右半邊（從中間值mid的下一位到最後一個值）
        return right
    
    
#2. 再來做合併的部分

    def merge_sort(self,List):
        
        if len(List)<=1: #若list長度<=1則直接回傳list
            return List
        
        ans = [] #先設定一個list暫存我們排序後的答案
        
        if len(List)>1: #若list長度>1時，則重複呼叫並執行切割的def
            left = self.halfcut_left(List)
            right = self.halfcut_right(List)

            left = self.merge_sort(left)     # recursive時要記得設回left與right變數，下次執行時才會用新的left與right執行～
            right = self.merge_sort(right)
    
            l = 0
            r = 0
    
            while len(left)>0 and len(right)>0: # 若left與right兩個list的長度皆大於0，則開始比較left與right最左邊值的大小
                if left[l]<right[r]: # 若left的值<right的值，則在ans中append該left點
                    ans.append(left.pop(0))
                    if len(left)<=0: # 當append完成後left長度<=0時則break跳出程式
                        break
                if left[l]>right[r]: # 若left的值>right的值，則在ans中append該right點
                    ans.append(right.pop(0))
                    if len(right)<=0: # 當append完成後right長度<=0時則break跳出程式
                        break
                if left[l]==right[r]: # 若left的值=right的值，則在ans中append該right點（此處亦可改成left，沒有影響）
                    ans.append(right.pop(0))
                    if len(right)<=0: # 同樣檢查當append完成後right長度<=0時則break跳出程式
                        break
                        
            while len(left)>0: # 當只有left長度>0時，
                ans.append(left.pop(0)) # 在ans加入剩下的left值
                left = self.merge_sort(left)
                
            while len(right)>0: # 當只有right長度>0時，
                ans.append(right.pop(0)) # 在ans加入剩下的right值
                right = self.merge_sort(right)
        
        return ans
#以下是練習時的測試資料：
#output = Solution().merge_sort([3,2,-4,6,4,2,19])
#output2 = Solution().merge_sort([])
#output3 = Solution().merge_sort([2,2,1,3,3,3,4,-5,0,7,10,8])
#print(output)
#print(output2)
#print(output3)
