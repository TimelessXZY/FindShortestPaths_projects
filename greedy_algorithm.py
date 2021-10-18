def Map(name):                #put the map data into a 2D list
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

def greedy(MAP):             #use greedy algorithm to find the shortest path starting from each startpoint
    import random
    Final_Path=[]
    for a in range(len(MAP[0])):
        distance=[]
        path=[]
        line=0
        path.append(a)
        X=a
        while line<len(MAP)-1:
            Start_Point=X
            L=0
            M=0
            R=0
            if X==0:
                M=abs(MAP[line+1][X]-MAP[line][X])
                R=abs(MAP[line+1][X+1]-MAP[line][X])
                if M==R:
                    X=X
                    distance.append(M)
                    path.append(X)
                elif M<R:
                    X=X
                    distance.append(M)
                    path.append(X)
                elif M>R:
                    X=X+1
                    distance.append(R)
                    path.append(X)
            elif X==len(MAP[line])-1:
                M=abs(MAP[line+1][X]-MAP[line][X])
                L=abs(MAP[line+1][X-1]-MAP[line][X])
                if M==L:
                    X=X
                    distance.append(M)
                    path.append(X)
                elif M<L:
                    X=X
                    distance.append(M)
                    path.append(X)
                elif M>L:
                    X=X-1
                    distance.append(L)
                    path.append(X)
            else:
                M=abs(MAP[line+1][X]-MAP[line][X])
                R=abs(MAP[line+1][X+1]-MAP[line][X])
                L=abs(MAP[line+1][X-1]-MAP[line][X])
                if min(M,R,L)==M:
                    X=X
                    distance.append(M)
                    path.append(X)
                elif min(M,R,L)==R:
                    X=X+1
                    distance.append(R)
                    path.append(X)
                elif min(M,R,L)==L:
                    X=X-1
                    distance.append(L)
                    path.append(X)
                elif R==L and R<M and L<M:
                    choice=random.choice((True,False))
                    if choice==True:
                        X=X-1
                        distance.append(L)
                        path.append(X)
                    else:
                        X=X+1
                        distance.append(R)
                        path.append(X)
            line=line+1    
        total_distance=sum(distance)
        path.insert(0,total_distance)
        Final_Path.append(path)
    return Final_Path

def write_files(names):                #write paths into files
    with open("Final_greedy.rt","w")as f:
        for S in Final:
            for SS in S:
                f.write(str(SS)+" ")
            f.write("\n")
    f.close()
    with open("Final_Best_greedy.rt","w")as g:
        Distance=[]
        for J in range(len(Final)): 
            Distance.append(Final[J][0])
        Best=min(Distance)
        X=Distance.index(Best)
        for K in Final[X]:   
            g.write(str(K)+" ")
    g.close()
    
MAP_name=input("Please enter the map name:")
TwoD_map=Map(MAP_name)
Final=greedy(TwoD_map)
write_files(Final)

             
                    
                    
            
                    
                    
                    
                
                    
                    
                    
                
                
            
        
            
        
    
        
        
