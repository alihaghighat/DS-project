from collections import defaultdict
from collections import OrderedDict
import re
#number of vertices
numNodes=0
#stor grafe
inputoftree=[]

def addto(u,v,w):
    xs=[u-1,v-1,w]
    inputoftree.append(xs)


def find(parent,i):
    if parent[i]==i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
    xroot=find(parent,x)
    yroot=find(parent,y)
    
    if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot
        
    else:
        parent[yroot] = xroot 
        rank[xroot] += 1

def kruskal(xs,g):
    res=[]
    i=0
    j=0
    parent = []
    rank = []
    xs=sorted(xs,key=lambda item: item[2])
    for node in range(g): 
            parent.append(node) 
            rank.append(0) 
    while j < g -1 : 
            
            u,v,w =  xs[i] 
            i = i + 1
            x = find(parent, u) 
            y = find(parent ,v) 
            
    
            if x != y: 
                j = j + 1     
                res.append([u+1,v+1,w]) 
                union(parent, rank, x, y)
    return res

file = open("bipe2p.stp");
read=file.readlines()
t=read.index("SECTION Graph\n")
t=t+1
gre=int(re.search(r'\d+', read[t]).group())
j=t+1

raneg=int(re.search(r'\d+', read[j]).group())
numNodes=gre
for p in range(0,raneg):
    temp=[int(x.group()) for x in re.finditer(r'\d+', read[p+j+1])]
    addto(temp[0], temp[1], temp[2])
    
Krusl=kruskal(inputoftree,numNodes)
Krusl1=Krusl
def findre(xs,l):
    reza=[]
    for array in xs:
        if array[0]==l:
            reza.append(array[1])
        elif array[1]==l:
            reza.append(array[0])
    return reza;


temp2=[]
for arrayk in Krusl1:
    po=[]
    po.append(arrayk[0])
    po.append(arrayk[1])
    temp2.append(po)   

for k in temp2:
    if len(k)> numNodes:
        break
    else:
        t=[]
        t=t+k
        y=findre(Krusl1,k[-1])
        for f in y:
            if not f in t:
                l=t+[f]
                temp2.append(l)
            
trminal=[]
u=read.index("Section Terminals\n")
u=u+1
rep=int(re.search(r'\d+', read[u]).group())

for p in range(0,rep):
    temp=[int(x.group()) for x in re.finditer(r'\d+', read[p+u+1])]
    trminal.append(temp[0])
res1=[]
for u in temp2:
    if u[0] in trminal and u[-1] in trminal:
        for k in u:
            res1.append(k)
    else:
        if len(u)>2:
            y=u[1:-1]
            temp2.append(y)
            
result=[]

for t  in Krusl1:
    if t[0] in res1 and t[1] in res1:
        result.append(t)
coust=0;
for j in result:
    coust=coust+j[2]
coust1=0;
for j in Krusl:
    coust1=coust1+j[2]

file = open("hc9u.out", "w")
cots1="Cost "+str(coust)+"\n"   
file.writelines(cots1)
cots="Edges "+str(len(result))+"\n"   
file.writelines(cots)
for j in result:
    t="E "+str(j[0])+" "+str(j[1])+"\n"
    file.writelines(t)
  
print(coust1)
file.close()



