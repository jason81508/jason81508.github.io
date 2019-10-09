# 有序可變動列表 list
grades = [12,15,18,20,22]
print (grades[0]) #一樣用索引

##也可以更新資料
grades[0] = 55 #把55放到列表中的第一個位置
print (grades)

##取的元素 不包含尾巴
grades = [12,15,18,20,22]
print (grades[1:4])

##把連續刪除列表中從編號1到編號4
grades = [12,15,18,20,22]
grades[1:4] = []
print (grades)

##列表串接
grades = [12,15,18,20,22]
grades = grades + [25,27]
print (grades)

#取得列表的長度 len(列表的資料)
grades = [12,15,18,20,22]
length = len(grades)
print(length)

#巢狀的列表
data = [[3,4,5],[6,7,8]]
print (data[0][0]) #第一層 第0個索引

#進階列表調整
data = [[3,4,5],[6,7,8]]
data [0][0:2] = [5,5,5]
print (data[0])

# 有序不可變動列表 tuple

data = (3,4,5)
print (data[2])

##錯誤: data[0] = 5 ,tuple資料不可更動