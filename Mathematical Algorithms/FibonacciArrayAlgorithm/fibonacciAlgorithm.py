#fibonacci algorithm
listFibbonaci=[]

limitNum=int(input("input a limit"))
for i in range(1,(limitNum+1)):
    if i==1 or i==2:
        listFibbonaci.append(1)                 
    elif limitNum>2:
        listFibbonaci.append(listFibbonaci[len(listFibbonaci)-1]+listFibbonaci[len(listFibbonaci)-2])
    else:
        print("Wrong request")
print(listFibbonaci)