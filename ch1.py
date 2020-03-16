a = 123
b = 123.456
c = "Python"
d = 'python'

print("a =",a)
print("b =",b) 
print("c =",c,end=' ') #讓print出來的東西不要換行
print("d =",d,end='*') #也可空多格或加上不同字元
print("f =",d)
print()

#format格式化輸出，字串的預設是靠左對齊，而整數和浮點數是靠右對齊，可用>或<符號控制對齊機制
print(format(a,'5d')) #print表示跳一空白行 #5d表示5個欄位寬，d表示一整數
print(format(b,'10.2f')) #f表示浮點數，10.2表示後面有2位小數點，有10個欄位寬(包含小數點)
print(format(c,'10s')) #s表示字串，且欄位寬為10
print()
print(format(a,'<5d')) #<為靠左對齊
print(format(b,'<10.2f')) 
print(format(c,'>10s')) #>為靠右對齊
print(format(c,'^10s')) #^為置中對齊
print()

#print('%格式化字符'%(variable_list))
#以%為開頭，後接格式化字符，可為d/f/s，預設皆為靠右對齊，若要靠左可加-號
print('%5d'%(a))
print('%10.2f'%(b))
print('%10s'%(c))
print()
print('%-5d'%(a))
print('%-10.2f'%(b))
print('%-10s'%(c))
print()

print('|%5d|'%(a))
print('|%10.2f|'%(b))
print('|%10s|'%(c))
print()
print('|%-5d|'%(a))
print('|%-10.2f|'%(b))
print('|%-10s|'%(c))
print()

#format格式化中亦可用x/o/b表示十六進位、八進位、二進位，但%格式化輸出中就沒有二進位機制
print(format(a,'5x'))
########print(format(b,'5o')) #?????????
print(format(a,'5b'))
print()
print('%5x'%(a))
print('%5o'%(a))
print()




x = 123
y = 123456
z = 12
p = 12
q = 123
r = 123456

print(x,y,z)
print(p,q,r)
print()

#using format
print(format(x,'8d') ,format(y,'8d') ,format(z,'8d'))
print(format(p,'8d') ,format(q,'8d') ,format(r,'8d'))
print()

#using %
print('%8d %8d %8d'%(x,y,z))
print('%8d %8d %8d'%(p,q,r))
print()

#轉義字元
print('Python\"Kptlin') #\" = "
print('Python\'Kptlin') #\' = '
print('Python\\Kptlin') #\\ = \
print('Python\tKptlin') #\t = 跳八格
print('Python\nKptlin') #\n = 換行

#輸入函示
a = input('Enter a number:')
print(a)
a,b = eval(input('Enter two numbers:'))
print('a=%d,b=%d'%(a,b))

#算術運算子
a = 100
b = a/3 #除 結果是浮點數
c = a//3 #除 結果是整數
f = a%3 #兩數相除，取餘數
d = a**2 #次方
e = a**0.5
print(a,b,c,f,d,e)
print()

#math數學模組下的函式
import math
print(math.pi)
print(math.e)
print(math.ceil(3.2)) #大於該數的最小整數
print(math.floor(3.2)) #小於該數的最大整數
print(math.fabs(-123.45)) #浮點數的絕對值
print(math.exp(2)) #e^x
print(math.log(10)) #loge(x)
print(math.log(100,10)) #logbase(x)
from math import sqrt
print(sqrt(100)) #x^0.5
print(math.sin(0))
print(math.cos(0))
print()

