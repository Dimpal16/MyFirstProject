import pandas as pd

#Renaming a column header
df1 = pd.DataFrame({'Index':[2001, 2002 , 2003 , 2005], 'STUDENT':['DIMPAL', 'AAKASH', 'MAYURI', 'KASTURI'], 'AGE':['18','20','19','19'],'SEX':['F','M','F','F']}, index=[1,2,3,4])
df2 = pd.DataFrame({'Index':[2006, 2007 , 2008 , 2009], 'STUDENT':['DIMPAL', 'AAKASH', 'MAYURI', 'KASTURI'], 'AGE':['18','20','19','19'],'SEX':['F','M','F','F']}, index=[5,6,7,8])
df = df1.rename(columns = {'Index':'Sr.'})
print(df)

#CONCATNETATION
#Adding email address field at the end of the dataframe
concat = pd.concat([df1, df2], sort=False)
print(concat)


