# week8 - Binary Tree

## Contents
* [Binary Tree介紹](#BinaryTree介紹)
* [Reference](#Reference)

## BinaryTree介紹
### Binary Tree
* **`BinaryTree`**：廣義的樹(Tree)對於樹上的node之child數目沒有限制，因此，每個node可以有無限多個child。若限制node只能有兩個child，等於「樹上的每一個node之degree皆為2」，即稱為Binary Tree(二元樹)，並稱兩個child pointer為left child和right child。  
比較嚴謹的定義如下：  
1. 每個節點最多有兩個子節點。
2. 子節點有左右之分。  
當然原來樹的定義也是要繼承下來。


在二元樹中也定義了一些專有名詞，解釋如下：
### **完滿二元樹(Full binary tree)**：
或稱滿二元樹，每個節點有0或2個子節點。也稱作嚴格二元樹(Strictly binary tree)、正規二元樹(Proper binary tree)或2-tree。範例如下：  
![tree1](https://pic.pimg.tw/emn178/1354416995-423540251.png "tree1")


### **完全二元樹(Complete binary tree)**：
除了最後一階層之外的階層都必須填滿，而最後一階層的節點必須由左至右填入。範例如下：  
![tree1](https://pic.pimg.tw/emn178/1354416995-423540251.png "tree1")

 
### **完滿二元樹(Full binary tree)**：
或翻譯滿二元樹，每個節點有0或2個子節點。也稱作嚴格二元樹(Strictly binary tree)、正規二元樹(Proper binary tree)或2-tree。範例如下：  
![tree1](https://pic.pimg.tw/emn178/1354416914-2701915548_n.png "tree1")

 
### **完美二元樹(Perfect binary tree)**：
同時滿足完滿二元樹的條件，並且所有的葉節點都在同一個階層。範例如下：    
![tree1](https://pic.pimg.tw/emn178/1354416838-422111732.png "tree1")

在這個定義下可以得知，完美二元樹也必定是完全二元樹。另外他也同時具有下面數學特性：
一棵深度為d的完美二元樹，其節點數為2d - 1。


### **歪斜二元樹(Skewed binary tree)**：
或翻譯作偏斜二元樹，都所有節點都只有同一邊的子節點的時候，就稱為歪斜二元樹，都只有左子節點的時候稱為左歪斜二元樹；都只有右子節點的時候稱為右歪斜二元樹。範例如下：    
![tree1](https://pic.pimg.tw/emn178/1354417492-1918786445.png "tree1")

## Reference
https://emn178.pixnet.net/blog/post/94164966
https://en.wikipedia.org/wiki/Binary_tree
