#script 6
def evenodd(list):
    evenlist=[]
    oddlist=[]
    for i in list:
        if (i % 2 == 0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("even list:",evenlist)
    print("odd list:",oddlist)
def creatlist():
    list=[]
    n=int(input("enter number of limit element:"))
    for i in range(0,n):
        ele=int(input())
        list.append(ele)
        #print(list)
creatlist()
evenodd(list)
    
