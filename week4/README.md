# week4 - Set & Insertion Sort

## Contents
* [**`Part1-Set`**](#Part1-Set)
   * [簡介Set](#簡介Set)
   * [基礎程式語法與function](#基礎程式語法與function)
   * [Leetcode題目](#Leetcode題目)
      * [645_Set_Mismatch](#645_Set_Mismatch)
* [**`Part2-Insertion_Sort`**](#Part2-Insertion_Sort)
   * [簡介Insertion_Sort](#簡介Insertion_Sort)
   * [影片觀念講解](#影片觀念講解)
   * [處理步驟分解](#處理步驟分解)
   * [實作概念](#實作概念)
   * [Leetcode題目](#Leetcode題目)
      * [147_Insertion_Sort_List](#147_Insertion_Sort_List)
* [Reference](#Reference)


# Part1-Set
## 簡介Set
集合Set是一個無序的**不重複**元素序列。創建一個空集合時，需使用 **`set()`** 而不是`{}`，{}使用來創造一空字典Dictionary。


## 基礎程式語法與function
* **`add(value)`** = 加入新元素。
* **`remove(value)`** = 移除元素。
* **`len()`** = 回傳set長度。
* **`sum()`** = 回傳set總和。
* **`max()`** = 回傳set中的最大值。
* **`min()`** = 回傳set中的最小值。
* **`in`與`not in`** = 判斷元素是否存在於set中。
* **`issubset()`** = 回傳是否為子集合(subset)。
* **`issuperset()`** = 回傳是否為超集合 (superset)。
* **`discard()`** = 刪除set中指定元素。
* **`clear()`** = 清空set。
* 集合 (Set) 沒辦法使用索引 (Index) 來印出
* 使用 == 與 != 來判斷兩個集合是否相同

|作用|程式碼|其它表示方法|
|----------|-----------|-----------|
| 聯集   | `union`    | x | y |
| 交集   | `intersection`   | x & y |
| 差集   | `difference`   | x - y |
| 對稱差集   | `symmetric_difference`   | |


## Leetcode題目
### 645_Set_Mismatch
> 題目：[Leetcode 645.Set Mismatch](https://leetcode.com/problems/set-mismatch/)


#### 完整程式碼
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        holder = [0]*len(nums)
        repeat_num = 0
        for i in range(len(nums)):
            if holder[nums[i]-1] != 0:
                repeat_num = nums[i]
            holder[nums[i]-1] = nums[i]
        return [repeat_num,holder.index(0)+1]
```


# Part2-Insertion_Sort
## 簡介Insertion_Sort
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
   <a href="https://www.youtube.com/watch?v=lCzQvQr8Utw&feature=youtu.be
" target="_blank"><img src="http://img.youtube.com/vi/lCzQvQr8Utw/0.jpg" 
alt="Insertion Sort" width="720" height="540" border="10" /></a>

## 處理步驟分解
1. 從第一個元素開始，該元素可以認為已經被排序
2. 取出下一個元素，在已經排序的元素序列中從後向前掃描
3. 如果該元素（已排序）大於新元素，將該元素移到下一位置
4. 重複步驟3，直到找到已排序的元素小於或者等於新元素的位置
5. 將新元素插入到該位置後重複步驟2~5


## Leetcode題目
### 147_Insertion_Sort_List
> 題目：[Leetcode 147.Inssertion_Sort_List](https://leetcode.com/problems/insertion-sort-list/)


#### 完整程式碼
```python
class Solution(object):
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        temp = []
        node = head
        while node != None:
            temp.append(node.val)
            node = node.next
        temp.sort()
        node = head
        for n in temp:
            node.val = n
            node = node.next
        return head
```


## Reference
* [http://www.runoob.com/python/python-func-set.html](http://www.runoob.com/python/python-func-set.html)	


* [https://wenyuangg.github.io/posts/python3/python-set.html](https://wenyuangg.github.io/posts/python3/python-set.html)


* [http://www.runoob.com/python3/python3-set.html](http://www.runoob.com/python3/python3-set.html)


* [https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/119168/#outline__3](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/119168/#outline__3)
