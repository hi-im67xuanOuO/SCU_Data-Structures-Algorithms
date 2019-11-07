class Solution(object):

    def heap_sort(self,List):
        
####1. 分割list成為heap結構。我的想法是先比較左右兩子節點，左邊的放大的，再比較左子節點與根節點的大小，較大的放入根節點。
    
        #因為要先將排序完成，所以設定while迴圈，以List的長度來判斷是否完成
        n = len(List)
        i=n

        #觀察heap的結構，根節點（root）若為第i個位置，其左子節點與右子節點位置分別為2*i+1與2*i+2
        while i>=0:
            root = i
            left = 2*i + 1
            right = 2*i + 2
        
            if left<n and right<n:
                if List[left] and List[right]: #左右兩個子節點先比較
                    if List[left]>List[right]:
                        List[left], List[right] = List[right], List[left]
                if List[root] and List[left]: #左子節點與其根節點比較
                    if List[left]<List[root]:
                        List[root], List[left] = List[left], List[root]
            if left<n:
                if List[left]: #只有左子節點時，左子節點跟其根節點比較
                    if List[left]<List[root]: 
                        List[root], List[left] = List[left], List[root]
            i-=1 #每執行完成一次，就將n減一，執行下一個點

        
####2. 排序heap。
    
        j = len(List)-1
        ans = [] #先創一個ans空間暫存我們排序好的答案
    
        while j>=0: #當j大於等於0時，也就是list中還有值時
            
            ans.append(List.pop(0)) #把list的第一個值pop到ans中
            
            #接著重新比較list內剩下前三個值的大小（因為已經pop掉第一個值，所以0、1、2位置的值都不同了）
    
            if 1<j and 2<j:
                if List[1] and List[2]: #左先跟右先比較，大的放左邊
                    if List[1]>List[2]:
                        List[1], List[2] = List[2], List[1]
                if List[0] and List[1]: #左再跟root比較，較大的放root
                    if List[1]<List[0]:
                        List[0], List[1] = List[1], List[0]
            if 1<j:
                if List[1]: #只有左有值時，左直接跟root比較，較大的放root
                    if List[1]<List[0]: 
                        List[0], List[1] = List[1], List[0]
            
            #接著因為heap結構已經被改變，所以要再重新建構一次heap
            n = len(List)
            i=n
                    
            while i>=0:
                
                root = i
                left = 2*i + 1
                right = 2*i + 2
        
                if left<n and right<n:
                    if List[left] and List[right]: #左右兩個子節點先比較
                        if List[left]>List[right]:
                            List[left], List[right] = List[right], List[left]
                    if List[root] and List[left]: #左子節點與其根節點比較
                        if List[left]<List[root]:
                            List[root], List[left] = List[left], List[root]
                if left<n:
                    if List[left]: #只有左子節點時，左子節點跟其根節點比較
                        if List[left]<List[root]: 
                            List[root], List[left] = List[left], List[root]
                        
                i-=1 #每執行完成一次，就將n減一，執行下一個點
            
            j-=1
        return ans
    
#以下為練習時的測試資料    
#output = Solution().heap_sort([12, 11, 13, 5, 6, 7])
#output2 = Solution().heap_sort([12,8, 13, 11,-1,-5, 7, 6, 5])
#output3 = Solution().heap_sort([])
#output4 = Solution().heap_sort([-3, 13, 11,-1,-5, 7, 6, 5])
#print(output)
#print(output2)
#print(output3)
#print(output4)
