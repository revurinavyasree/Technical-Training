a=input("enter a string")
count=1
res=""
for i in range(len(a)):
    if(i+1<len(a) and a[i]==a[i+1]):
        count=count+1
    else:
        res=res+a[i]
        res=res+str(count)
        c=1
print(res)
