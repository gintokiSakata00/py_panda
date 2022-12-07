import pandas as pd
from tabulate import tabulate

data = pd.read_csv("MDS.csv")
data = pd.DataFrame(data)
data_mine = data[["FirstName","LastName","FullName","Gender","Age"]]
head = list(data_mine.columns.values)
pointer = ["chosen", "pick", "get"]
identifier = ["male","female","students"]
syntax = ["starts","with","ends","contains","of"]
join = head+identifier

initialize=new_data=heads =0

filter_val =pointer_val = identifier_val = syntax_val = head_val = ""

def passArray(a):
    array_A = []
    for i in a:
        array_A.append(i.lower())
    return array_A

join = passArray(join)
head_arr = passArray(head)



def checkValues(a):
    global initialize
    if "male" in a.lower() or "female" in a.lower() and "gender" in a.lower():
        initialize+=1
    else:
        initialize=0
    x = a.lower().split()
    last = a.split()
    last = last[len(last)-1]
    z = []
    global filter_val,pointer_val, identifier_val, syntax_val, head_val
    syntax_val =""
    syntax_count=count_filter=0
    for i in x:
        if i in pointer:
            pointer_val=i
            z.append(1)
        elif i in join:
            if initialize == 1:
                if "male" == i:
                    filter_val="Male"
                elif "female" == i:
                    filter_val="Female"
                else:
                    identifier_val = "Gender"
            else:
                if i in identifier:
                    identifier_val=i
                else:
                    for x in head:
                        if i == x.lower():
                            identifier_val=x
                z.append(2)
        elif i in syntax:
            syntax_count+=1
            syntax_val+=i
            if syntax_count==1:
                syntax_val+=" "
            elif syntax_count==2:
                z.append(3)
        else:
            if i == last.lower():
                filter_val = last
            else:
                filter_val = i
            count_filter+=1
            if count_filter==2:
                z.append(0)
                z.append(0)
            
            
   
              
    if(len(set(z)) == len(z)):
        z.clear()
        return True
    else:
        return False
    
    

def display(check):
    # if check:
    #     print("pointer:",pointer_val)
    #     print("identi :",identifier_val)
    #     print("syntax :",syntax_val)
    #     print("filter :",filter_val)
    # else:
    #     print(check)
        
    try:
        if "starts" in syntax_val:
            data = data_mine[data_mine[identifier_val].str.startswith(filter_val)]
        elif "ends" in syntax_val:
            data = data_mine[data_mine[identifier_val].str.endswith(filter_val)]
        elif initialize ==1:
            data = data_mine[data_mine[identifier_val]==filter_val]
        else:
            data = data_mine[data_mine[identifier_val].str.contains(filter_val)]
        global new_data,heads
        new_data = data[[identifier_val]]
        heads = list(new_data.columns.values)
        return new_data.index
    except:
        print("wrong")

        
print("Conditional Probability")
print(data_mine)
print()
formula = "P(A)*P(B|A)"
user_A = input(str("A -> "))

formula_split = formula.split("*")
# user_A = "pick lastname starts with Ab"
# user_B = "get gender of female"
# get students firstname starts with A 
# get students gender female


User_input_A = checkValues(user_A)
return_A = display(User_input_A)
len_return_A = len(return_A)
old_data_mine = data_mine
print(tabulate(new_data, headers=heads, tablefmt='psql'))
heads=""
user_B = input(str("B -> "))
data_mine = data_mine.drop(new_data.index)
User_input_B= checkValues(user_B)
return_B = display(User_input_B)
len_return_B= len(return_B)
new_data_mine = data_mine
print(tabulate(new_data, headers=heads, tablefmt='psql'))
print("Formula: "+formula)
lenA = len(old_data_mine)
lenB = len(new_data_mine)
result_A = str(len_return_A)+"/"+str(lenA)
result_B = str(len_return_B)+"/"+str(lenB)
print(formula_split[0]+ ":\t S/N = " ,end="")
print(result_A)
print(formula_split[1]+ ":\t S/N = " ,end="")
print(result_B)
print()
print("\t:"+result_A+" * "+result_B)
ansA = len_return_A*len_return_B
ansB = lenA*lenB
finalAns = str(ansA)+"/"+str(ansB)
print("\t:"+finalAns)
print("Final Answer: "+finalAns)