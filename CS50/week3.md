# CS50 - Week3

## Contents
* [演算法的時間複雜度(Time Complexity)](#演算法的時間複雜度Time_Complexity)
* [Sorting排序](#Sorting排序)
  * [Bubble Sort](#Bubble_Sort)
  * [Selection Sort](#Selection_Sort)
  * [Insertion Sort](#Insertion_Sort)
* [Reference](#Reference)


## 演算法的時間複雜度Time_Complexity
* **時間複雜度？**：一個函式，它定性描述該演算法的執行時間。這是一個代表演算法輸入值的字串的長度的函式。時間複雜度常用大O符號表述。
  * 相同大小的不同輸入值仍可能造成演算法的執行時間不同，因此我們通常使用演算法的**最壞情況複雜度**。
  * **平均情況複雜度**，通常較少使用，通常有特別指定才會使用。

而時間複雜度的比較如下圖：  


![image](http://cdn.cs50.net/2013/fall/lectures/3/w/notes3w/worse_runtimes.png)  

```
橫軸為n，代表資料量大小；y軸表示時間。  
```

## Sorting排序
當資料被有效的排序後，可以加速我們處理資料的效率。從week0的電話簿例子中就可以發現，若排序資料可協助我們直接更有效率的推測出特定資料所在的位置。所以接下來介紹幾種排序方式：  

### Bubble_Sort
* 原理：
* 步驟：
 1. 比較相鄰的元素。如果第一個比第二個大，就交換他們兩個。
 2. 對每一對相鄰元素作同樣的工作，從開始第一對到結尾的最後一對。這步做完後，最後的元素會是最大的數。
 3. 針對所有的元素重複以上的步驟，除了最後一個。
 4. 持續每次對越來越少的元素重複上面的步驟，直到沒有任何一對數字需要比較。
### Selection_Sort
### Insertion_Sort


## Reference
https://zh.wikipedia.org/wiki/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6  


