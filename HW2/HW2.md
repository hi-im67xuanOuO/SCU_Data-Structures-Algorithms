# HW2 - Heap Sort & Merge Sort（作業二！！）

## Contents
* [Heap_Sort簡介](#Heap_Sort簡介)
  * Heap_Sort學習歷程、文字描述、流程圖：[連結](#Heap_Sort與Merge_Sort的比較)
* [Merge_Sort簡介](#Merge_Sort簡介)
  * Merge_Sort學習歷程、文字描述、流程圖：[連結](#Heap_Sort與Merge_Sort的比較)
* [Heap_Sort與Merge_Sort的比較](#Heap_Sort與Merge_Sort的比較)
* [Reference](#Reference)

## Heap_Sort簡介

## Merge_Sort簡介
MergeSort是一種高效率、較穩定的演算法。
## Heap_Sort與Merge_Sort的比較
* 時間複雜度與空間複雜度比較：

| 排序方法 | Worst complexity  | Average complexity | Best complexity | Space complexity | Stable 
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ 
| Heap Sort      | nlog(n) | nlog(n)  | nlog(n) | 1 | No 
| Merge Sort      | nlog(n)  | nlog(n) | nlog(n) | n | Yes 

`理論上，MergeSort還是要比HeapSort來得快速，雖然兩者的Worst complexity都為O(nlogn)，但是HeapSort是in-place的排序法，不需要像MergeSort每次都要跟記憶體求取一塊位置暫存，所以整理來說，HeapSort在某些情況下，還是比MergeSort來得好的。`

## Reference
https://medium.com/@randerson112358/sorting-algorithms-6005e9ddd8c0
