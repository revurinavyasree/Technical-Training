#simpleintrest=p*t*r/100

def simple_intrest(p,t,r):
    return(p*t*r)/100
p,t,r=4,5,7
print(simple_intrest(p,t,r))

#using lambda function
si=lambda p,t,r:(p*t*r)/100
p,t,r=3,4,5
res=si(p,t,r)
print(res)


#using list
p,t,r=1,2,3
si=[p*t*r/100][0]
print(si)
