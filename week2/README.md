# week2 - Linked List

## Contact
* [簡介Linked-List](#簡介Linked-List)
* [比較Array與Linked-List](#比較Array與Linked-List)
    * [Array](#Array)
    * [Linked-List](#Linked-List)
* [影片觀念講解](#影片觀念講解)
* [實作概念](#實作概念)
* [Leetcode題目](#Leetcode題目)
    * [206_Reversed_Linked_List](#206_Reversed_Linked_List)
    * [707_Design_Linked_List](#707_Design_Linked_List)
* [Referrence](#Referrence)


## 簡介Linked-List
Linked list(連結串列)是一種常見的資料結構，其使用`node(節點)`來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以`NULL`來代表Linked list的終點（python中為`None`），見圖一(a)。若實際打開每個node的內部，至少會包含 __(1)data__ 來代表資料，與 __(2)pointer__ 指向下一個node，如圖一(b)。Linked list的資料散落在記憶體中各處，加入或是刪除元素只需要改變pointer即可完成，但是在資料的讀取上比較適合循序的使用，無法直接取得特定順序的值（比如說沒辦法直接知道list[3]）。


* **`single linked list`**：每個節點只有指向下一個結點，而沒有指出上一個結點。  
* **`double linked list`**：有指出上一個節點。


![Linked_List_1](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f1.png "Linked_List_1")


> 圖一(a)  
> 圖片來源：[http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)	


![Linked_List_2](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f2.png "Linked_List_2")  


> 圖一(b)  
> 圖片來源：[http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)	


* Node1：
    * 以int的data，記錄正整數7
    * 本身的記憶體位置為0x1001042f0
    * 以「node之pointer」，記錄(指向)下一個node之記憶體位置(0x100104300)
 
* Node2：
    * 以int的data，記錄正整數3
    * 本身的記憶體位置為0x100104300
        * 由於在Node1中的「node之pointer」指向了Node2之記憶體位置，因此，便能夠經由Node1「找到」Node2
    * 以「node之pointer」，記錄(指向)下一個node之記憶體位置(0x100104310)

* Node3：
    * 以int的data，記錄正整數14
    * 本身的記憶體位置為0x100104310。
    * 由於在Node2中的「node之pointer」指向了Node3之記憶體位置，因此，便能夠經由Node2「找到」Node3
    * 以「node之pointer」，記錄(指向)NULL，表示Linked list的最後一個node


> 通常在面對一個Linked list時，能夠公開存取(access)的node只有「第一個node」，以`ListNode *first`表示，不過因為node中有pointer記錄下一個node的記憶體位置，便能夠讀取下一個node的data與pointer。


## 比較Array與Linked-List
### Array
* 優點
    * **random access**：只要利用index即可在O(1)時間對Array的資料做存取。
    * **較Linked list為節省記憶體空間**：因為Linked list需要多一個pointer來記錄下一個node的記憶體位置。
* 缺點
    * **新增/刪除資料很麻煩**：若要在第一個位置新增資料，就需要O(N)時間把矩陣中所有元素往後移動。同理，若要刪除第一個位置的資料，也需要O(N)時間把矩陣中剩餘的元素往前移動。
    * 若資料數量時常在改變，要時常調整矩陣的大小，會花費O(N)的時間在搬動資料(把資料從舊的矩陣移動到新的矩陣)。
* 適用時機
    * 希望能夠快速存取資料。
    * 已知欲處理的資料數量，便能確認矩陣的大小。
    * 要求記憶體空間的使用越少越好。


### Linked-List
* 優點
    * **新增/刪除資料較Array簡單**：只要對O(1)個node(所有與欲新增/刪除的node有pointer相連的node)調整pointer即可，不需要如同Array般搬動其餘元素。
    * 若是在Linked list的「開頭」新增node，只要O(1)。
    * 若要刪除特定node，或者在特定位置新增node，有可能需要先執行O(N)的「搜尋」。
    * **Linked list的資料數量可以是動態的，不像Array會有resize的問題**
* 缺點
    * 因為Linked list沒有index，若要找到特定node，需要從頭(ListNode *first)開始找起，搜尋的時間複雜度為O(N)。
    * 需要額外的記憶體空間來儲存pointer。
* 適用時機
    * 無法預期資料數量時，使用Linked list就沒有resize的問題。
    * 需要頻繁地新增/刪除資料時。
    * 不需要快速查詢資料。
    
    
## 影片觀念講解
<a href="http://www.youtube.com/watch?feature=player_embedded&v=WwfhLC16bis
" target="_blank"><img src="http://img.youtube.com/vi/WwfhLC16bis/0.jpg" 
alt="圖片 ALT 文字放在這裡" width="720" height="540" border="10" /></a>


## 實作概念
* **part1 - class ListNode**：包含了資料及指標兩個屬性的節點
```python
class ListNode:
  def __init__(self, data): 
    # store data
    self.data = data
    # store the reference (next item)
    self.next = None
    return
```
在建立一個節點時，需要傳入一個data的值，並且指標預設是指向None的。
```python
node1 = ListNode(15)
```
這樣就會建立一個帶有15的資料的節點了。


* **part2 - class SingleLinkedList**：定義出各種資料結構操作的list本身
```python
class SingleLinkedList:
  def __init__(self): 
    self.head = None
    self.tail = None
    return
```
在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性。當我們加入一個新的節點時：
1. 若list本身還沒有任何節點，則head以及tail都會變成新的結點
2. 若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。

```python
def add_list_item(self, item):
  # make sure item is a proper node  
  if not isinstance(item, ListNode):
    item = ListNode(item)
    
  if self.head is None:
    self.head = item
  else:
    self.tail.next = item
    
  self.tail = item
  return
```
其中比較需要注意的是，在取得item之後，要檢查item是否是一個結點，若不是的話則使用ListNode(item)建立一個帶有item資料的節點。
```python
list1 = SingleLinkedList()
list1.add_list_item(node1)
list1.add_list_item(12)
```
這樣子就建立一個名為list1的linked-list，裡面包含了帶有資料15以及12的節點。


更多相關Linked List程式語法，可以參考 [https://stackabuse.com/python-linked-lists/](https://stackabuse.com/python-linked-lists/)


## Leetcode題目
### 206_Reversed_Linked_List
> 題目：[Leetcode 206. Reversed Linked List](https://leetcode.com/problems/reverse-linked-list/)


#### 完整程式碼
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None # 設立prev儲存處理過後的節點
        
        while head:
            current = head # current作為被挑出且將要處理的節點
            head = head.next # head為下個要執行動作的節點
            current.next = prev # 將處理過後的一串節點添加至正在處理中的節點之後
            prev = current # prev為目前處理完成的一串節點
        
        return prev
```


### 707_Design_Linked_List
> 題目：[Leetcode 707.Design Linked List](https://leetcode.com/problems/design-linked-list/)


#### 基礎程式語法與function
* **`val`** = 當前節點node的值
* **`next`** = 指向下一個節點
* **`prev`** = 指向前一個節點
* **`get(index)`** = 獲取第index節點的值。
* **`addAtHead(val)`** = 在第一個元素之前添加值為val的節點，插入後，成為新的第一個節點。
* **`addAtTail(val)`** = 將值為val的節點添加為最後一個節點。
* **`addAtIndex(index, val)`** = 在第index個節點之前添加一個值為val的節點。如果index等於linked list長度，則將該節點添加至末端。如果index大於長度，則不會插入該節點。
* **`deleteAtIndex(index)`** = 刪除第index個節點。


#### 完整程式碼(解法一）
```python
class MyLinkedList:

    def __init__(self): 
    # Initialize your data structure here.
        self.linkedlist = list()

    def get(self, index: int) -> int: 
    # Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        if index < 0 or index >= len(self.linkedlist) :
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val: int) -> None: 
    # Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        self.linkedlist.insert(0,val)
        
    def addAtTail(self, val: int) -> None: 
    # Append a node of value val to the last element of the linked list.
       self.linkedlist.append(val)

    def addAtIndex(self, index: int, val: int) -> None: 
    # Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        if index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index: int) -> None: 
    # Delete the index-th node in the linked list, if the index is valid.
       if  0 <= index < len(self.linkedlist):
            del self.linkedlist[index]
```


#### 完整程式碼(解法二）
```python
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None:
            return -1
        if index == 0:
            return self.val
        p = self.next
        i = 1
        while p != None:
            if i == index:
                return p.val
            p = p.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:
            self.val = val
            return
        temp = self.val
        self.val = val
        tempnode = self.next
        self.next = MyLinkedList()
        self.next.val = temp
        self.next.next = tempnode
        return

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:
            self.val = val
            return
        p = self
        while p.next != None:
            p = p.next
        p.next = MyLinkedList()
        p.next.val = val
        return


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        i = 0
        p = self
        pre = p
        if index <= 0:
            self.addAtHead(val)
            return
        while i < index:
            i += 1
            pre = p
            if p != None and p.val != None:
                p = p.next
            else:
                return
        pre.next = MyLinkedList()
        pre.next.val = val
        pre.next.next = p
        return
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        p = self
        if index < 0:
            return
        if index == 0:
            if self.val == None:
                return
            if self.next == None:
                self = None
                return
            self.val = self.next.val
            self.next = self.next.next
        pre = p
        while i < index:
            i += 1
            pre = p
            if pre == None:
                return
            p = p.next
        if p != None:
            pre.next = p.next
        else:
            pre.next = None
        return 
```


## Referrence
* [http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)	


* [https://medium.com/@tobby168/用python實作linked-list-524441133d4d](https://medium.com/@tobby168/用python實作linked-list-524441133d4d)


* [https://stackabuse.com/python-linked-lists/](https://stackabuse.com/python-linked-lists/)
