import pandas as pd
#DATA MUNGING: convert a particular form of data into another
csv_file = pd.read_csv('C:\\Users\\Dimpoo\\.spyder-py3\\Project\\annual-enterprise-survey-2018-financial-year-provisional-csv.csv', index_col =0)
#index_col =0 make sure that i have no index present in that particular dataframe

#convert csv file to HTML file
csv_file.to_html('html_file.html')

