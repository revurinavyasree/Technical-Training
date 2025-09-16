def prime(i):
    for j in range(2,i):
        if(i%j==0):
            return False
    return True

def sod(i):
    d=[int(i) for i in str(i)]
    return sum(d)

def alldig(i):
    while(i!=0):
        d=i%10
        if(not prime(d)):
            return False
        i=i//10
    return True

for i in range(200,1000):
    if(prime(i) and prime(sod(i)) and alldig(i)):
        print(i,end=" ")

