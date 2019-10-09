#判斷式
if True:
	print ("True 執行")
else:
	print ("False 執行")

#取得字串形式的使用者輸入
x = input ("請輸入數字:") #取得字串形式的使用者輸入
x = int(x) #將字串型態轉換成數字型態
if x > 100:
	print ("大於100")
elif x == 100:
	print("等於100") #等於一百==
else:
	print ("小於100")
#四則運算
n1 = int(input("請輸入數字1:"))
n2 = int(input("請輸入數字2:"))
print (n1+n2)

##進階 做哪種+-*/
n1 = int(input("請輸入數字1:"))
op = input("請輸入運算+,-,*,/: ")
n2 = int(input("請輸入數字2:"))
if op == "+":
	print (n1 + n2)
elif op == "-":
	print (n1 - n2)
elif op == "*":
	print (n1 * n2)
elif op == "/":
	print (n1 / n2)
else:
	print ("不支援的語法")

