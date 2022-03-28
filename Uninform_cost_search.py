def uniform_cost_search(graph,targets):
	
    penalty=10000    # set penalty value
    
    pirority = []       # list to store the pirority

    
    min_cost=[penalty for i in range(len(targets))]  #create list to store the minimum cost and set all to be the penalty value
        
    pirority.append([0, 0])   # add first node to the queue
	
    visited = {}      

    counter = 0         # set counter to 0


    while (len(pirority) > 0):  

        pirority.sort()    # the pirority queue is sorted in ascending order

        p = pirority.pop(-1)   

        p[0] =p[0]* -1        # multiple the pirority point by -1


        if (p[1] in targets):     # check if the piority point is in the list of target

            index = target.index(p[1])  # extract the index from the list of target

            if (min_cost[index] == penalty): #check if the minimum cost for the index is equal to the maximum
                    counter += 1 

            if (min_cost[index] > p[0]):
                min_cost[index] = p[0]

            pirority.pop(-1)    # remove the last point from the pirority

            pirority.sort()             # sort the queue
            if (counter == len(listtargetgoal)):  # if counter os equal to the goal, we return the minimum cost
                return min_cost, visited
         
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                

                pirority.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

                visited[p[1]] = 1
        if p[1]==19:
            break

    return min_cost, visited

# Node points 
nodes=['A','B','S','K','Y','N','Q','H','J','D','X','Z','E','P','T','F',
       'M','L','U','G']

#our road map with cost
roadmap =[[['B',4],['N',4]],[['S',2],['Q',5],['A',4]],[['K',2],['H',5],['B',2]],[['Y',3],['J',5],['K',3]],[['D',3],['K',3]],
          
         [['Q',5],['X',7],['A',4]],     [['H',2],['Z',6],['N',5],['B',5]],      [['J',2],['E',2],['S',5],['Q',2]],  [['D',1],['P',8]], [['T',1],['Y',2],['J',1]],
          
         [['Z',2],['F',2],['N',7]],       [['E',10],['M',8],['Q',6],['X',5]],    [['P',8],['L',2],['H',2],['Z',10]], [['T',8],['U',8],['E',8],['J',8]],     [['G',3],['P',8],['D',1]],


         [['M',7],['X',7]], [['L',1],['F',8],['Z',9]], [['U',2],['E',2],['M',1]],   [['P',8],['G',2],['L',2]],  [['U',3],['T',3]]]


graph = []
cost={}      #cost

graph2=[]
for g in range(len(roadmap)):
    m=roadmap[g]

    n=[nodes.index(i[0]) for i in m]

    graph2.append(n)

    for i in range(len(m)):
        t=m[i]
        c=nodes.index(t[0])

        cost[(g,c)]=t[1]
        
         
print('Result obtained from the Uniform Cost search algorithm')
mincost,visitednodes= uniform_cost_search(graph2,[20])   # obtain the results from the uniform search algorithm

visitednodes=[nodes[i] for i in visitednodes]  #obtain all string using the index from uniform search algorithm

# obtain the string nodes 
visitedstr=''
for r in visitednodes:
    visitedstr+=r+'-'

# print the results
print('Optimized route= ',visitedstr[:-1])
