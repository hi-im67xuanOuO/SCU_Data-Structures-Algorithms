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

------

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

------

##圖片
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
|1|`![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")`|![baidu](data:image/png;base64,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 "GitHub logo")
|2|`![][code-past]`|![][code-past]

注意例2的寫法使用了**URL標示符號**的形式，在[連結](#連結)中有介绍。

------

