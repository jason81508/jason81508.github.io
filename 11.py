#import 模組的名稱(檔案名稱)

#import 模組名稱 as 模組別名(縮短名稱)

# 模組名稱或別名.函式名稱(參數資料)
# 模組名稱或別名.變數名稱



# 載入內建sys模組並取得資訊
import sys #python內建模組
print (sys.platform)
print (sys.maxsize)

## 操作系統的path(新增路徑)
sys.path.append("modules")
# 建立geometry模組, 載入使用
import geometry
result = geometry.distance(1,1,5,5)
print (result)
result = geometry.slope(1,2,5,6)
print (result)
# 調整搜尋模組的路徑
print (sys.path) #印出模組的搜尋路徑


