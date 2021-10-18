def Map(name):                              #create a 2D list
    with open(name,"r")as f:
        lines=f.readlines()
        a=[]
        for line in lines:
            a1=[]
            i=line.strip("\n")
            j=i.split(" ")
            for k in j:
                if k!='':
                    a1.append(int(k))
                else:
                    continue
            a.append(a1)
        del(a[0])
    return a


def breaklist(map_):                        #put all the data in one list
    F=[]
    for i in range(len(map_)):
        for j in map_[i]:
            F.append(j)
    return F

def createdistance(map_,map_broken):        #create adjacency matrix
    C=[]
    i=0
    while i<(len(map_)*len(map_)):
        C.append([999999]*(len(map_)*len(map_)))
        i=i+1
    for a in range(len(C)):
        for b in range(len(C[a])):
            if a%len(map_)==0 and len(map_)<=b-a<=len(map_)+1:
                C[a][b]=abs(map_broken[b]-map_broken[a])
            elif (a%len(map_))+1==len(map_) and len(map_)-1<=b-a<=len(map_):
                C[a][b]=abs(map_broken[b]-map_broken[a])
            elif 0<a%len(map_)<len(map_)-1 and len(map_)-1<=b-a<=len(map_)+1:
                C[a][b]=abs(map_broken[b]-map_broken[a])
            else:
                continue
    return C


def createdist(map_,distance_matrix):        #create a list containing the distances from each starpoint to all the points in the map
    a1=[]
    for i1 in range(len(map_)):
        a1.append(distance_matrix[i1])
    return a1

def visited(distance_of_startpoint):         #create a list to record each point that has been passed
    s=[]
    i=0
    while i<len(distance_of_startpoint):
        l=[]
        j=0
        while j<len(distance_of_startpoint[i]):
            if j==0:
                l.append(1)
            else:
                l.append(0)
            j=j+1
        i=i+1
        s.append(l)
    return s

def dijkstra(map_,visitedrecord,distancemap): #calculate the total shortest distance from each start point to all the point in the map
    C=createdist(map_,distancemap)
    E=[]
    for i in range(len(C)):
        l=0
        F=[999999]*len(C[i])
        while l<len(C[i]):
            v=0
            min_dist=999999
            j=0
            while j<len(C[i]):
                if visitedrecord[i][j]==0 and C[i][j]<min_dist:
                    min_dist=C[i][j]
                    if F[j]==999999:
                        F[j]=i
                    v=j
                j=j+1
            visitedrecord[i][v]=1
            k=0
            while k<len(C[i]):
                if visitedrecord[i][k]==0:
                    if C[i][v]+distancemap[v][k]<C[i][k]:
                        
                        C[i][k]=C[i][v]+distancemap[v][k]
                        F[k]=v
                k=k+1
            l=l+1
        E.append(F)
    return C,E

def print_path(Dist,Path):                    #print final path
    min_=0
    G=[]
    for o in range(len(Dist)):
        h=len(Dist[o])-len(Dist)
        H=[]
        min_=Dist[o][h]
        while h<len(Dist[o]):
            if min_>Dist[o][h]:
                min_=Dist[o][h]
            h=h+1
        f=Dist[o].index(min_,len(Dist[o])-len(Dist))
        g=len(Path)
        H.append(f%len(Path))
        while g>1:
            p=Path[o][f]
            f=p
            H.append(f%len(Path))
            g=g-1
        H.append(min_)
        G.append(H[::-1])
    return G

def write_files(names):              #write paths into files
    with open("Final_result_dijkstra.rt","w")as f:
        for S in names:
            for SS in S:
                f.write(str(SS)+" ")
            f.write("\n")
    f.close()
    with open("Final_Best_result_dijkstra.rt","w")as g:
        Distance=[]
        for J in range(len(names)):
            Distance.append(names[J][0])
        Best=min(Distance)
        X=Distance.index(Best)
        for K in names[X]:
            g.write(str(K)+" ")
    g.close()

MAP_name=input("Please enter the map name:")
MAP=Map(MAP_name)
Broken_map=breaklist(MAP)
distance_map=createdistance(MAP,Broken_map)
distance_startpoint=createdist(MAP,distance_map)
visited_record=visited(distance_startpoint)
Final_dist=dijkstra(MAP,visited_record,distance_map)
shortest_distance=Final_dist[0]
path=Final_dist[1]
Final_path=print_path(shortest_distance,path)
write_files(Final_path)






