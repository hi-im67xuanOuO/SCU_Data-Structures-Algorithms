# CS50 - Week7

## Contents
* [Linked List](#Linked_List)
* [Hash Table](#Hash_Table)
* [線性探測Linear Probing](#線性探測Linear_Probing)
* [衝突](#衝突)
* [單獨鍊表法](#單獨鍊表法)
* [Reference](#Reference)


### Linked_List
Array可使相似變量存儲在連續內存，但他們大小固定，且沒有簡單的方法可在數值中間插入新的數值。我們必須為該Array分配內存，然後將所有插入位置的右邊元素都向右邊移動。  
Linked List就可以解決上述的問題，他並無需使用連續內存的約束。所以內存記憶體是分散的。  
以下是更多Linked List的介紹。

* **Linked List**：一種常見的基礎資料結構，是一種線性表，但是並不會按線性的順序儲存資料，而是在每一個節點裡存到下一個節點的指標(Pointer)。由於不必須按順序儲存，連結串列在插入的時候可以達到O(1)的複雜度，但是尋找一個節點或者存取特定編號的節點則需要O(n)的時間。

* **結構**：連結串列中最簡單的一種是單向連結串列，它包含兩個域，一個資訊域和一個指標域。這個連結指向列表中的下一個節點，而最後一個節點則指向一個空值。

* **示意圖**：


![image](http://cdn.cs50.net/2013/fall/lectures/7/m/notes7m/linked_list.png)  
> 圖片來源：http://cdn.cs50.net/2013/fall/lectures/7/m/week7m.pdf  


* **優點**：
  1. 可以克服陣列連結串列需要預先知道資料大小的缺點
  2. 可充分利用電腦記憶體空間，實現靈活的記憶體動態管理。
* **缺點**：
  1. 失去陣列隨機讀取的優點
  2. 連結串列因增加了節點的指標域，空間花費較大。
* **常見功能**：
  1. 新增insert
  2. 刪除delete
  3. 查詢search
  4. 走訪traverse


### Hash_Table
* **Hash Table**：**雜湊表**，也叫**哈希表**，是根據鍵（key）直接查詢內存存儲位置的資料結構，加快查找速度，計算鍵值的函數就稱為**映射函數**。
* **時間複雜度**：O(1)，恆定時間。  

### 線性探測Linear_Probing
* **線性探測**：當我們需要插入哈希表的位置已經有值，那我們就從該值往下再找一個空的單位，將這個新的值插入至此。這樣的方法在最壞的情況下，我們可能必須走訪array中所有b個位置才能插入或搜尋到目標值，因此運行時間會惡化為線性，這種方法就被稱為線性探測。

### 衝突
* **衝突**：當兩個元素具有相同的哈希值，則哈希表中存在衝突。上面說到的線性探測為處理碰撞的第一種方法。

### 單獨鍊表法
* **單獨鍊表法**：將雜湊到同一個存儲位置的所有元素保存在一個鍊表中。實現時，一種策略是雜湊表同一位置的所有衝突結果都是用Stack存放的，新元素被插入到表的前端還是後端完全取決於方便程度。


## Reference
http://www.youtube.com/watch?v=RUAsmwYC2mc  
http://cdn.cs50.net/2013/fall/lectures/7/m/week7m.pdf  
http://www.youtube.com/watch?v=QWnZpgZKOoc  
https://zh.wikipedia.org/wiki/%E9%93%BE%E8%A1%A8  
