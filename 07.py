#while 迴圈
n = 1 
while n<=10:
	print(n)
	n += 1
## 紀錄累加的結果sum
n = 1 
sum = 0
while n<=10:
	sum = sum+n
	n += 1
	print(sum) #有凸排跟無凸排結果不同
print(sum) #有凸排跟無凸排結果不同


#for 迴圈
for x in [3,5,7]:
	print(x)
##印出字元
for x in "hello":
	print(x)
##印出範圍
for x in range(5):
	print(x) #不含尾巴
##印出範圍2
for x in range(5,10):
	print(x)
##紀錄累加的結果
sum = 0
for x in range(11):
	sum = sum+x
print(sum)