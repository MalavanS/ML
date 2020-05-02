import pandas as pd 
df = pd.read_csv("boston.csv")

#try to understand data
print(df.shape)
print(df.columns)
print(df.describe())
print(df.head(4))
print(df.groupby('LotShape').size())
print(df.info())

df_null = df.isnull().sum() #getting null value count on each columns and columns become index of this series
# values & index of above series can be seen using below
print(df_null.index)
print(df_null.tolist())
type(df_null)

cols_rem = df_null[df_null > 0.05*len(df_null)]
df = df.drop(cols_rem.index, axis=1)
print(df.shape)

#replace null values in object data columns with most used value
ls = df.select_dtypes(include=['object']).isnull().sum()
for index in ls.index:
    b1 = df[index].value_counts().index.tolist()
    df[index] = df[index].fillna(b1[0])

#replace null values in integer and float data type columns with most used value
numeric_nulls = df.select_dtypes(include=['integer','float']).isnull().sum()
print(numeric_nulls)
null_cols = numeric_nulls[numeric_nulls!=0].index
print(null_cols)
#df = df.fillna(df[null_cols].mode().to_dict(orient='records')[0]) - since there is no null values