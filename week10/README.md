# week10 - Red Black Tree

## Contents
* [Red Black Tree介紹](#RedBlackTree介紹)
* [Reference](#Reference)

## RedBlackTree介紹
### Red Black Tree
* **`Red Black Tree`**：紅黑樹（Red Black Tree）是一棵二叉查詢樹，在每個節點增加一個屬性表示節點顏色，值為紅色（Red）或者黑色（Black）。紅黑樹也是“平衡”樹中的一種，通過對任何一條從根到葉子的路徑上各個節點的顏色來進行約束，確保沒有一條路徑會比其他路徑長出2倍，因而是“近似平衡”的。對平衡性的要求相較於AVL樹更寬鬆。  

一個紅黑樹具有一下特性：  
* 每個 node 只有黑與紅
* Root 必須是黑
* 每個葉子（leaf）是 NIL 且為黑
* 如果一個 node 是紅，那他的 child 都會是黑
* 每一條從 root 到 leaf 的路徑所包含的黑色 node 數量都一樣

![tree1](https://raw.githubusercontent.com/alrightchiu/SecondRound/master/content/Algorithms%20and%20Data%20Structures/Tree%20series/RBT_fig/Intro/f6.png "tree1")

在說明Rotation(旋轉)之前有兩點需要先申明：  
1.	若是要應用在BST上，則Rotation(旋轉)前後的BST必須要維持相同之Key排序。此處介紹的Rotation(旋轉)便屬於此類。  
2.	Rotation(旋轉)與node是否具有顏色無關，即使是在一般的BST，亦能夠使用Rotation(旋轉)來調整height(樹高)。  

關於旋轉可以參考：http://alrightchiu.github.io/SecondRound/red-black-tree-rotationxuan-zhuan.html  

## Reference
https://alrightchiu.github.io/SecondRound/red-black-tree-introjian-jie.html  
http://alrightchiu.github.io/SecondRound/red-black-tree-rotationxuan-zhuan.html  
