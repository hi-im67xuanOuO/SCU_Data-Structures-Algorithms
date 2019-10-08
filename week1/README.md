README
===========================
測試並展示書寫README時的各種markdown語法。此語法稱為`GitHub Flavored Markdown`，簡稱`GFM`。除了README外，issues和wiki均支持markdown語法。

## 目錄
* [分隔線](#分隔線)
* [標題Headers](#標題)
* [文本Contents](#文本)
    * [普通文本](#普通文本)
    * [單行文本](#單行文本)
    * [文字強調](#文字強調)
    * [換行](#換行)
    * [斜體/粗體/刪除線](#斜體_粗體_刪除線)
* [圖片Image](#圖片)
    * 來源於網路之圖片
    * GitHub中的圖片
* [連結](#連結) 
    * 文字超連結
        *  連結外部URL
        *  連結GitHub裡的URL
    *  錨點
    * [圖片連結](#圖片連結)
* [列表](#列表)
    * 無分層列表
    * 有分層列表
    * 帶選框之列表
* [引用](#引用)
* [程式碼](#程式碼)
* [表格](#表格) 
* [表情符號](#表情符號)
* [diff語法](#diff語法)


## 分隔線
```
***、---、___可以顯示横線效果
```

------

## 標題
```no-highlight
# H1
## H2
### H3
#### H4
##### H5
###### H6

也可使用下劃線的方式標記 H1 與 H2：

Alt-H1
======

Alt-H2
------
```

# H1
## H2
### H3
#### H4
##### H5
###### H6

也可使用下劃線的方式標記 H1 與 H2：

Alt-H1
======

Alt-H2
------


## 文本
### 普通文本
這是一段普通的文本。
### 單行文本
    這是一段單行文本。
在一行開頭加入1個Tab或者4個空格鍵。
### 文字強調
使部分文字高亮，也適合做一篇文章的tag。語法：
```
`東吳巨資` `資料結構` `演算法` `劉謦瑄` 
```
效果：`東吳巨資` `資料結構` `演算法` `劉謦瑄`

### 換行
可在上一行文本後補兩個空格，  
這樣下一行的文本就換行行了。

或是在兩行文本直接加一個空行。

### 斜體_粗體_刪除線

|語法|效果|
|----|-----|
|`*斜體1*`|*斜體1*|
|`_斜體2_`| _斜體2_|
|`**粗體1**`|**粗體1**|
|`__粗體2__`|__粗體2__|
|`這是一個 ~~刪除線~~`|這是一個 ~~刪除線~~|
|`***斜粗體1***`|***斜粗體1***|
|`___斜粗體2___`|___斜粗體2___|
|`***~~斜粗體刪除線1~~***`|***~~斜粗體刪除線1~~***|
|`~~***斜粗體刪除線2***~~`|~~***斜粗體刪除線2***~~|


## 圖片
------
基本格式：
```
![alt](URL title)
```
alt和title跟HTML中的alt和title屬性相同（都可省略）：
- alt表示圖片顯示失败時的替換文本
- title表示滑鼠停在圖片時顯示的文本（注意這裡要加引號）

URL即圖片的網址，如果引用GitHub中的圖片，直接使用**相對路徑**就可了，如果引用其他GitHub的圖片格式則為：`GitHub地址/raw/分支名/圖片路徑`，如：
```
https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif
```

|#|語法|效果|
|---|---|----
|1|`![GitHub](https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2018/06/04/105/4827699.jpg "GitHub logo")`|![GitHub](https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2018/06/04/105/4827699.jpg "GitHub logo")
|2|`![][code-past]`|![GitHub](https://github.blog/wp-content/uploads/2019/05/facebook-1200x630.png?w=1203)

注意例2的寫法使用了**URL標示符號**的形式，在[連結](#連結)中有介绍。


## 連結
------
### 連結外部URL

|#|語法|效果|
|---|----|-----|
|1|`[Leetcode](https://leetcode.com/ "游標顯示")`|[Leetcode](https://leetcode.com/ "游標顯示")|
|2|`[CodeSignal](https://app.codesignal.com/arcade/intro/level-1) `|[CodeSignal](https://app.codesignal.com/arcade/intro/level-1) |

語法2由兩部分组成：
- 第一部分使用兩個中括號，[ ]裡可以是數字、字母等的组合。
- 第二部分標記實際URL。

### 連結GitHub裡的URL

|語法|效果|
|----|-----|
|`[我的Leetcode紀錄](/Leetcode)`|[我的Leetcode紀錄](/Leetcode)|
|`[README教學](./README.md)`|[README教學](./README.md)|

### 圖片連結

|#|語法|效果|
|---|----|:---:|
|1|`![facebook_logo.jpg](https://www.facebook.com/)`|![facebook_logo.jpg](https://www.facebook.com/)|
|2|`![](/img/google_logo.jpg "googel首頁")][google]`|![](/img/google_logo.jpg "google首頁")|
|3|`![google_logo.jpg]](https://www.google.com.tw/)`|![google_logo.jpg](https://www.google.com.tw/)|

