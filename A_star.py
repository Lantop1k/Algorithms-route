# create the heruistic function
def heriusticfcn(index):
    costvalue = [16,12,10,8,5,
        12,7,5,3,2,
        5,13,3,11,3,
        12,4,5,3,0]

    return costvalue[index]

# create a function for the A star algorithm
def A_star_alg():
    
        
    visited_list =   set(['A'])  # add the first point to visited nodes
        
    dest_list = set([])              

    g = {}

    g['A'] = 0

    parents = {}
    parents['A'] = 'A'

    while len(visited_list) > 0 :    #loop until node to visit is empty
            
        nextnode = None   # set next node to None

        for v in visited_list:   # loop through the visited list
        
            if nextnode == None :
                nextnode = v
                    
            elif g[v] + heriusticfcn(nodes.index(v)) < g[nextnode] + heriusticfcn(nodes.index(nextnode)):
                    nextnode = v
           
        if nextnode ==  'G':
            result_path = []           # list to store the optimal path: list for the shortest path found

            while parents[nextnode] != nextnode:
                result_path.append(nextnode)  # we add n to path 
                nextnode =parents[nextnode]

            result_path.append('A')   # we first add source node to result path
 
            result_path.reverse()    
            return result_path

            

        
        t=nodes.index(nextnode)  # check the index of the next node
        for l in graph2[t]:

            m=nodes[l]

            #print(cost[t,l],cost2[t][l])
            c=cost[t,l]
            #c=cost2[t][l]
                
            if m not in visited_list and m not in dest_list:
                visited_list.add(m)
                parents[m] = nextnode
                g[m] = g[nextnode] + c

            else:
                if g[m] > g[nextnode] + c:
                    g[m] = g[nextnode] + c
                    parents[m] = nextnode

                    if m in dest_list:
                        dest_list.remove(m)
                        visited_list.add(m)

        visited_list.remove(nextnode)  #remove n from the start list
        dest_list.add(nextnode)    #remove n from the destination list
            

    return result_path

# Node points 
nodes=['A','B','S','K','Y','N','Q','H','J','D','X','Z','E','P','T','F',
       'M','L','U','G']

N=len(nodes)  #Number of nodes

graph = []

cost={}      #cost


#our road map with cost
roadmap =[[['B',4],['N',4]],[['S',2],['Q',5],['A',4]],[['K',2],['H',5],['B',2]],[['Y',3],['J',5],['K',3]],[['D',3],['K',3]],
          
         [['Q',5],['X',7],['A',4]],     [['H',2],['Z',6],['N',5],['B',5]],      [['J',2],['E',2],['S',5],['Q',2]],  [['D',1],['P',8]], [['T',1],['Y',2],['J',1]],
          
         [['Z',2],['F',2],['N',7]],       [['E',10],['M',8],['Q',6],['X',5]],    [['P',8],['L',2],['H',2],['Z',10]], [['T',8],['U',8],['E',8],['J',8]],     [['G',3],['P',8],['D',1]],


         [['M',7],['X',7]], [['L',1],['F',8],['Z',9]], [['U',2],['E',2],['M',1]],   [['P',8],['G',2],['L',2]],  [['U',3],['T',3]]]


graph2=[]
cost2=[]

for g in range(len(roadmap)):
    m=roadmap[g]

    n=[nodes.index(i[0]) for i in m]

    graph2.append(n)
    mm=[]
    for i in range(len(m)):
        t=m[i]

        idx=nodes.index(t[0])

      
        cost[(g,idx)]=t[1]
        mm.append(t[1])
    cost2.append(mm)

print('The Result obtained from the A* Algorithm')
visitedlist=A_star_alg()  #obtain the visited nodes for the A* algorithm

# obtain the string nodes 
visitedstr=''
for r in visitedlist:
    visitedstr+=r+'-'

# print the results
print(visitedstr[:-1])


