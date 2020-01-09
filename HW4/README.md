# HW4 - Hash Table + MD5（作業四！！）

## Contents
* [我的Hash Table程式碼](https://github.com/chinghsuan/class_exercises/blob/master/HW4/hash_table_06170203.py)
* [我的學習歷程](https://github.com/chinghsuan/class_exercises/blob/master/HW4/hash_table_%E4%BD%9C%E6%A5%AD%E8%AA%AA%E6%98%8E%E8%88%87%E6%AD%B7%E7%A8%8B_06170203.ipynb)
* [HashTable雜湊表](#HashTable雜湊表)
* [HashFunction雜湊函數](#HashFunction雜湊函數)
* [Reference](#Reference)

## Hash Table 與 Hash Function 原理
## HashTable雜湊表
亦稱「哈希表」，是根據鍵（Key）而直接查詢在內存存儲位置的資料結構。  
它通過計算一個關於鍵值的函數，也就是「雜湊函數hash function」，  
將所需查詢的數據映射到雜湊表中一個位置來查詢記錄，此方法加快了查找速度。  

## HashFunction雜湊函數
又稱「雜湊演算法」，能使查詢數據的過程更迅速且準確的方法。  
雜湊函式把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定下來。  
通常用一個短的隨機字母和數字組成的字串來代表。  

關於雜湊函數的幾種方法：  
* 直接定指法：取關鍵字或關鍵字的某個線性函數值為雜湊地址。
* 數字分析法：假設關鍵字是以r為基的數，並且哈希表中可能出現的關鍵字都是事先知道的，則可取關鍵字的若干數位組成哈希地址。
* 平方取中法：取關鍵字平方後的中間幾位為哈希地址。
* 折疊法：將關鍵字分割成位數相同的幾部分（最後一部分的位數可以不同），然後取這幾部分的疊加和（捨去進位）作為哈希地址。
* 隨機數法
* 除留餘數法：取關鍵字被某個不大於雜湊表表長m的數p除後所得的餘數為雜湊地址。
但若數據出現相同的雜湊地址機率是非常高的，此情況被稱為「**衝突**」。  
為了知道衝突產生的相同雜湊函數地址所對應的關鍵字，必須選用另外的雜湊函數，或者對衝突結果進行處理。  
方法有：開放定址法、單獨鍊表法、雙雜湊、再雜湊等等。

## Reference
http://practicalcryptography.com/hashes/md5-hash/  
https://www.cs.wcupa.edu/rkline/ds/hash-sets.html  
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html  
https://toyo0103.blogspot.com/2018/04/hash-table.html  
https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8  
