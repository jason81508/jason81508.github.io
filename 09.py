# 定義函式
def multiply(): #沒有參數的函式
	print(3*4)

def multiply2(n1,n2): #有參數的函式
	print (n1*n2)


#呼叫函式
multiply()

multiply2(3,4)
multiply2(10,8)

#回傳值return
def multiply3(n1, n2):
	print(n1*n2)
	return "end" #如果沒有return 或return沒有布林值 value顯示none
value = multiply3(5,4)
print(value) 

##回傳值進階操作
def multiply4(n1, n2):
	return n1*n2 #如果沒有return 或return沒有布林值 value顯示none
value = multiply4(5,4) + multiply4(4,5)
print(value)

#函式可用來做程式的包裝 同樣的邏輯可以重複利用 
def calculate(max):
	sum = 0
	for n in range(1,max+1):
		sum = sum + n
	print(sum)

calculate(10)
calculate(20)

# 以上同下 需要複雜式的貼上迴圈 用定義即可縮減程式碼
sum = 0
for x in range(1,11):
	sum = sum+x
print (sum)

