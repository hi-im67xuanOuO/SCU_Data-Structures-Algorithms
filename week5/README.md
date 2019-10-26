# week5 - Quick Sort（作業一！！）

## Contents
* [簡介Quick_Sort與舉例說明](#簡介Quick_Sort與舉例說明)
* [流程圖](#流程圖)
  * 流程圖一：[有使用額外空間版本](#有使用額外空間版本)
  * 流程圖二：[無使用額外空間版本](#無使用額外空間版本)
* [影片觀念講解](#影片觀念講解)
* [處理步驟分解](#處理步驟分解)
* [基本程式語法](#基本程式語法)
  * coding實作一：[使用額外空間版本](#使用額外空間版本)
  * coding實作二：[無需額外空間版本](#無需額外空間版本)
* [Leetcode題目](#Leetcode題目)
  * 課堂練習題目：[148_Sort_List](#148_Sort_List)
* [Reference](#Reference)


## 簡介Quick_Sort與舉例說明
快速排序法（Quick sort）：先找一個基準點（key），然後派兩個代理人分別從資料的左右兩端開始向中間找，當右邊找到一個值比key小，左邊找到一個值比key大，就讓他們互換。反覆此動作直到兩個點的位置相同。然後再將該位置的值與key互換，接著以新的基準點將原數列分為兩半，並分別重複執行前述動作。如此遞迴(recursion)，把數列一分為二，直到不能再進行切割為止，即完成排序。


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



## 流程圖
### 有使用額外空間版本：


![Quick_Sort有使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BA%8C%EF%BC%9A%E5%89%B5%E9%80%A0%E6%96%B0%E7%A9%BA%E9%96%93%E6%9A%AB%E5%AD%98%E7%89%88%E6%9C%AC.png "Quick_Sort有使用額外空間")
> 放大圖片連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BA%8C%EF%BC%9A%E5%89%B5%E9%80%A0%E6%96%B0%E7%A9%BA%E9%96%93%E6%9A%AB%E5%AD%98%E7%89%88%E6%9C%AC.png


> 程式碼實作：[使用額外空間版本](#使用額外空間版本)


* [～～返回目錄～～](#Contents)



### 無使用額外空間版本：


![Quick_Sort無使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%B8%80%EF%BC%9Aplace-in%E7%89%88%E6%9C%AC.png "Quick_Sort無使用額外空間")
> 放大圖片連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/%E6%B5%81%E7%A8%8B%E5%9C%96%E4%B8%80%EF%BC%9Aplace-in%E7%89%88%E6%9C%AC.png


> 程式碼實作：[無需額外空間版本](#無需額外空間版本)


* [～～返回目錄～～](#Contents)


## 影片觀念講解
   <a href="https://www.youtube.com/watch?v=0Ds3KqYeXzA
" target="_blank"><img src="http://img.youtube.com/vi/0Ds3KqYeXzA/0.jpg" 
alt="Quick Sort" width="720" height="540" border="10" /></a>


* [～～返回目錄～～](#Contents)


## 處理步驟分解
1.  取第一個元素（最左的數）為鍵值 key
2.  由左向右（前向後）找一個數（第一個滿足的），其值大於等於 key 值，該數之索引為 left_pivot
3.  由右向左（後向前）找一個數（第一個滿足的），其值小於等於 key 值，該數之索引為 right_pivot
4.  如果 left_pivot < right_pivot 則交換值，否則把 key 值與 right_pivot 值交換，以 right_pivot 為基準，分為左右兩數列
5. 重複上述步驟排序左右兩個數列，直到完成排序


* [～～返回目錄～～](#Contents)


## 基本程式語法
### 使用額外空間版本：


![Quick_Sort有使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/img/Quick_Sort%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.png "Quick_Sort有使用額外空間")
> 完整程式碼連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/Quick_Sort_%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.ipynb


* [～～返回目錄～～](#Contents)


### 無需額外空間版本：


![Quick_Sort無使用額外空間](https://github.com/chinghsuan/class_exercises/blob/master/img/Quick_Sort_%E7%84%A1%E4%BD%BF%E7%94%A8%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.png "Quick_Sort無使用額外空間")
> 完整程式碼連結：https://github.com/chinghsuan/class_exercises/blob/master/week5/Quick_Sort%E7%84%A1%E9%A1%8D%E5%A4%96%E7%A9%BA%E9%96%93.ipynb


* [～～返回目錄～～](#Contents)


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


* [～～返回目錄～～](#Contents)


## Reference
* [http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)	


* [https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR](https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR)


* [https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html](https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html)

