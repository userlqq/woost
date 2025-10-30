import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)

insurance_df=pd.read_csv('insurance-chinese.csv',encoding='gbk')

print("输出数据框的前五行记录,如下")
print(insurance_df.head())
print()

print("输出数据框的各列详细信息如下:")
insurance_df.info()







