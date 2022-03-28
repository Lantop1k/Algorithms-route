from queue import PriorityQueue

#The unique Node points that will be visited  
nodepoint=['A','B','S','K','Y','N','Q','H','J','D','X','Z','E','P','T','F',
       'M','L','U','G']

#our road map with cost
roadmap =[[['B',4],['N',4]],[['S',2],['Q',5],['A',4]],[['K',2],['H',5],['B',2]],[['Y',3],['J',5],['K',3]],[['D',3],['K',3]],
          
         [['Q',5],['X',7],['A',4]],     [['H',2],['Z',6],['N',5],['B',5]],      [['J',2],['E',2],['S',5],['Q',2]],  [['D',1],['P',8]], [['T',1],['Y',2],['J',1]],
          
         [['Z',2],['F',2],['N',7]],       [['E',10],['M',8],['Q',6],['X',5]],    [['P',8],['L',2],['H',2],['Z',10]], [['T',8],['U',8],['E',8],['J',8]],     [['G',3],['P',8],['D',1]],


         [[['M',7],['X',7]], [['L',1],['F',8],['Z',9]], ['U',2],['E',2],['M',1]],   [['P',8],['G',2],['L',2]],  [['U',3],['T',3]]]


def greedybest(destination, n):

    cond= [False for i in range(len(nodepoint))]    # create boolean list to check if a node is visited 

    cond[0] = True   # set the first point to be True
        
    pq = PriorityQueue() #create empty prority queue
    
    pq.put((0, 0))  # first point of the priority queue is set to 0 (A index)

    visitedlist=''   # list to store visited nodes
  
    while pq.empty() == False:
  
        node_lowest_cost = pq.get()[1]  # get the node point that yield the lowest cost
        visitedlist+=nodepoint[node_lowest_cost] +'-'  # append result to the visited list
     
        if node_lowest_cost == destination:  #if the node that yield lowest cost is the same as the destination node
            break   #stop the iteration

        for idx,c in roadmap[node_lowest_cost]: 

            idx=nodepoint.index(idx)
            if cond[idx] == False: # check the node and if it not visited
                        
                cond[idx] = True  # append node to visited node
                pq.put((c, idx))   # set condition to be true


    return visitedlist[:-1]
	

print('Result from the Greedy Best First Search')

visitedlist=greedybest(nodepoint.index('G'), len(nodepoint))   # applying the functi
print(visitedlist)  


