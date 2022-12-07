import pandas as pd
from tabulate import tabulate
data = pd.read_csv("MDS.csv")
data = pd.DataFrame(data)
data_mine = data[["FirstName","LastName","FullName","Gender","Age"]]

print(data_mine.loc[1:2,["FullName"]])