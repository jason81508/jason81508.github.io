# 參數的預設資料
def power(base,exp=0): #exp預設是0
	print (base**exp) #base的幾次方(exp)
power(3,2) #3的2次方
power(4) #4的0次方

def divide(n1,n2):
	print(n1/n2)
divide(2,4)
divide(n2=2, n1=4)#預設值進去

# 無限/不定 參數資料
def avg(*numbers): #算出平均數
	sum = 0
	for x in numbers:
		sum = sum + x
	print(sum / len(numbers)) #總和再除以列表的長度
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)

