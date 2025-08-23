import random
no=int(input("enter no of teams:"))
teams=[]
matches=[]
for i in range(no):
    a=input("enter the team name:")
    teams.append(a)
meet=int(input("enter the no of team meets:"))
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(meet):
            
            matches.append([teams[i],teams[j]])
random.shuffle(matches)

for i in range(len(matches)):
    print("matches{} .{} vs{}".format(i+1,matches[i][0],matches[j][1]))
