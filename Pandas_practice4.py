#Use - case
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

csv_file = pd.read_csv('C:\\Users\\Dimpoo\\.spyder-py3\\Project\\annual-enterprise-survey-2018-financial-year-provisional-csv.csv', index_col =0)
#,converters={"Value":int} add this as a parameter to read_csv 

df = csv_file.head(5)#only top 5 values of dataset

df = df.set_index(["Industry_aggregation_NZSIOC"])

sd = df.reindex(columns = ['Industry_code_NZSIOC', 'Value'])
sd["Value"] = sd["Value"].astype("int")
sd["Industry_code_NZSIOC"] = sd["Industry_code_NZSIOC"].astype("int")
#reindex the column, i want only these two to be my columns
print(sd)

db = sd.diff(axis=1)  #This will give me the percentage change in the two columns 
db.plot(kind='bar')  #Using a bar plot
plt.show()  

