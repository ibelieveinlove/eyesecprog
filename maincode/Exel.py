import pandas as pd

columns_names = []

with open('columns_names.txt','r') as file:
    for i in file:
        columns_names.append[i.strip()]

dataframe = pd.read_csv('threat.txt',index_col=columns_names)

