#breadth first search algorithm
def breadth_first_search():

    visitedlist=''  # list to store visited nodes
           
    c = [False for i in range(len(nodepoint))]    # create boolean list to check if a node is visited 

    c[0] = True   # set the first point to be True

    v = [0] # add to the list of visited nodes

            
    while len(v)>0:  # check if visited node is empty and we stop

        s = v.pop(0)  # remove the node that is added

        visitedlist+=nodepoint[s] + '-'  # append result to the visited list
        for i in graph2[s]: 
                    
            if c[i] == False:  # check the node and if it not visited
                        
                v.append(i)  # append node to visited node
                c[i] = True     # set condition to be true


    return visitedlist[:-1]

#nodes for the map
nodepoint=['A','B','S','K','Y','N','Q','H','J','D','X','Z','E','P','T','F',
       'M','L','U','G']


# create the road map using 2D array, each index has the branch nodes
roadmap =[ ['B','N'],['S','Q'],['K','H'],['Y','J'],['D'],
         ['Q','X'],['H','Z'],['J','E'],['D','P'],['T'],
         ['Z','F'],['E','M'],['P','L'],['T','U'],['G'],
         ['M'],['L'],['U'],['G'],['U']]

# create the graph 
graph2=[]
for g in range(len(roadmap)):
    m=roadmap[g]

    n=[nodepoint.index(i) for i in m]

    graph2.append(n)

    for i in range(len(m)):
        t=m[i]

print("Applying the BFS Algorithm")
visitedlist=breadth_first_search()
print(visitedlist)
