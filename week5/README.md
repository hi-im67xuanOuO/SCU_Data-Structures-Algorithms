# week5 - Quick Sort（作業一！！）

## Contents
* [簡介Quick_Sort](#簡介Quick_Sort)
* [流程圖](#流程圖)
  * 流程圖一：[有使用額外空間版本](#有使用額外空間版本)
  * 流程圖二：[無使用額外空間版本](#無使用額外空間版本)
* [影片觀念講解](#影片觀念講解)
* [實例解說](#實例解說)
* [處理步驟分解](#處理步驟分解)
* [基本程式語法](#基本程式語法)
  * coding實作一：[使用額外空間版本](#使用額外空間版本)
  * coding實作二：[無需額外空間版本](#無需額外空間版本)
* [Leetcode題目](#Leetcode題目)
  * 課堂練習題目：[148_Sort_List](#148_Sort_List)
* [Reference](#Reference)


## 簡介Quick_Sort
快速排序法（Quick sort）運用到 `Divide and conquer` 的概念：先找一個基準點（key），然後派兩個代理人分別從資料的兩邊開始往中間找，如果右邊找到一個值比基準點小，左邊找到一個值比基準點大，就讓他們互換。反覆此動作直到兩個點相遇。然後再將相遇的點值與基準點互換，第一輪結束。如此重複遞迴(recursion)，把數列一分為二，直到最終完成排序。


* 示意圖如下：


   ![QuickSort](https://pic.pimg.tw/jialin128/1467645871-4201784417_n.png "QuickSort")


> 圖一


> 圖片來源：[http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)


## 流程圖
### 有使用額外空間版本：


![Quick_Sort有使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BA%8C%EF%BC%9A%E5%89%B5%E9%80%A0%E6%96%B0%E7%A9%BA%E9%96%93%E6%9A%AB%E5%AD%98%E7%89%88%E6%9C%AC.png "Quick_Sort有使用額外空間")
> 放大圖片連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BA%8C%EF%BC%9A%E5%89%B5%E9%80%A0%E6%96%B0%E7%A9%BA%E9%96%93%E6%9A%AB%E5%AD%98%E7%89%88%E6%9C%AC.png


### 無使用額外空間版本：


![Quick_Sort無使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%B8%80%EF%BC%9Aplace-in%E7%89%88%E6%9C%AC.png "Quick_Sort無使用額外空間")
> 放大圖片連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%B8%80%EF%BC%9Aplace-in%E7%89%88%E6%9C%AC.png


## 影片觀念講解
   <a href="https://www.youtube.com/watch?v=0Ds3KqYeXzA
" target="_blank"><img src="http://img.youtube.com/vi/0Ds3KqYeXzA/0.jpg" 
alt="Quick Sort" width="720" height="540" border="10" /></a>


## 實例解說


* 舉例來說，有一數列有數字1~10，並選擇基準點為8。

   
   **8**　6　1　10　5　3　9　2　7　4


* 接著從兩邊開始找。左邊找比基準點大，右邊找比基準點小。


   **8**　`6`　1　10　5　3　9　2　7　`4`


   **8**　6　`1`　10　5　3　9　2　7　`4`


   **8**　6　1　**`10`**　5　3　9　2　7　**`4`**


* 然後互換。


   **8**　6　1　**`4`**　5　3　9　2　7　**`10`**


* 再繼續往下找：


   **8**　6　1　4　`5`　3　9　2　`7`　10


   **8**　6　1　4　5　`3`　9　2　`7`　10


   **8**　6　1　4　5　3　**`9`**　2　**`7`**　10


* 再互換：


   **8**　6　1　4　5　3　**`7`**　2　**`9`**　10


* 繼續往下找，直到左右代理人相遇（本例子在2的位子）。


   **8**　6　1　4　5　3　7　**`2`**　9　10


* 與基準點互換：

   **`2`**　6　1　4　5　3　7　**`8`**　9　10


* 分為兩個子循環。


   ( 2　6　1　4　5　3　7 ) 　　+　　8 (基準點)　　+ 　　( 9　10 )


* 再分別重複以上動作。最終結果：


   1　2　3　4　5　6　7　8　9　10




## 處理步驟分解
1.  取第一個元素（最左的數）為鍵值 key
2.  由左向右（前向後）找一個數（第一個滿足的），其值大於等於 key 值，該數之索引為 left_pivot
3.  由右向左（後向前）找一個數（第一個滿足的），其值小於等於 key 值，該數之索引為 right_pivot
4.  如果 left_pivot < right_pivot 則交換值，否則把 key 值與 right_pivot 值交換，以 right_pivot 為基準，分為左右兩數列
5. 重複上述步驟排序左右兩個數列，直到完成排序

## 基本程式語法
### 使用額外空間版本：


![Quick_Sort有使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/img/Quick_Sort%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.png "Quick_Sort有使用額外空間")
> 完整程式碼連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/Quick_Sort_%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.ipynb


### 無需額外空間版本：


![Quick_Sort無使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/img/Quick_Sort_%E7%84%A1%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.png "Quick_Sort無使用額外空間")
> 完整程式碼連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/Quick_Sort%E7%84%A1%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.ipynb


## Leetcode題目
### 148_Sort_List
> 題目：[Leetcode 148.Sort_List](https://leetcode.com/problems/sort-list/)


#### 完整程式碼
```python
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        # pre = ListNode(0) #use it to clear the rear half linked list
        slow = fast = head # 找到中心點
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
        
        
    def merge(self, left, right):
        res = cur = ListNode(0) # 創建一個新的linked list儲存已merge好的資料
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
            if left: 
                cur.next = left
            if right: 
                cur.next = right
        return res.next
```


## Reference
* [http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)	


* [https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR](https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR)


* [https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html](https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html)

