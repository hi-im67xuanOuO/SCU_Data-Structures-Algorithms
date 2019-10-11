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
插入排序法（Insertion sort）將數列分成排序與未排序兩部分，未排序數列中的數與已排序數列中之數比較大小，並把其插入已排序數列中適當的位置，比該數大的值則向右（後）移動。也就是說從未排序的數列裡，每次取一個值並逐一和已排序的數列進行比較，並插入到已排序的數列中，適合的位置。
* **時間複雜度(Time Complexity)**：
  * Best Case：Ο(1)，當資料的順序恰好為由小到大時，每回合只需比較1次
  * Worst Case：Ο(n2)，當資料的順序恰好為由大到小時，第i回合需比i次
  * Average Case：Ο(n2)，第n筆資料，平均比較n/2次
* **空間複雜度(Space Complexity)** ：θ(1)
* **穩定性(Stable/Unstable)** ：穩定(Stable)


   ![InsertionSort1](https://runestone.academy/runestone/books/published/pythonds/_images/insertionsort.png
 "InsertionSort1")


> 圖一 
> 圖片來源：[https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html](https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html)


## 影片觀念講解
   <a href="https://www.youtube.com/watch?v=0Ds3KqYeXzA
" target="_blank"><img src="http://img.youtube.com/vi/0Ds3KqYeXzA/0.jpg" 
alt="Quick Sort" width="1440" height="1080" border="10" /></a>

## 處理步驟分解
1. 從第一個元素開始，該元素可以認為已經被排序
2. 取出下一個元素，在已經排序的元素序列中從後向前掃描
3. 如果該元素（已排序）大於新元素，將該元素移到下一位置
4. 重複步驟3，直到找到已排序的元素小於或者等於新元素的位置
5. 將新元素插入到該位置後重複步驟2~5


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

