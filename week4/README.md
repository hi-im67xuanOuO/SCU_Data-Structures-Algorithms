# week4 - Set & Insertion Sort

## Contents
* [**`Part1-Set`**](#Part1-Set)
   * [簡介Set](#簡介Set)
   * [基礎程式語法與function](#基礎程式語法與function)
   * [實作概念](#實作概念)
   * [Leetcode題目](#Leetcode題目)
      * [155_Min_Stack](#155_Min_Stack)
* [**`Part2-Insertion_Sort`**](#Part2-Insertion_Sort)
   * [簡介Insertion_Sort](#簡介Insertion_Sort)
   * [影片觀念講解](#影片觀念講解)
   * [基礎程式語法與function](#基礎程式語法與function)
   * [實作概念](#實作概念)
   * [Leetcode題目](#Leetcode題目)
      * [155_Min_Stack](#155_Min_Stack)
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


## 實作概念
* **part1-Stack**：包含了pop與append用法
```python

```


## Leetcode題目
### 155_Min_Stack
> 題目：[Leetcode 155. Min_Stack](https://leetcode.com/problems/min-stack/)


#### 完整程式碼
```python

```


## Reference
* [http://www.runoob.com/python/python-func-set.html](http://www.runoob.com/python/python-func-set.html)	


* [https://wenyuangg.github.io/posts/python3/python-set.html](https://wenyuangg.github.io/posts/python3/python-set.html)


* [http://www.runoob.com/python3/python3-set.html](http://www.runoob.com/python3/python3-set.html)

