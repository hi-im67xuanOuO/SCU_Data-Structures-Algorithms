# CS50 - Week0

## Contents
* [簡介二進位制與文字編碼](#簡介二進位制與文字編碼)
* [簡介二進位制與文字編碼](#簡介二進位制與文字編碼)
* [Reference](#Reference)


## 簡介二進位制與文字編碼
* **Binary**：為了表示更多更大的數字，我們可以使用這個概念。將每個位數以兩個可能的值（也就是0和1）表示。當有兩位數時，即可表示2 * 2個可能的數值；三位時，可表示2 * 2 * 2個可能的值。
* **ASCII**：這是一種編碼系統，具有每個字母字符代表的數字為何。例如：大寫A由數字65表示，大寫Z以數字90表示。使用此編碼系統可以統一各種文字表達的方式。


## 演算法Algorithms
* 為何要使用演算法？：影片中以電話簿為例，當我們要從一本厚重的電話簿裡尋找到特定的聯絡人，在資訊尚未發達的年代，我們必須慢慢從電話簿中搜尋，但當有了演算法這個概念後，我們可以更快速、有效率的解決這個問題。例如：我們可以將電話簿直接翻到中間，確定該聯絡人在字母表的左半部分，我們接下來就可以僅查找左半部分的電話簿就好，重複執行前述的這個邏輯，直到找到聯絡人為止。而時間的比較如下圖：  
![image](http://cdn.cs50.net/2013/fall/lectures/0/w/notes0w/runtimes.png)  




### Heap_Sort
1. 可分為Max-Heap和Min-Heap
2. 有insert與delete兩種操作方式
3. 建立方式：a. Top-down b. Bottom-up(shiftdown)  
我的更多文字說明：[連結](https://github.com/chinghsuan/class_exercises/blob/master/HW2/heap_sort_06170203_%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E%EF%BC%88%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%89.ipynb)


### 時間複雜度與空間複雜度比較：

| 排序方法 | Worst complexity  | Average complexity | Best complexity | Space complexity | Stable 
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ 
| Heap Sort      | nlog(n) | nlog(n)  | nlog(n) | 1 | No 
| Merge Sort      | nlog(n)  | nlog(n) | nlog(n) | n | Yes 


## Reference
https://medium.com/@randerson112358/sorting-algorithms-6005e9ddd8c0  
http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php

