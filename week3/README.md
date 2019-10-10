# week3 - Stack & Queue

## Contact
* [簡介Stack及Queue](#簡介Stack及Queue)
    * [Stack](#Stack)
    * [Queue](#Queue)
* [影片觀念講解](#影片觀念講解)
* [基礎程式語法與function](#基礎程式語法與function)
* [實作概念](#實作概念)
* [Leetcode題目](#Leetcode題目)
    * [155_Min_Stack](#155_Min_Stack)
    * [232_Implement-Queue-Using-Stacks](#232_Implement-Queue-Using-Stacks)
* [Reference](#Reference)


## 簡介Stack及Queue
Stack和Queue是兩個使我們能簡單地依序檢索和儲存數據的結構。在Stack中，我們輸入的最後一個元素會是第一個被顯示出來的元素。在Queue中，我們輸入的第一個元素則會是第一個被顯示的元素。我們可以使用`push`將項目添加到Stack中，並使用`pop`操作來檢索項目。對於Queue，我們使用`enqueue`來添加項目，並使用`dequeue`檢索項目。


### `Stack`
* **遵循LIFO原則**：Last-in-First-out原則，就像一個硬幣堆在另一個硬幣上，最後一個被放在頂部的硬幣，會是第一個要從堆疊中移除的硬幣。
* 在高階程式語言，通常用array、linked list來實作。
* 大部分的程式語言都是Stack-Oriented，因為仰賴堆疊來處理method call(呼叫堆疊, Call Stack)。
* 應用例子：瀏覽器回上一頁、PhotoShop上一步(undo)
* Stack特性：有限的記憶體配置空間、存活時間規律可預測的

* 下圖為兩個Stack的基本操作：
    * **`push`**：將元素添加至Stack頂部。

      ![Stack1](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-1.jpg "Stack1")


    * **`pop`**：將Stack最頂部的元素刪除。

      ![Stack1](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-2.jpg "Stack2")


> 圖片來源：[https://stackabuse.com/stacks-and-queues-in-python/](https://stackabuse.com/stacks-and-queues-in-python/)


### `Queue`
* **遵循FIFO原則**：Fast-in-First-out原則，就像排隊等候進場一樣，第一個排隊的人會是能夠優先進場的人。
* 在高階程式語言，通常用array、linked list來實作。
* 應用例子：多個程序的資源共享，例如CPU排程

* 下圖為兩個Queue的基本操作：
    * **`enqueue`**：將元素添加至Queue尾端。

      ![Queue1](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-3.jpg "Queue1")


    * **`dequeue`**：將Queue最前端的元素刪除。

      ![Queue2](https://s3.amazonaws.com/stackabuse/media/stacks-and-queues-in-python-4.jpg "Queue2")


> 圖片來源：[https://stackabuse.com/stacks-and-queues-in-python/](https://stackabuse.com/stacks-and-queues-in-python/)
    
    
## 影片觀念講解
<a href="https://www.youtube.com/watch?v=wjI1WNcIntg" target="_blank"><img src="http://img.youtube.com/vi/wjI1WNcIntg/0.jpg" 
alt="Stack&Queue" width="720" height="540" border="10" /></a>


## 基礎程式語法與function
### `Stack`
* **`Push(Data)`** = 把資料放進Stack。ex:把書放進箱子。
* **`pop`** = 把Stack中最上層的資料移除。ex:把箱子中最上面的書拿出。
* **`top`** = 回傳Stack最上面的資料。ex:確認箱子中最上面的是哪本書。
* **`isEmpty`** = 確認Stack中是否有資料。ex:確認箱子中是否有書。
* **`getSize`** = 回傳Stack中的資料個數。ex:記錄目前箱子中有多少本書。


### `Queue`
* **`Push(Data)`** = 把資料從「最後面」放進Queue，形成新的back。ex:新來的人要從後面排隊，成為隊伍新的最後一個人。
* **`pop`** = 把front所指向的資料從Queue中移除，更新新的front。從Queue中刪除資料又稱為dequeue。
* **`getFront`** = 回傳front所指向的資料。
* **`getBack`** = 回傳back所指向的資料。
* **`isEmpty`** = 確認Queue中是否有資料。ex:確認隊伍中是否有排隊者。
* **`getSize`** = 回傳Queue中的資料個數。ex:記錄目前隊伍中有多少人。


## 實作概念
* **part1-Stack**：包含了pop與append用法
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```


* **part2-Queue**：定義出各種資料結構操作的list本身
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```


## Leetcode題目
### 155_Min_Stack
> 題目：[Leetcode 155. Min_Stack](https://leetcode.com/problems/min-stack/)


#### 完整程式碼
```python

```


### 232_Implement-Queue-Using-Stacks
> 題目：[Leetcode 232.Implement-Queue-Using-Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)


#### 完整程式碼
```python

```



## Reference
* [https://stackabuse.com/stacks-and-queues-in-python/](https://stackabuse.com/stacks-and-queues-in-python/)	


* [https://www.101computing.net/stacks-and-queues-using-python/](https://www.101computing.net/stacks-and-queues-using-python/)


* [https://docs.python.org/zh-tw/3/tutorial/datastructures.html](https://docs.python.org/zh-tw/3/tutorial/datastructures.html)


* [https://super9.space/archives/1105#%E7%B0%A1%E4%BB%8B](https://super9.space/archives/1105#%E7%B0%A1%E4%BB%8B)
