str=input()
lst=[]
for i in str:
   lst.append(i)
for j in lst:
    if lst.count(j)==1:
        print(j,end="")
