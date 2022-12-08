import sys
import pandas as pd
from tabulate import tabulate
import os
        
data = pd.read_csv("MDS.csv")
data = pd.DataFrame(data)
data_mine = data[["FirstName","LastName","FullName","Gender","Age"]]
head = list(data_mine.columns.values)
pointer = ["chosen", "pick", "get","chance","pull","call"]
identifier = ["male","female"]
syntax = ["starts","with","ends","contains","of","greater","less","not","equal","to","or","than"]
join = head+identifier
filters = ['numbers', 'alphabet', 'letters', 'strings', 'female', 'male']
initialize=new_data=heads=counter =0

filter_val =pointer_val = identifier_val = syntax_val = head_val = ""

def passArray(a):
    array_A = []
    for i in a:
        array_A.append(i.lower())
    return array_A

join = passArray(join)
head_arr = passArray(head)



def checkValues(a):
    if "quit" in a.lower() or "exit" in a.lower():
        sys.exit() 
    global initialize
    if "male" in a.lower() or "female" in a.lower() and "gender" in a.lower():
        initialize+=1
    else:
        initialize=0
    x = a.lower().split()
    last = a.split()
    last = last[len(last)-1]
    global filter_val,pointer_val, identifier_val, syntax_val, head_val
    syntax_val =""
    syntax_count=count_filter=0
    for i in x:
        if i in pointer:
            pointer_val=i
            
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
        elif i in syntax:
            syntax_count+=1
            if syntax_count>0:
                syntax_val+=" "
                syntax_val+=i
            else:
                pass
        else:
            if i == last.lower() or last.isnumeric():
                filter_val = last
            else:
                filter_val = i
            count_filter+=1
            

def display():
    try:
        if initialize==1:
            data = data_mine[data_mine[identifier_val]==filter_val]
        else:
            if "starts" in syntax_val:
                data = data_mine[data_mine[identifier_val].str.startswith(filter_val)]
            elif "ends" in syntax_val:
                data = data_mine[data_mine[identifier_val].str.endswith(filter_val)]
            elif "contains" in syntax_val:
                data = data_mine[data_mine[identifier_val].str.contains(filter_val)]
            elif syntax_val.strip() == "greater than" or syntax_val.strip() == "not less than or not equal to":
                data = data_mine[data_mine[identifier_val]>int(filter_val)]
            elif syntax_val.strip() == "not greater than" or syntax_val.strip()=="not greater than or equal to" or syntax_val.strip() == "less than or equal to":
                data = data_mine[data_mine[identifier_val]<=int(filter_val)]
            elif syntax_val.strip() == "greater than or equal to" or syntax_val.strip() =="not less than or equal to":
                data = data_mine[data_mine[identifier_val] >=int(filter_val)]  
            elif syntax_val.strip()== "less than" or syntax_val.strip()== "not greater than or not equal to":
                data = data_mine[data_mine[identifier_val]<int(filter_val)]
            elif syntax_val.strip()== "not less than" or syntax_val.strip()== "not less than or equal to" :
                data = data_mine[data_mine[identifier_val]>=int(filter_val)] 
            elif syntax_val.strip()=="equal to":
                data = data_mine[data_mine[identifier_val]==int(filter_val)]
            elif syntax_val.strip()=="not equal to":
                data= data_mine[data_mine[identifier_val]!=int(filter_val)]    
            global new_data,heads
        new_data = data[[identifier_val]]
        heads = list(new_data.columns.values)
        return len(new_data.index)
    except:
        print("Wrong Query")
        
def printResults():
    print(tabulate(new_data,headers= heads, tablefmt='psql'))
    
def processAnswer(x1,y1,x2,y2):
    print()
    print("Conditional Probability Solutions")
    formula = "P(A)*P(B|A)"
    formula_split = formula.split("*")
    print("Formula: "+formula)
    y1 = len(y1)
    y2 = len(y2)
    result_A = str(x1)+"/"+str(y1)
    result_B = str(x2)+"/"+str(y2)
    print(formula_split[0]+ ":\t S/N = " ,end="")
    print(result_A)
    print(formula_split[1]+ ":\t S/N = " ,end="")
    print(result_B)
    print()
    print("\t:"+result_A+" * "+result_B)
    ansA = x1*x2
    ansB = y1*y2
    strAns = f"{x1}*{x2} / {y1}*{y2}"
    initialAns = str(ansA)+"/"+str(ansB)
    print("\t:"+strAns)
    print("\t:"+initialAns)
    finalAns = ansA/ansB
    if finalAns!=0.0:
        print(f"Answer: {finalAns} or {initialAns}")
    else:
        print("ZeroDivisionError: Numerator cannot be Zero")
    
def data_dataframe():
    print("\nSELECTED DATA SETS \n")
    print(data_mine)        

def askuser(return_A):
    user_choice = input("Print results? Y/N : ")
    if user_choice.lower() =="y" and return_A>0:
        printResults()
    elif return_A==0:
        print("Empty query results")

def tutorial():
    print("HOW TO USE:")
    howtouse = """\tThis program automatically handles English Language to generates query based on the user query. This follows 4 categories of structing the query results such as the following; 
\nPointer:\t'Chose' 'Pick' 'Get' \n\t\t-This point to what the user want to call with the query
\nIdentifier:\t'Names' 'Age' 'Gender' \n\t\t-This is the column names of the chosen datasets
\nSyntax:\t\t'starts' 'end' 'contains' 'equal' 'greater' 'less' 'than' 'not' \n\t\t-This point to what the user want to call with the query
\nFilter:\t\t'numbers' 'alphabet lettes' 'strings' 'female' 'male' \n\t\t-These filters were the data or rows found on the data sets or csv file chosen.
\n\tConditional Probility is a measure of the probability of an event occurring, given that another event has already occurred. For example given a scenarios what are the chances or probability that event B will occur given the fact the event A happened first.
\n\tExample commands:
\tget firstname starts with A
\tget gender of female
\tchose fullnames which contains of Jam
\tpull age greater than 20
\tcall age that is greater than or equal to 21
\n\tYou can relate english language to your query."""
    print(howtouse)
    print(f"Pointer   : {pointer}")
    print(f"Identifier: {identifier}")
    print(f"Syntax    : {syntax[0:6]}")
    print(f"          : {syntax[6:]}")
    print(f"Filter    : {filters}")

def tryagain():
    global counter
    if counter == 0:
        stat = "start"
        cont = "continue"
        counter+=1
    else:
        stat = "exit"
        cont = "close"
    user_choice= input(str(f"Type '{stat}' to {cont} \n'again' to restart \nDecision: "))
    if "again" in user_choice:
        os.system("python index.py")
    elif "exit" in user_choice:
        sys.exit()
        
state = input(str("Do you want a tutorial? Y/N : "))
if state.lower() == "y":
    tutorial()

print() 
tryagain()
        

while True:
    data_dataframe()
    print()
    print("Conditional Probability Program")
    user_A = input(str("A -> "))
    User_input_A = checkValues(user_A)
    return_A = display()
    len_return_A =return_A
    old_data_mine = data_mine
    askuser(return_A)
    data_mine = data_mine.drop(new_data.index)    
    head = ""
    user_B = input(str("B -> "))
    User_input_B= checkValues(user_B)
    return_B = display()
    len_return_B = return_B
    new_data_mine = data_mine
    askuser(return_B)
    processAnswer(len_return_A,old_data_mine,len_return_B,new_data_mine)
    print()
    tryagain()