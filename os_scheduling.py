
n= int(input("Enter no of jobs?"))
li = []
print("Enter n lines, with each line containing Arrival time, and CPU burst time...\n")
for i in range(n):
    li.append(list(map(int,input().split()))+[i])
li.sort()
print("FCFS Ordering!!!")
time = 0
for i,index in enumerate(li):
    time=max(time,li[i][0])
    print("Index: ",li[i][2],", Burst Time: ",li[i][1],", Execution start time: ",time)
    time+=li[i][1]
print("\n\nSJF Ordering!!!")
time = 0
li1 = li[:]
li2=[]
while len(li1)!=0 or len(li2)!=0:
    removed = []
    for i in li1:
        if i[0]<=time:
            li2.append(i)
            removed.append(i)
    for i in removed:
        li1.remove(i)
    if len(li2)>0:
        job = min(li2,key=lambda x: x[1])
        li2.remove(job)
    else:
        time+=1
        continue
    print("Index: ",job[2],", Burst Time: ",job[1],", Execution start time: ",time)
    time+=job[1]
li1=li[:]
time = 0
li2=[]
print("\n\nSRTF Scheduling!!!")
while len(li1)!=0 or len(li2)!=0:
    removed = []
    for i in li1:
        if i[0]<=time:
            li2.append(i)
            removed.append(i)
    for i in removed:
        li1.remove(i)
    if len(li2)>0:
        job = li2.index(min(li2,key=lambda x: x[1]))
        li2[job][1]-=1
    else:
        time+=1
        continue
    print("Index: ",li2[job][2],", Burst Time: ",1,", Time: ",time)
    time+=1
    if li2[job][1]==0:
        li2.pop(job)


