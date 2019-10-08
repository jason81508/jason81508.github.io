#數字運算, + - * /
x=3+6
print(x)

#整數除法 // 不會運算到小數點
y=3//6 #本來是0.5 運算完是0
print(y)

#開根號 **3(n的三次方)
n=2**2 #開根號**0.5
print(n)

#取餘數%
t=7%3
print(t)

#進階數字運算 先後區隔
u = 2 + 3
print(u)
u = u + 1 #將變數的數字+1
print(u)

##簡便寫法
i = 2 + 3
i+=1
print(i)

#字串運算
s = "hello"
print(s)

#跳脫\
h = "hello\" world"

#字串串接 + 或空白
j = "hello"+"world"
print(j)
k = "hello" "world"
print(k)

#字串換行\n
o = "hello\nworld"
print(o)
##換行方式"""
p = """hello
world"""
print(p)

#字串會對內部的字元編號(或索引) 從0開始
r = "hello"
print (r[0]) #得到h

##進階 獲得子字串
e = "hello"
print (e[1:4]) #得到ell

##進階 給開頭不給結尾
q = "hello"
print(q[1:])
