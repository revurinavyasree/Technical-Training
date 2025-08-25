student=[
    {"name":"raju","dept":"cse","marks":[30,40,25]},
    {"name":"rani","dept":"cse","marks":[45,40,35]},
    {"name":"raju ka rani","dept":"cse","marks":[33,42,45]},
    {"name":"navya","dept":"cse","marks":[50,50,45]},
    {"name":"poojith","dept":"cse","marks":[50,40,45]}
]
for i in student:
    total=sum(i["marks"])
    d=total//3
    i["per"]=d
res=sorted(student,key=lambda x:x["per"],reverse=True)
des=["FIRST","SECOND","THIRD","FOURTH","FIFTH"]
for i in range(5):
    print("rank {}:{}-{}has scored percantage stands{}".format(i+1,res[i]["name"],res[i]["per"],des[i]))
