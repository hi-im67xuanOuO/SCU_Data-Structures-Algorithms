# week3 - Stack & Queue

## Contact
* [簡介Stack及Queue](#簡介Stack及Queue)
    * [Stack](#Stack)
    * [Queue](#Queue)
* [影片觀念講解](#影片觀念講解)
* [實作概念](#實作概念)
* [Leetcode題目](#Leetcode題目)
    * [206_Reversed_Linked_List](#206_Reversed_Linked_List)
* [Reference](#Reference)




## 簡介Stack及Queue
Stack和Queue是兩個使我們能簡單地依序檢索和儲存數據的結構。在Stack中，我們輸入的最後一個元素會是第一個被顯示出來的元素。在Queue中，我們輸入的第一個元素則會是第一個被顯示的元素。我們可以使用`push`將項目添加到Stack中，並使用`pop`操作來檢索項目。對於Queue，我們使用`enqueue`來添加項目，並使用`dequeue`檢索項目。


### `Stack`
* **遵循LIFO原則**：Last-in-First-out原則，就像一個硬幣堆在另一個硬幣上，最後一個被放在頂部的硬幣，會是第一個要從堆疊中移除的硬幣。
* 下圖為兩個Stack的基本操作：
    * **`push`**：將元素添加至Stack頂部。

      ![Stack1](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-1.jpg "Stack1")


    * **`pop`**：將Stack最頂部的元素刪除。

      ![Stack1](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-2.jpg "Stack2")


> 圖片來源：[https://stackabuse.com/stacks-and-queues-in-python/](https://stackabuse.com/stacks-and-queues-in-python/)


### `Queue`
* **遵循FIFO原則**：Fast-in-First-out原則，就像排隊等候進場一樣，第一個排隊的人會是能夠優先進場的人。
* 下圖為兩個Queue的基本操作：
    * **`enqueue`**：將元素添加至Queue尾端。

      ![Queue1](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-3.jpg "Queue1")


    * **`dequeue`**：將Queue最前端的元素刪除。

      ![Queue2](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-4.jpg "Queue2")


> 圖片來源：[https://stackabuse.com/stacks-and-queues-in-python/](https://stackabuse.com/stacks-and-queues-in-python/)
    
    
## 影片觀念講解
<a href="https://www.youtube.com/watch?v=wjI1WNcIntg" target="_blank"><img src="http://img.youtube.com/vi/wjI1WNcIntg/0.jpg" 
alt="Stack&Queue" width="720" height="540" border="10" /></a>


## 實作概念
* **part1-Stack**：包含了pop與append用法
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```


* **part2-Queue**：定義出各種資料結構操作的list本身
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```


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


## Reference
* [http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)	


* [https://medium.com/@tobby168/用python實作linked-list-524441133d4d](https://medium.com/@tobby168/用python實作linked-list-524441133d4d)


* [https://stackabuse.com/python-linked-lists/](https://stackabuse.com/python-linked-lists/)
