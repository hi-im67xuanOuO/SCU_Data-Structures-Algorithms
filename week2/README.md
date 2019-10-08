# week2 - Linked List

## Contact
* [簡介Linked-List](#簡介Linked-List)
* [比較Array與Linked-List](#比較Array與Linked-List)
* [實作概念](#實作概念)
* [Leetcode題目](#Leetcode題目)

## 簡介Linked-List
Linked list(連結串列)是一種常見的資料結構，其使用`node(節點)`來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以`NULL`來代表Linked list的終點，見圖一(a)。


![Linked_List_1](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f1.png "Linked_List_1")


> 圖一(a)  


若實際打開每個node的內部，至少會包含 __(1)data__ 來代表資料，與 __(2)pointer__ 指向下一個node，見圖一(b)：  


![Linked_List_2](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f2.png "Linked_List_2")  


> 圖一(b)  


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



## 實作概念

## Leetcode題目
