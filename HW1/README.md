# week5 - Quick Sort（作業一！！）

## Contents
* [簡介Quick_Sort與舉例說明](#簡介Quick_Sort與舉例說明)
* [程式碼與解說](#程式碼與解說)
  * coding實作一：[使用額外空間版本](#使用額外空間版本)
  * coding實作二：[無需額外空間版本](#無需額外空間版本)
* [流程圖](#流程圖)
  * 流程圖一：[有使用額外空間版本](#有使用額外空間版本)
  * 流程圖二：[無使用額外空間版本](#無使用額外空間版本)
* [Leetcode題目](#Leetcode題目)
  * 課堂練習題目：[148_Sort_List](#148_Sort_List)
* [影片觀念講解](#影片觀念講解)
* [Reference](#Reference)


## 簡介Quick_Sort與舉例說明
**`快速排序法（Quick sort）`** ：先找一個基準點（key），然後派兩個代理人分別從資料的左右兩端開始向中間找，當右邊找到一個值比key小，左邊找到一個值比key大，就讓他們互換。反覆此動作直到兩個點的位置相同。然後再將該位置的值與key互換，接著以新的基準點將原數列分為兩半，並分別重複執行前述動作。如此遞迴(recursion)，把數列一分為二，直到不能再進行切割為止，即完成排序。


* 舉例來說，有一數列有數字1~8，並選擇基準點為8。

   
   **6**　8　1　5　3　2　7　4


* 接著從左右兩邊開始分頭找。左邊找比基準點大的點，右邊找比基準點小的點。


   **6**　**`8`**　1　5　3　2　7　**`4`**


* 然後將找到的兩個點互換，使左邊的點漸漸比右邊來的小。


   **6**　**`4`**　1　5　3　2　7　**`8`**


* 接著就繼續往下找：


   **6**　4　`1`　5　3　2　`7`　8


   **6**　4　1　`5`　3　`2`　7　8


* 只要找到就將其再互換：


   **6**　4　1　**`2`**　3　**`5`**　7　8


* 繼續往下找，直到左邊的點等於右邊的點（本例子在3的位子）。


   **6**　4　1　2　**`3`**　5　7　8


* 將上述的點與基準點互換：

   **`3`**　4　1　2　**`6`**　5　7　8


* 以新的基準點將原數列分為兩個子循環。


   ( 3　4　1　2　) 　　+　　6 (基準點)　　+ 　　( 5　7　8 )


* 兩個子循環再分別重複以上所有動作。最終呈現結果為：


   1　2　3　4　5　6　7　8


* [～～返回目錄～～](#Contents)


## 程式碼與解說
### 使用額外空間版本：


> 我的程式碼連結（改寫版本與解說歷程）：[使用額外空間版本（內有兩種自己改寫的方法與歷程）](https://github.com/chinghsuan/class_exercises/blob/master/HW1/Quick_Sort_%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.ipynb)


### 無需額外空間版本：


> 我的程式碼連結（改寫版本與解說歷程）：[無需額外空間版本（內有一種自己改寫的方法與歷程）](https://github.com/chinghsuan/class_exercises/blob/master/HW1/Quick_Sort%E7%84%A1%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.ipynb
)


* [～～返回目錄～～](#Contents)



## 流程圖
### 有使用額外空間版本：


![Quick_Sort有使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/HW1/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BA%8C%EF%BC%9A%E5%89%B5%E9%80%A0%E6%96%B0%E7%A9%BA%E9%96%93%E6%9A%AB%E5%AD%98%E7%89%88%E6%9C%AC.png "Quick_Sort有使用額外空間")
> 放大圖片連結：https://github.com/chinghsuan/class_exercises/blob/master/HW1/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BA%8C%EF%BC%9A%E5%89%B5%E9%80%A0%E6%96%B0%E7%A9%BA%E9%96%93%E6%9A%AB%E5%AD%98%E7%89%88%E6%9C%AC.png


> 程式碼實作：[使用額外空間版本](#使用額外空間版本)


* [～～返回目錄～～](#Contents)



### 無使用額外空間版本：


![Quick_Sort無使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/HW1/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%B8%80%EF%BC%9Aplace-in%E7%89%88%E6%9C%AC.png "Quick_Sort無使用額外空間")
> 放大圖片連結：https://github.com/chinghsuan/class_exercises/blob/master/HW1/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%B8%80%EF%BC%9Aplace-in%E7%89%88%E6%9C%AC.png


> 程式碼實作：[無需額外空間版本](#無需額外空間版本)


* [～～返回目錄～～](#Contents)


## Leetcode題目
### 148_Sort_List
> 題目：[Leetcode 148.Sort_List](https://leetcode.com/problems/sort-list/)


#### 完整程式碼
```python
class ListNode:
    def __init__(self, x): # 定義好linked list的格式
         self.val = x
         self.next = None
class Solution(object):
    def sortList(self, head: ListNode) -> ListNode:
      
        if not head or not head.next: # 若head或head的下一個為空值，則直接return head
            return head
            
        slow = fast = head # 找出中心點
        
        while fast and fast.next:
            pre = slow # pre暫存較左的點
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


* [～～返回目錄～～](#Contents)


## 影片觀念講解
   <a href="https://www.youtube.com/watch?v=0Ds3KqYeXzA
" target="_blank"><img src="http://img.youtube.com/vi/0Ds3KqYeXzA/0.jpg" 
alt="Quick Sort" width="720" height="540" border="10" /></a>


* [～～返回目錄～～](#Contents)


## Reference
* [http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)	



* [https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html](https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html)


