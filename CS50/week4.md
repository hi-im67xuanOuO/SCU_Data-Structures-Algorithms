# CS50 - Week4

## Contents
* [Merge Sort](#Merge_Sort)
* [證明合併排序法的時間複雜度](#證明合併排序法的時間複雜度)
* [Recursion遞迴](#Recursion遞迴)
* [Reference](#Reference)


## Merge_Sort
* **原理與介紹**：**合併排序法**，採用分治法（Divide and Conquer）的一個非常典型的應用，且各層分治遞迴可以同時進行。分治法分為兩部份：
1. 分割：遞迴地把目前序列平均分割成兩半。  
2. 整合：在保持元素順序的同時將上一步得到的子序列整合到一起（合併）。  
* **步驟**：
合併排序需要額外空間存儲list，所以通常我們要在速度與資源之間進行權衡。  
* 遞迴法（Top-down）：
1. 申請空間，使其大小為兩個已經排序序列之和，該空間用來存放合併後的序列
2. 設定兩個指標，最初位置分別為兩個已經排序序列的起始位置
3. 比較兩個指標所指向的元素，選擇相對小的元素放入到合併空間，並移動指標到下一位置
4. 重複步驟3直到某一指標到達序列尾
5. 將另一序列剩下的所有元素直接複製到合併序列尾
* 疊代法（Bottom-up）：
 1. 將序列每相鄰兩個數字進行合併操作，形成n/2個序列，排序後每個序列包含兩/一個元素
 2. 若此時序列數不是1個則將上述序列再次合併，n/4個序列，每個序列包含四/三個元素
 3. 重複步驟2，直到所有元素排序完畢，即序列數為1
* **時間複雜度（最壞）**：O(nlogn)  
原因：logn的部分是因為將數值分割為2，n的部分是合併。
* **pseudocode**：
```
On input of n elements:
    If n < 2
        Return.
    Else:
        Sort left half of elements.
        Sort right half of elements.
        Merge sorted halves.
```
* **示意圖**：


![image](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif)  
> 圖片來源：https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F  


* **舉例**：
CS50課程舉了一個例子，現在我們擁有一個42613758的序列，接下來我們要將他們進行合併排序法： 
首先是進行分割的部分，我們針對左半部進行分割舉例：  
1. 4261 3758
2. 42 613758
3. 4 2613758
分割到只剩下1個元素即停止分割，所以我們回溯至剛剛切割的list，將4與2進行排序，並將排序結果放入新的list：  
4. 24 _ _ _ _ _ _ / _ _ 613758
5. 2416 _ _ _ _ / _ _ _ _ 3758
6. 1246 _ _ _ _ / _ _ _ _ 3758
7. 12463758（將步驟6合併，左半邊排序完成。接下來開始進行右半邊排序）
8. 1246 _ _ 58 / _ _ _ _ 37 _ _
9. 1246 _ _ _ _ / _ _ _ _ 3758
10. 1246 _ _ _ _ / _ _ _ _ 3578（對右半邊排序）
11. 12463578（將兩半邊再次合併）
12. 12345678（合併並排序，完成！）

## 證明合併排序法的時間複雜度
![image](https://github.com/chinghsuan/class_exercises/blob/master/img/CS50-%E8%AD%89%E6%98%8Emergesort%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6.jpg)  


## Recursion遞迴
* **Recursion遞迴**：在一個函式當中再去呼叫它自己，其中一個實際的範例就是階層的計算（factorial）。呼叫者本身會先被置入記憶體堆壘中，等到被呼叫者執行完畢之後，再從堆壘中取出之前被置入的函式繼續執行。堆疊（Stack）是一種「先進後出」的資料結構，就好比您將書本置入箱中，最先放入的書會最後才取出。

## Reference
http://cdn.cs50.net/2013/fall/lectures/4/m/week4m.pdf  
https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F  
http://www.youtube.com/watch?v=8IZ9r5kmS3Y  
http://www.youtube.com/watch?v=lw1U7CvmjoU  
https://pjchender.blogspot.com/2017/09/recursive-function-recursion.html

