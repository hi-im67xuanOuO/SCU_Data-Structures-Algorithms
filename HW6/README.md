# HW6 - Dijkstra & Kruskal（作業六！！）

## Contents
* [我的Dijkstra&Kruskal程式碼](https://github.com/chinghsuan/class_exercises/blob/master/HW6/Dijkstra_06170203.py)
* [我的學習歷程](https://github.com/chinghsuan/class_exercises/blob/master/HW6/%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E5%8E%9F%E7%90%86%E8%AA%AA%E6%98%8E.md)
* [Kruskal與Dijkstra原理](#Kruskal與Dijkstra原理)
  * [Kruskal](#Kruskal)
  * [Dijkstra](#Dijkstra)
* [Reference](#Reference)

## Kruskal與Dijkstra原理
### Kruskal
* **`Kruskal（克魯斯克爾演算法）`**:，是一種用來尋找**最小生成樹**的演算法，以增加邊的觀念做為出發點。「生成樹」。從一張圖取出一棵樹，包含圖上所有點。可能有許多種。當一張圖完全連通，則擁有生成樹。當一張圖不連通，則沒有生成樹，而是擁有許多棵「生成子樹」構成的「生成森林」。
  * **`時間複雜度`**：O(ElogV)（E為圖的邊V為圖的點）
  * **`原理`**： 首先將所有的邊，依照權重的大小排序。再來依序加入權重最小的邊，如果造成cycle時，則必須捨棄，直到增加了n-1條邊為止。(假設有 n 個節點)。
  * **`概略步驟`**：
    1. 圖上每一個點，各自是一棵最小生成子樹MSS。
    2. 圖上所有邊，依照權重大小，由小到大排序。
    3. 嘗試圖上所有邊，作為最小生成樹（森林）的邊：
       3-1. 兩端點分別位於兩棵MSS，也就是產生了橋：用這條邊連結兩棵MSS，合併成一棵MSS。這條邊是最小生成樹（森林）上的邊。
       3-2. 兩端點皆位於同一棵MSS，也就是產生了環：捨棄這條邊。
  * **`應用範圍`**：最小生成樹的目的是建立最經濟的聯通子圖。可以有以下應用:
    1. 城市之間的交通系統
    2. 石油管道規劃
  
### Dijkstra
* **`Dijkstra（戴克斯特拉算法）`**：使用了廣度優先搜尋解決賦權有向圖的單源最短路徑問題。以某一節點為出發點，計算從該節點出發到所有其他節點的最短路徑。。
  * **`時間複雜度`**：O(E+VlogV)
  * **`原理`**：每次新擴展一個距離最短的點，更新與其相鄰的點的距離。當所有邊權都為正時，由於不會存在一個距離更短的沒擴展過的點，所以這個點的距離永遠不 會再被改變，因而保證了演算法的正確性。不過根據這個原理，用Dijkstra求最短路的圖不能有負權邊，因為擴展到負權邊的時候會產生更短的距離，有可能就破壞了已經更新的點距離不會改變的性質。
  * **`概略步驟`**：
    1. 將所有頂點分為兩個部分：已知最短路徑的頂點集合 P 和未知最短路徑的頂點集合 Q。一開始，P 中只有一個源點為已知點，所以用另一個 book[i] 陣列來將源點做記號為 1，表示在 P 之中為已知。若 book[i] = 0 的話表示這個頂點 i 為未知，還在 Q 之中。
    2. 設定源點 s 到自己的最短路徑為 0 (dis[s] = 0)。如果 s 能到其他點 i，則把路徑 e[s][i] 存到 dis[i] 之中。若 s 不能到的頂點，路徑 e[s][i] = ∞。
    3. 在集合 Q 中找一個頂點 u 離源點 s 最近，將 u 加入到 P 為已知中。並以 u 為起點對其他邊進行鬆弛，比較從 s → u → v 的路徑能否比 s → v 短，可以的話則更新。
    4. 重複步驟 3 直到集合 Q 為 0。最終的 dis 陣列就是源點到所有頂點的最短路徑了。
  * **`應用範圍`**：
    1. 找到兩個城市之間的最短路徑。

## Reference
[克魯斯克爾演算法-維基百科](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)  
[Minimum Spanning Tree：Kruskal's Algorithm](http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html)  
[代克思托演算法 (Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)  
[戴克斯特拉算法-維基百科](https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)  
