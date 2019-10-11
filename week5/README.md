# week5 - Quick Sort

## Contents
* [簡介Quick_Sort](#簡介Quick_Sort)
* [影片觀念講解](#影片觀念講解)
* [處理步驟分解](#處理步驟分解)
* [實作概念](#實作概念)
* [Leetcode題目](#Leetcode題目)
  * [148_Sort_List](#148_Sort_List)
* [Reference](#Reference)


## 簡介Quick_Sort
快速排序法（Quick sort）運用到 Divide and conquer 的概念：先找一個基準點（key），然後派兩個代理人分別從資料的兩邊開始往中間找，如果右邊找到一個值比基準點小，左邊找到一個值比基準點大，就讓他們互換。反覆此動作直到兩個點相遇。然後再將相遇的點值與基準點互換，第一輪結束。如此重複遞迴，把數列一分為二，直到最終完成排序。

* **時間複雜度(Time Complexity)**：
  * Best Case：
  * Worst Case：
  * Average Case：
* **空間複雜度(Space Complexity)** ：
* **穩定性(Stable/Unstable)** ：


   ![QuickSort](https://pic.pimg.tw/jialin128/1467645871-4201784417_n.png "QuickSort")


> 圖一 
> 圖片來源：[http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python](http://jialin128.pixnet.net/blog/post/142927691-%5B-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5D-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)


## 影片觀念講解
   <a href="https://www.youtube.com/watch?v=0Ds3KqYeXzA
" target="_blank"><img src="http://img.youtube.com/vi/0Ds3KqYeXzA/0.jpg" 
alt="Quick Sort" width="720" height="540" border="10" /></a>

## 處理步驟分解
1.  取第一個元素（最左的數）為鍵值 key
2.  由左向右（前向後）找一個數（第一個滿足的），其值大於等於 key 值，該數之索引為 left_pivot
3.  由右向左（後向前）找一個數（第一個滿足的），其值小於等於 key 值，該數之索引為 right_pivot
4.  如果 left_pivot < right_pivot 則交換值，否則把 key 值與 right_pivot 值交換，以 right_pivot 為基準，分為左右兩個數列
5. 重複上述步驟排序左右兩個數列，直到完成排序


## Leetcode題目
### 148_Sort_List
> 題目：[Leetcode 148.Sort_List](https://leetcode.com/problems/sort-list/)


#### 完整程式碼
```python

```


## Reference
* [http://www.runoob.com/python/python-func-set.html](http://www.runoob.com/python/python-func-set.html)	


* [https://wenyuangg.github.io/posts/python3/python-set.html](https://wenyuangg.github.io/posts/python3/python-set.html)


* [http://www.runoob.com/python3/python3-set.html](http://www.runoob.com/python3/python3-set.html)


* [https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/119168/#outline__3](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/119168/#outline__3)


* [http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)

