import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

XYZ_web1 = {'day': [1, 2, 3, 4, 5, 6], 'Visitors':[1000, 700, 800, 50, 500, 1024], 'Bounce_rate':[20, 40, 67, 45, 34, 78]}

df1 = pd.DataFrame(XYZ_web1)

print(df1)

#Slicing
print(df1.head(2))
print(df1.tail(2))

#Merging: Merge two dataframes
XYZ_web2 = {'day': [1, 2, 3, 4, 5, 6], 'Visitors':[1000, 700, 800, 50, 500, 1024], 'Bounce_rate':[20, 40, 67, 45, 34, 78]}

df2 = pd.DataFrame(XYZ_web2)

merge1 = pd.merge(df1, df2)
print(merge1)

#if you wanna keep or remove certain columns
merge2 = pd.merge(df1, df2, on=["Visitors","day"]) # Only Vistors column will be common
print(merge2)

#Joining: joining happens with the index values
#NaN: when there is no particular value attached to particular index, it wries it as NaN(Not a Number)

dict1 ={'Index':[2001, 2002 , 2003 , 2005], 'Visitors':[1000, 700, 800, 50]}
dict2 = {'Indexw': [2003, 2006, 2004, 2010], 'Visitorsw':[1000, 700, 800, 50]}

ff1 = pd.DataFrame(dict1)
ff2 = pd.DataFrame(dict2)

joined = ff1.join(ff2)
print(joined)

#changing the index and column headers
#df1.set_index(['day','Visitors'], inplace=True)
df1.set_index('day', inplace=True)
print(df1)

df1.plot()
plt.show()

