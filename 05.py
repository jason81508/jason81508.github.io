#集合的運算
test = {3,4,5}
print (3 in test) #3有沒有有在test中 True
print (3 not in test) #3有沒有沒有在test中 Fales

## 交集
test = {3,4,5}
test2 = {5,6,7}
test3 = test&test2 #交集: 取兩個集合中,相同資料
print (test3)

## 聯集
test = {3,4,5}
test2 = {4,5,6,7}
test3 = test|test2 #聯集: 取兩個集中的所有資料,但不重複
print (test3)

##差集
test = {3,4,5}
test2 = {4,5,6,7}
test3 = test-test2 #差集: 從test中,減去和test2重複的部分
print (test3)

##反交集
test = {3,4,5}
test2 = {4,5,6,7}
test3=test^test2 #反交集:取兩個集中,不重疊的部分
print (test3)

##字串set
s = set("hello")
print(s) #沒有順序性, 不會重複
print("h" in s)

#字典的運算 key-value的配對
dic = {"apple":"蘋果","banana":"香蕉"}
print (dic["apple"])

dic["apple"]="青蘋果"
print (dic["apple"])

##判斷key是否存在
dic = {"apple":"蘋果","banana":"香蕉"}
print ("apple" in dic) #判斷key是否存在 True
print ("car" in dic) #判斷key是否存在 Fales

##刪除字典鍵值對
dic = {"apple":"蘋果","banana":"香蕉"}
del dic["apple"] #刪除字典中的key值對(key-value pair)
print (dic)

#進階用法 key:value for key in 列表
dic = {x:x*2 for x in [3,4,5]}
print (dic) #產生鍵值對
