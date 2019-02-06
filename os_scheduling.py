def sumi (li, key = lambda x: x):
    res = 0
    for i in li:
        res += key(i)
    return res

n= int(input("Enter no of jobs?"))
li = []
print("Enter n lines, with each line containing Arrival time, CPU burst time and Priority...\n")
for i in range(n):
    li.append(list(map(int,input().split()))+[i])



######################## FCFS ###################
# Sort as per arrival time for FCFS
li.sort()
fcfs = [] # List contains completion time, arrival time, burst time, turn around time and waiting time
print("FCFS Ordering!!!")
time = 0
for i,index in enumerate(li):
    time=max(time,li[i][0])
    print("Index: ",li[i][2],", Burst Time: ",li[i][1],", Execution start time: ",time)
    at = li[i][0]
    bt = li[i][1]
    ct = time + bt
    tat = ct - at
    wt = tat - bt
    fcfs.append([ct,at,bt,tat,wt])
    time+=li[i][1]
print("\nFCFS Results:\n")
print("Avg. Waiting Time = ",sumi(fcfs,key = lambda x: x[4])/n)
print("Avg. Turn around Time = ",sumi(fcfs,key = lambda x: x[3])/n)
print("CPU Utilization = ",sumi(fcfs,key = lambda x: x[2])*100/time, "%")
print("No. of Context switches = ",n-1)    
print("Throughput = ",n/time)



#################### S JF #######################
print("\n\nSJF Ordering!!!")
time = 0 #Keeps track of current time
li1 = li[:]
li2=[]
#li1 contains all the jobs which are not yeat ready
#li2 contains all jobs which are ready for execution
sjf=[] #List simailar to fcfs above
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
    at = job[0]
    bt = job[1]
    ct = time+bt
    tat = ct - at
    wt = tat - bt
    sjf.append([ct,at,bt,tat,wt])
    print("Index: ",job[2],", Burst Time: ",job[1],", Execution start time: ",time)
    time+=job[1]
print("\nSJF Results:\n")
print("Avg. Waiting Time = ",sumi(sjf,key = lambda x: x[4])/n)
print("Avg. Turn around Time = ",sumi(sjf,key = lambda x: x[3])/n)
print("CPU Utilization = ",sumi(sjf,key = lambda x: x[2])*100/time, "%")
print("No. of Context switches = ",n-1)   
print("Throughput = ",n/time)
    
 
 #################### SRTF #####################   
li1=li[:]
time = 0
li2=[]
#li1, li2 and time have their usual meaning as above.
srtf = [[] for _ in range(n)] #Similar except for the fact that process number is the index in srtf list
# List contains completion time, arrival time, burst time, turn around time and waiting time
context_switches = 0
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
    at = li2[job][0]
    bt = li2[job][1]
    ct = time+bt
    tat = ct - at
    wt = tat - bt
    srtf[li2[job][-1]] = [ct,at,bt,tat,wt]
    time+=1
    if li2[job][1]==0:
        li2.pop(job)
print("\nSRTF Results:\n")
print(srtf)
print("Avg. Waiting Time = ",sumi(srtf,key = lambda x: x[4])/n)
print("Avg. Turn around Time = ",sumi(srtf,key = lambda x: x[3])/n)
print("CPU Utilization = ",sumi(srtf,key = lambda x: x[2])*100/time, "%")
print("No. of Context switches = NOT WORKING!!!!",n-1)   
print("Throughput = ",n/time)
    
## TODO: Preserve bus time and count number of context switches.
