class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None   
class MyHashSet:
    def __init__(self, capacity=5):# 定義出data的儲存空間
        self.capacity = capacity
        self.data = [None] * capacity
    def get_MD5(self,key):# 取得加密的MD5值
        from Cryptodome.Hash import MD5
        h = MD5.new()
        h.update(key.encode('utf-8'))
        ans = h.hexdigest()
        return ans
    def MD5_to_value(self,ans):# 將MD5加密結果轉換為16進位的數字
        value = int(ans,16)  
        return value
    def value_to_num(self,value):# 將16進位數字取餘數並決定儲存之capacity編號為何
        num = int(value%10)
        num = num%self.capacity
        return num
    def add(self, key):# 將key加入hash table中
        password = self.get_MD5(key)#先取得加密的值、16進位數以及餘數、儲存之capacity位置
        value = self.MD5_to_value(password)
        num = self.value_to_num(value)
        if self.data[num]==None: #若該capacity為空
            self.data[num]=ListNode(value) #直接將該key作為該capacity的值
        elif self.data[num] != None: #若該capacity不為空
            current=self.data[num] 
            while current: # 使用while迴圈走訪capacity中的值
                if current.next: # 若該值的下一位仍不為空
                    current=current.next # 繼續走訪
                else: # 若該值的下一位為空
                    current.next=ListNode(value) # 將該空的位子直接加上key值
                    break
    def contains(self, key):# 確認hash table中是否含有key值
        password = self.get_MD5(key) #先取得加密的值、16進位數以及餘數、儲存之capacity位置
        value = self.MD5_to_value(password)
        num = self.value_to_num(value)
        if self.data[num]==None: # 若該capacity為空
            return False # 回傳False
        current = self.data[num] #若該capacity不為空
        while current is not None: # 開始使用while迴圈走訪該capacity的值
            if current.val != value: # 若目前的值不等於key
                if current.next: # 且該值的下一位仍不為空
                    current = current.next # 繼續走訪
                else: # 若該值的下一位為空
                    return False # 回傳False
            elif current.val==value: # 若目前的值等於key
                return True # 回傳True
    def remove(self, key):# 將hash table的key值全部移除
        password = self.get_MD5(key)#先取得加密的值、16進位數以及餘數、儲存之capacity位置
        value = self.MD5_to_value(password)
        num = self.value_to_num(value)
        current = self.data[num] #設立一個current作為走訪時的「分身」
        if current: # 當current不為空且等於目標刪除value時
            if current.val == value: 
                current = current.next #直接將走訪的current從下一節點開始
                self.data[num] = current
        if current: # 當current不為空執行下面程式
            while current.next: # 當current的下一位不為空
                if current.next.val==value: # 且該值等於目標刪除value值
                    if current.next.next: # 檢查current的下下位，若不為空
                        current.next=current.next.next # 將current的下一位（也就是目標刪除的值）直接用current的下下位作替代
                    else: # current的下下位，若為空
                        current.next = None # 直接將current的下一位指定為空
                elif current.next.val!=value: # 若該值不等於目標刪除value值
                    current=current.next # 繼續走訪下一個節點

# 參考資料：
#http://practicalcryptography.com/hashes/md5-hash/  
#https://www.cs.wcupa.edu/rkline/ds/hash-sets.html  
#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html  
#https://toyo0103.blogspot.com/2018/04/hash-table.html   
#https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8
