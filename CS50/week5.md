# CS50 - Week5

## Contents
* [Stack](#Stack)
* [Heap](#Heap)
* [Stack與Heap的示意圖](#Stack與Heap的示意圖)
* [Stack與Heap的比較](#Stack與Heap的比較)
* [關於圖片的存儲](#關於圖片的存儲)
* [Reference](#Reference)


### Stack
* **Stack**：是內存的一部分，中文叫做**堆疊**，是一種讓資料後進先出、或說讓資料先進後出的資料組織方式。區域變數、函式的參數與函式的位址等等，由系統管理，必須在編譯時期為已知。這些變數的回收會發生在它從堆疊pop出去的時候，因為個數、大小什麼的都是已知，所以系統知道怎麼進行配置與回收。

### Heap
* **Heap**：中文叫做**堆積**。這裡的記憶體由使用者負責進行回收，配置則是由malloc或是new來負責。使用這裡的記憶體主要是用在編譯時期還不知道大小或個數的變數。例如說，你需要用一個陣列，這個陣列的大小要在執行的時候由使用者的輸入來決定，那你就只能使用動態配置，也就是把這個陣列配置在heap中。


### Stack與Heap的示意圖


![image](http://cdn.cs50.net/2013/fall/lectures/5/w/notes5w/program_memory.png)  
> 圖片來源：http://cdn.cs50.net/2013/fall/lectures/5/w/week5w.pdf


### Stack與Heap的比較
* **Stack**：給程式呼叫function時存放function資料用。
  * 快速訪問
  * 不必顯式取消分配變量
  * CPU有效管理空間，內存不會變得零散
  * 僅局部變量
  * 堆棧大小限制（取決於OS）
  * 變量無法調整大小
* **Heap**：用來存放並且管理程式全部所需要用檔的變數與資料。
  * 變量可以全局訪問
  * 內存大小無限制
  * （相對）訪問速度較慢
  * 無法保證有效利用空間，隨著時間的推移，內存塊可能會隨著內存塊的分配而碎片化，然後釋放
  * 必須管理內存（分配和釋放變量）
  * 變量可以使用 realloc()
  
  
### 關於圖片的存儲
存儲圖片有許多不同的格式可以選擇。其中一種選擇是**bitmap（BMP）**，  
這種格式使用0表示黑色，1表示白色，因此一系列的0與1數列可以存儲黑白圖像。  

## Reference
http://www.youtube.com/watch?v=IEuvKVjw2oM  
http://cdn.cs50.net/2013/fall/lectures/5/w/week5w.pdf  
https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html  
