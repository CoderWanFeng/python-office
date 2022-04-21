import pandas as pd
import numpy as np

info1 = name + time + result
info1 = np.array(info1).reshape(1,3)

df = pd.DataFrame(info1,columns=['姓名','时间','检测结果'])
df.to_excel('核酸结果.xlsx', index=False)