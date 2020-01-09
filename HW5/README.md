# HW5 - BFS & DFS（作業五！！）

## Contents
* [我的BFS&DFS程式碼](https://github.com/chinghsuan/class_exercises/blob/master/HW5/BFS_06170203.py)
* [我的學習歷程](https://github.com/chinghsuan/class_exercises/blob/master/HW5/%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.md)
* [DFS與BFS原理與比較](#DFS與BFS原理與比較)
  * [BFS](#BFS)
  * [DFS](#DFS)
* [Reference](#Reference)

## DFS與BFS原理與比較
### BFS
* **`BFS（廣度優先搜尋 Breadth-first Search）`**：又稱**寬度優先搜尋**，或**橫向優先搜尋**，是一種圖形搜尋演算法。從根節點開始，沿著樹的寬度遍歷樹的節點。如果所有節點均被存取，則演算法中止。距離原點相同的節點的訪問順序是相近的。
  * **`時間複雜度`**：O(V+E)（分別遍歷所有節點和其所有連結之節點）
  * **`空間複雜度`**：O(v)（Queue中最多可能存放所有節點）
  * **`特性`**：
    1. 用於有效率的迭代(traversal)
    2. 迭代的方式為鄰近的先訪問(level-ordered)
    3. 使用FIFO的Queue來實作，Queue為空時，代表完成迭代
  * **`優點`**：
    1. 求最短路徑時不會像def需反覆經過相同的狀態，因此此時bfs勝過dfs。
  * **`缺點`**：
    1. 會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間，因此有時用DFS替代。
  * **`應用範圍`**：
    1. machine learning
    2. Edmonds-Karp演算法
    3. Cheney演算法
  
### DFS
* **`DFS（深度優先搜尋 Depth-first Search）`**：從根節點開始，逐個訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個回溯前驅節點。使用棧儲存未被檢測的節點，節點按照深度優先的次序被訪問並依次被壓入棧中，並以相反的次序出棧進行新的檢測。
  * **`時間複雜度`**：O(V+E)（分別遍歷所有節點和其所有連結之節點）
  * **`空間複雜度`**：O(logV)（訪問至末端節點後LIFO，Stack最多只會同時存在logV個節點，也就是樹的高度）
  * **`特性`**：
    1. 為了解Maze Problem而生的演算法
    2. 效能比BFS稍佳
    3. 使用LIFO的Stack來實作
  * **`優點`**：
    1. 使用遞迴函式程式可以簡潔地進行書寫，狀態管理也很簡單，因此大多數情況仍以dfs解決。
    2. dfs是與遞迴深度成正比的，一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省記憶體。
  * **`缺點`**：
    1. 在求最短路問題時，dfs需要反覆經過同樣的狀態，不管在記憶體或時間複雜度上，此時使用bfs都較好。
  * **`應用範圍`**：
    1. 拓撲排序 Topological Order
    2. Kosaraju演算法
    3. 推薦系統 Recommand System
    4. 判斷Grapth是否有cycle(DAG)
    5. Maze

## Reference
[Graph: Breadth-First Search(BFS，廣度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html#algorithm)  
[演算法筆記- Graph - 網路郵局](http://www.csie.ntnu.edu.tw/~u91029/Graph.html)  
[(DFS)和廣度優先搜尋(BFS) - MagicLen](https://magiclen.org/dfs-bfs/)  
[bfs及dfs的比較](https://www.itread01.com/content/1541297601.html)  
