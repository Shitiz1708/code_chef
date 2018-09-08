test=int(input())
list=[]
for i in range(test):
    n,m,x,y=[int(i) for i in input().split(" ")]
    if n>=x and m>=y:
        if(n%x==m%y):
            if(n%x>2):
                list.append("Pofik")
            else:
                list.append("Chefirnemo")
        else:
            list.append("Pofik")
    else:
        list.append("Pofik")

for j in list:
    print(j)