def Map(name):                        #create a 2D list
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
    b=a[::-1]
    return b

def changecalculation_step_map(MAP):  #create two lists, one is to record the total calculation of changes, and the other is to record the positions (value of x) that I am ready to go
    a=[]
    b=[]
    i=0
    while i<len(MAP):
        a.append([0]*len(MAP[i]))
        b.append([0]*len(MAP[i]))
        i=i+1
    return a,b

def dynamic(calculation_map,step_map,map_data):   #find the shortest path starting from each start point 
    import random
    for row in range(1,len(map_data)):
        for point in range(len(map_data[row])):
            one=0
            two=0
            three=0
            if point==0:
                one=calculation_map[row-1][point]+abs(map_data[row][point]-map_data[row-1][point])
                two=calculation_map[row-1][point+1]+abs(map_data[row][point]-map_data[row-1][point+1])
                if one<two:
                    calculation_map[row][point]=one
                    step_map[row][point]=point
                elif one>two:
                    calculation_map[row][point]=two
                    step_map[row][point]=point+1
                elif one==two:
                    calculation_map[row][point]=one
                    step_map[row][point]=point
            elif point==len(map_data[row])-1:
                two=calculation_map[row-1][point-1]+abs(map_data[row][point]-map_data[row-1][point-1])
                three=calculation_map[row-1][point]+abs(map_data[row][point]-map_data[row-1][point])
                if two<three:
                    calculation_map[row][point]=two
                    step_map[row][point]=point-1
                elif two>three:
                    calculation_map[row][point]=three
                    step_map[row][point]=point
                elif two==three:
                    calculation_map[row][point]=two
                    step_map[row][point]=point
            else:
                one=calculation_map[row-1][point-1]+abs(map_data[row][point]-map_data[row-1][point-1])
                two=calculation_map[row-1][point]+abs(map_data[row][point]-map_data[row-1][point])
                three=calculation_map[row-1][point+1]+abs(map_data[row][point]-map_data[row-1][point+1])
                if min(one,two,three)==two:
                    calculation_map[row][point]=two
                    step_map[row][point]=point
                elif min(one,two,three)==one:
                    calculation_map[row][point]=one
                    step_map[row][point]=point-1
                elif min(one,two,three)==three:
                    calculation_map[row][point]=three
                    step_map[row][point]=point+1
                elif one==three and one<two and three<two:
                    calculation_map[row][point]=one
                    choice=random.choice((True,False))
                    if choice==True:
                        step_map[row][point]=point-1
                    else:
                        step_map[row][point]=point+1
    return calculation_map,step_map


def find_path(Calculation,Step_map):
    total_path=[]
    for a in range(len(Calculation[len(Calculation)-1])):
        path=[]
        path.append(Calculation[len(Calculation)-1][a])
        path.append(a)
        row=len(Step_map)-1
        point=Step_map[row][a]
        p=0
        while row>0:
            row=row-1
            path.append(point)
            point=Step_map[row][point]
        total_path.append(path)
    distance_=[]
    for b in range(len(total_path)):
        distance_.append(total_path[b][0])
    _min_=min(distance_)
    position=distance_.index(_min_)
    best=total_path[position]
    return total_path,best

def write_files(names):              #write paths into files
    with open("Final_dynamic.rt","w")as f:
        for S in names[0]:
            for SS in S:                
                f.write(str(SS)+" ")
            f.write("\n")
    f.close()
    with open("Final_Best_dynamic.rt","w")as g:
        for a in names[1]:
            g.write(str(a)+" ")
    g.close()

MAP_name=input("Please enter the map name:")
map_=Map(MAP_name)
maps=changecalculation_step_map(map_)
Calculation_initial_map=maps[0]
Step_initial_map=maps[1]
final_maps=dynamic(Calculation_initial_map,Step_initial_map,map_)
Calculation_final_map=final_maps[0]
Step_final_map=final_maps[1]
Final_result=find_path(Calculation_final_map,Step_final_map)
write_files(Final_result)


    

    





