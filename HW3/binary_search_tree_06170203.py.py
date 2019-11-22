class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def TreeToList(self, root): #tree轉換為list       

        tree_to_list=[] #創建一個放入node的list
        self.recursive(root,tree_to_list) #開始執行回圈
        return tree_to_list
     
    def recursive(self,root,tree_to_list):
        
        if root is not None: #當root不為空時，將其左右兩子節點都執行回圈，左右兩子節點概念也相同
            self.recursive(root.left,tree_to_list)
            tree_to_list.append(root.val) # 將root的值append進入我們創建的list中
            self.recursive(root.right,tree_to_list)

    def list_to_tree(self, nums): #List轉換為tree
        
        if not nums: 
            return None
        
        elif nums:
            nums = sorted(nums) #先將list排序，方便排列新的樹的結構
            Len = len(nums)
            middle = Len // 2 #取list中間的值作為中間值
            root = TreeNode(nums[middle]) #將該值作為root
            root.left = self.list_to_tree(nums[:middle]) #以mid為中心，將list分為左右兩側，並且分別執行該函式的遞迴
            root.right = self.list_to_tree(nums[middle+1:])
        return root
    
    def insert(self, root, val):
                                                                
        if root is None: #先檢測是否為空
            return TreeNode(val) #若為空則反回新增的該值
        
        current = root
        if root is not None: #若不為空
            
            while root is not None:
                
                if val>root.val: #若新增的值大於root值
                    if root.right:
                        root = root.right #繼續往右子樹找
                    else: #直到右子樹為空
                        break
                    
                elif val<root.val: #若新增的值小於root值
                    if root.left:
                        root = root.left #繼續往左子樹找
                    else: #直到左子樹為空
                        break
                    
                elif val==root.val: #若新增的值等於root值
                    if root.left: 
                        root=root.left #往左繼續執行
                    else: #直到左子樹為空
                        break
                        
            if root.val<val: #若root值小於我們要新增的值，
                val = TreeNode(val)
                root.right = val #將該值放入右子樹
                return root.right
            
            elif root.val>val: #若root值大於我們要新增的值，
                val = TreeNode(val)
                root.left = val #將該值放入左子樹
                return root.left
            
            elif root.val == value: #若root值等於我們要新增的值，
                val = TreeNode(val)
                root.left = val #將該值放入左子樹
                return root.left
    
    def search(self, root, target):
    
        if root is None: #步驟一，先判斷是否為空
            return None
    
        while root is not None: #步驟二，若不為空時，判斷root與目標值的大小
            
            if root.val < target: #目標值大於root時，繼續往右邊子樹尋找
                root = root.right
            elif root.val > target: #目標值小於root時，繼續往左邊子樹尋找
                root = root.left
            elif root.val == target: #root等於目標值時，返回該root
                root = root
                break
                
        return root
    
    def delete(self, root, target):
        
        tree_to_list = self.TreeToList(root) #將tree轉換為list
        
        ans_list = [] #新增一個list存放處理過後的值
        
        for  i in range(len(tree_to_list)): #使用for與if判斷原本list中的值，
            if tree_to_list[i]!=target: #list中的值不等於目標刪除值
                ans_list.append(tree_to_list[i]) # 就將值新增至新的list中
        
        answer = self.list_to_tree(ans_list) #最後用處理過後的新list，轉換為新的樹
        
        return answer
    
    def modify(self, root, target, new_val): 
        
        tree_to_list = self.TreeToList(root) #先將原本的tree轉換成list
        
        for  i in range(len(tree_to_list)): #使用for迴圈跟if判斷list中的值
            if tree_to_list[i]==target: #若該值等於我們要替換的目標值
                tree_to_list[i]=new_val #就將該值的位子改成新的值
        
        answer = self.list_to_tree(tree_to_list) #將處理完成的list轉回tree結構
        return answer

#root = TreeNode(5)
#Node1 = TreeNode(3)
#Node2 = TreeNode(3)
#Node3 = TreeNode(-5)
#Node4 = TreeNode(8)
#Node5 = TreeNode(7)
#Node6 = TreeNode(6)
#Node7=TreeNode(10)
#root.left=Node1
#root.left.left=Node2
#root.left.left.left=Node3
#root.right=Node4
#root.right.left=Node5
#root.right.left.left=Node6
#root.right.right=Node7

## 參考資料
## https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be
## http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
## http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
## https://www.geeksforgeeks.org/binary-search-tree-data-structure/
