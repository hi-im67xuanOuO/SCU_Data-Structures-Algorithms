README
===========================
測試並展示書寫README時的各種markdown語法。此語法稱為`GitHub Flavored Markdown`，簡稱`GFM`。除了README外，issues和wiki均支持markdown語法。

## 目錄
* [分隔線Line](#分隔線Line)
* [標題Header](#標題Header)
* [重點Emphasis](#重點Emphasis)
    * [斜體/粗體/刪除線]
* [文本Contents](#文本Contents)
    * [普通文本]
    * [單行文本]
    * [文字強調]
    * [換行]
* [圖片Image](#圖片Image)
    * 來源於網路之圖片
    * GitHub中的圖片
* [連結Link](#連結Link) 
    * 文字超連結
        *  [連結外部URL](#連結外部URL)
        *  [連結GitHub裡的URL](#連結GitHub裡的URL)
    * [圖片連結](#圖片連結)
    * [錨點](#錨點)
* [列表List](#列表List)
    * 無分層列表
    * 有分層列表
    * 帶選框之列表
* [引用Referrence](#引用Referrence)
* [程式碼Code](#程式碼Code)
* [表格Table](#表格Table) 
* [表情符號emoji](#表情符號emoji)
* [diff語法](#diff語法)
* [Youtube影片](#Youtube影片)


## 分隔線Line
```
***、---、___可以顯示横線效果
```

------

## 標題Header
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

## 重點Emphasis
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



## 文本Contents
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


## 圖片Image

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


## 連結Link

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
|1|`![](/img/google_logo.jpg "googel首頁")][google]`|![](/img/google_logo.jpg "google首頁")|

### 錨點
每個標題都是一個錨點，和HTML的`#`類似 

|語法|效果|
|---|---|
|`[回到頂部](#readme)`|[回到頂部](#readme)|

不過要注意，標題中的英文字母都被轉化為**小寫字母**了。


## 列表List
### 無標序列表
#### 語法
```
* 姓名：劉謦瑄
- 英文名字：Liu Ching-hsuan
* Majior：Big Data Management
```
#### 效果
* 姓名：劉謦瑄
- 英文名字：Liu Ching-hsuan
* Majior：Big Data Management

### 多級無標序列表
#### 語法
```
* 巨量資料管理學院
    * Big Data Management
        * 資料結構與演算法
```
#### 效果
* 巨量資料管理學院
    * Big Data Management
        * 資料結構與演算法

### 一級有標序列表
#### 語法
在數字後面加一個點及一個空格。
```
舉例三種程式語言：

1. Python
2. R語言
3. Java
```

#### 效果
舉例三種程式語言：

1. Python
2. R語言
3. Java


### 多層有標序列表
#### 語法
```
1. 这是一级的有序列表，數字1還是1
   1. 這是二级的有序列表，阿拉伯數字顯示時轉換為羅馬數字
      1. 這是三级的有序列表，數字轉換為英文字母
```

#### 效果

1. 这是一级的有序列表，數字1還是1
   1. 這是二级的有序列表，阿拉伯數字顯示時轉換為羅馬數字
      1. 這是三级的有序列表，數字轉換為英文字母
	 

### 複選匡列表
#### 語法
```
- [x] 需求分析
- [x] 系统設計
- [x] 詳細設計
- [ ] 編碼
- [ ] 測試
```
#### 效果

- [x] 需求分析
- [x] 系统設計
- [x] 詳細設計
- [ ] 編碼
- [ ] 測試

> Tip:
>> 在GitHub的**issue**中使用該語法法是可以即時點擊複選框來勾選或取消勾選的，無需修改issue原文。

## 引用Referrence

### 常用於引用文本
> **這是一個引用文本的例子**  
以下文字是為了呈現GitHub中引用文本時呈現的樣子：  
“……東吳大學巨量資料管理學院，108-1資料結構與演算法，GitHub實作Readme撰寫，這裡是引用文本的舉例。......”

### 引用有多層結構
#### 語法
```
> 數據結構
>> 樹
>>> 二叉樹
>>>> 平衡二叉樹
>>>>> 滿二叉樹
```
#### 效果
> 數據結構
>> 樹
>>> 二叉樹
>>>> 平衡二叉樹
>>>>> 滿二叉樹

## 程式碼Code

### 語法
在三個反引號後面加上編程語言的名字，另起一行開始寫程式碼，最後一行再加上三個反引號。

### 效果
```Java
public static void main(String[]args){} //Java
```
```c
int main(int argc, char *argv[]) //C
```
```Bash
echo "hello GitHub" #Bash
```
```javascript
document.getElementById("myH1").innerHTML="Welcome to my Homepage"; //javascipt
```
```cpp
string &operator+(const string& A,const string& B) //cpp
```

## 表格Table

表頭1  | 表頭2|
--------- | --------|
表格內容  | 表格內容 |
表格內容  | 表格內容 |

| 表頭1  | 表頭2|
| ---------- | -----------|
| 表格內容   | 表格內容   |
| 表格內容   | 表格內容   |

### 對齊
可指定對齊方式

| 左對齊 | 居中  | 右對齊 |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |

### 混合其他語法
#### 使用普通文本的刪除線、斜體等效果

| 名字 | 描述 |
| ------------- | ----------- |
| Help      | ~~Display the~~ help window.|
| Close     | _Closes_ a window     |

#### 表格中嵌入圖片（連結）

| 圖片 | 描述 |
| ---- | ---- |
|`![](/img/google_logo.jpg "googel首頁")][google]`|![](/img/google_logo.jpg "google首頁")|

## 表情符號emoji

Github的Markdown語法支持添加emoji表情，輸入不同的符號代碼（兩個冒號包圍的字符）可顯示出不同的表情。

比如`:blush:`，可以顯示:blush:。

具體每一個表情的符号码，可以查詢GitHub的官網[http://www.emoji-cheat-sheet.com](http://www.emoji-cheat-sheet.com)。

## diff語法

展示一文件内容的增加與刪除。使用綠色表示新增，红色表示刪除。
#### 語法
與程式碼類似，只是在三個反引號後面寫diff，並且其内容中，可以用 `+ `開頭表示新增，`- `開頭表示刪除。另外還有 `!`和`#`的語法。

#### 效果

```diff
+ 人閒桂花落，
- 夜静春山空。
! 月出驚山鳥，
# 時鳴春澗中。
```

## Youtube 影片

Youtube 影片無法直接被加入，不過我們可以加入圖片，在圖片上設定連結到影片，像這樣：

```no-highlight
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE影片ID放在這裡
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE影片ID放在這裡/0.jpg" 
alt="圖片 ALT 文字放在這裡" width="240" height="180" border="10" /></a>
```

或是，用單純的 Markdown，不過會無法改變圖片的大小與邊框：


```no-highlight
[![圖片 ALT 文字放在這裡](http://img.youtube.com/vi/YOUTUBE影片ID放在這裡/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE影片ID放在這裡)
```

可以在 `git commit` 裡面用 #bugID 的方式引用一個 bug，比如說 #1。
