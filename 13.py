# 檔案物件 = open (檔案路徑,mode = 開啟模式)
# 開啟模式
	##讀取模式 - r
	##寫入模式 - w
	##讀寫模式 - r+
# 檔案物件.read()
# 讀取json格式
	##import json
	##讀取到的資料=json.load(檔案物件)
#寫入文字
	##檔案物件.write(字串)
#寫入換行符號
	##檔案物件.write("這是範例文字"\n)
#寫入json格式
	##import json
	## json.dump(要寫入的資料,檔案物件)
#關閉檔案 --釋放資源
	##檔案物件.close
#最佳實務語法
	##with open(檔案路徑,mode = 開啟模式) as 檔案物件:
	## 讀取或寫入檔案的程式	以上區塊會自動安全的關閉檔案

#儲存檔案
file = open("data.txt",mode = "w") #開啟檔案
file.write("5\n3") #寫入成功 產生data.txt
file.close #關閉檔案

##處理中文的問題 encoding = "utf-8"
file = open("data2.txt",mode = "w", encoding = "utf-8")
file.write("30cm\n好棒棒") #寫入成功 產生data2.txt
file.close #關閉檔案

##實務型語法with open... as file: 不需要寫close 自動關閉
with open("data3.txt",mode = "w", encoding = "utf-8") as file:
	file.write("60cm\n好大大") #寫入成功 產生data3.txt 自動close

#讀取檔案
with open("data.txt",mode = "r", encoding= "utf-8") as file: #讀取檔案
	data = file.read() #檔案讀取出來
print(data)

##檔案要一行一行讀出來做總和
sum = 0
with open("data.txt",mode = "r") as file:
	for line in file: #一行一行讀出來
		sum+=int(line) #轉換成整數加到總和
print(sum)

#使用json格式讀取、覆寫檔案
import json
with open("config.json", mode = "r") as file:
	data = json.load(file)
# print("name",data["name"])
# print("version", data["version"])
##修改變數資料

data["name"] = "new name" #修改變數中的資料

with open("config.json", mode = "w") as file:
	data = json.dump(data,file)