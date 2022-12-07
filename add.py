import pandas as pd
data = pd.read_csv("MDS.csv")
data = pd.DataFrame(data)
# print(data.loc[[0,10]]) #return the first and 10th row 
# print(data.head(5)) #print first five rows
# print(data.tail(5)) #printing last five rows
# print(data.info()) #printing data type for each column
# newData = data.dropna() #drop rows that was empty
# data.fillna("spacer", inplace=True) #replace empty rows
# data["FirstName"].fillna("spacer", inplace=True) #replace na or empty rows at specified column
# meanofsomething = data["Age"].mean() #getting mean and puttig into variable
# median, and  mode is also a functional function
# data["Age"].fillna(meanofsomething, inplace=True) #filling NA rows with average age of AGE column
# data["Age"] = pd.to_int(data["Age"]) #converting column data type
# data.dropna(subset=['Age','FullName'],inplace=True) #removing rows from column which has NA values
#data.loc[5,"Age"] = data["Age"].mean() #replacing the values of specified rows with mean values of a column
"""  #iterate through column rows and change values of NA 
for x in data.index:
    if data.loc[x,"Age"] == data.isna(x):
        data.loc[x,"Age"] = 25 #change values
        data.drop(x, inplace=True) #drop rows
""" 
# data.duplicated() #display rows that are duplicated by giving output True or False
# data.corr() # display column relationships between each others
# df = df.iloc[:,0:2] # this selects first two columns
# df = df[['column1', 'column2']]
# df.iloc[:5,] #First 5 rows
# df.iloc[1:5,] #Second to Fifth row
# df.iloc[5,0] #Sixth row and 1st column
# df.iloc[1:5,0] #Second to Fifth row, first column
# df.iloc[1:5,:5] #Second to Fifth row, first 5 columns
# df.iloc[2:7,1:3] #Third to Seventh row, 2nd and 3rd column
# end
# next is plotting
        
