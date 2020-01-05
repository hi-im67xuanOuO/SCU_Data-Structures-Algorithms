# CS50 - Week8

## Contents
* [Stacks](#Stacks)
* [Queues](#Queues)
* [Trees](#Trees)
  * [Binary Search Trees](#Binary_Search_Trees)
* [Reference](#Reference)


### Stacks
* **Stacks**：  
具有「Last-In-First-Out」的資料結構，「最晚進入Stack」的資料會「最先被取出」。
* **優點**：
  1. 對於組織程序的內存很有用
  2. 對於驗證網頁HTML的樹形結構也很有用
  
* **示意圖**：


![image](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/Stack/intro/f1.png)  
> 圖片來源：http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html  

* **一般功能**：
  1. Push(data)：把資料放進Stack。(把書放進箱子。)
  2. Pop：把「最上面」的資料從Stack中移除。(把位於箱子「最上面」的書拿出來。)
  3. Top：回傳「最上面」的資料，不影響資料結構本身。(確認目前位於箱子「最上面」的是哪本書。)
  4. IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。(確認箱子裡面有沒有書。)
  5. getSize：回傳Stack裡的資料個數，不影響資料結構本身。(記錄目前箱子已經裝了多少本書。)
* **應用**：
  1. 編輯器中的undo
  2. 網頁瀏覽器「回到前一頁」功能
  3. 編譯器中的Parsing
  4. 遞迴recursion形式的演算法（因為遞迴使用了系統的Call Stack）
  5. 記憶體管理中的Call Stack


### Queues
* **Queues**：  
具有「First-In-First-Out」的資料結構，如同排隊買車票的隊伍即可視為Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。
* **示意圖**：


![image](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/Queue/intro/queue.gif)  
> 圖片來源：https://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html  

* **一般功能**：
  1. Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。
    1. 在Queue中新增資料又稱為enqueue。
  2. Pop：把front所指向的資料從Queue中移除，並更新front。
    1. 從Queue刪除資料又稱為dequeue。
  3. getFront：回傳front所指向的資料。
  4. getBack：回傳back所指向的資料。
  5. IsEmpty：確認Queue裡是否有資料。
  6. getSize：回傳Queue裡的資料個數。
* **應用**：
  1. 作業系統：被多個程式共享的資源(例如CPU、印表機、網站伺服器)，一次只能執行一個需求(例如request、interrupt)，因此需要有個Queue來安排多個程式的執行順序(例如device queue、job queue)
  
### Trees
### Binary_Search_Trees

## Reference
http://www.youtube.com/watch?v=9qvt6MwBKZQ  
http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html  
https://www.youtube.com/watch?v=ihmHDZKOkA8  
https://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html  
