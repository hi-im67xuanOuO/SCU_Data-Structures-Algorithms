# HW2 - Heap Sort & Merge Sort（作業二！！）

## Contents
* [Heap_Sort簡介](#Heap_Sort簡介)
  * Heap_Sort學習歷程、文字描述、流程圖：[連結](#Heap_Sort與Merge_Sort的比較)
* [Merge_Sort簡介](#Merge_Sort簡介)
  * Merge_Sort學習歷程、文字描述、流程圖：[連結](#Heap_Sort與Merge_Sort的比較)
* [Heap_Sort與Merge_Sort的比較](#Heap_Sort與Merge_Sort的比較)
* [Reference](#Reference)

## Heap_Sort簡介
1. 可分為Max-Heap和Min-Heap
2. 有insert與delete兩種操作方式
3. 建立方式：a. Top-down b. Bottom-up(shiftdown)
我的更多文字說明：[連結](#https://github.com/chinghsuan/class_exercises/blob/master/HW2/heap_sort_06170203_%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E%EF%BC%88%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%EF%BC%89.ipynb)

## Merge_Sort簡介
1. MergeSort是一種高效率、較穩定的演算法。  
2. 概念：將兩個已排序過的記錄合併，而得到另一個排序好的記錄。
3. 可分為兩種類型:a. Recursive (遞迴) b. Iterative (迴圈, 非遞迴)
4. 不論是遞迴或是非遞迴方式，都需要暫時性的陣列空間，目的是用來暫存每回合Merge後的Run之結果。
我的更多文字說明：[連結](#Heap_Sort與Merge_Sort的比較)


## Heap_Sort與Merge_Sort的比較
* 時間複雜度與空間複雜度比較：

| 排序方法 | Worst complexity  | Average complexity | Best complexity | Space complexity | Stable 
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ 
| Heap Sort      | nlog(n) | nlog(n)  | nlog(n) | 1 | No 
| Merge Sort      | nlog(n)  | nlog(n) | nlog(n) | n | Yes 

1. 理論上，MergeSort還是要比HeapSort來得快速，雖然兩者的Worst complexity都為O(nlogn)，但是HeapSort是in-place的排序法，不需要像MergeSort每次都要跟記憶體求取一塊位置暫存，所以整理來說，HeapSort在某些情況下，還是比MergeSort來得好的。  
2. n 愈大，Merge所需的暫存空間就愈多，因此額外的空間需求與 n 成正比。

## Reference
https://medium.com/@randerson112358/sorting-algorithms-6005e9ddd8c0
