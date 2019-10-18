#主程式 + 封包 __init__.py 封包完就不用特別搜尋資料夾 sys.path.appent
import geometry.point
result = geometry.point.distance(3,4)
print ("距離",result)

import geometry.line
result = geometry.line.slope(1,1,3,3)
print("斜率",result)

##別名 封包 as
import geometry.line as line
result = line.slope(1,1,3,3)
print("斜率",result)