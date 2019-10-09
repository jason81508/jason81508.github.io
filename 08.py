#break 中斷迴圈
# n=0
# while n<5 :
# 	if n==3:
# 		break
# 	print(n)
# 	n+1
# print("最後的n:",n) #執行這段會壞掉

#continue 得true往下走 得false跳過
for x in [0,1,2,3]:
	if x % 2 == 0: #取餘數,x是偶數
		continue #有False再往下走
	print(x)
	x += 1
print("最後的n:",x)

#else
sum = 0
for y in range(11):
	sum+=y
else:
	print(sum) #印出1+2+...+10的結果

# 綜合範例 數入9 得到3 數入11 得到{沒有}整數的平方根
n = input("輸入一個正整數:")
n = int(n) #轉換成數字
for i in range(n):
	if i * i == n:
		print ("整數平方根", i) # 1*1 ,2*2 ,3*3=9 break 找到平方根停止
		break # 用break強制結束迴圈時 不會執行else
else:
	print("沒有整數平方根")