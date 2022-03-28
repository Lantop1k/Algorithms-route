#each node for the map
nodepoint=['A','B','S','K','Y','N','Q','H','J','D','X','Z','E','P','T','F',
       'M','L','U','G']

# create the road map using 2D array, each array store the branches 
roadmap =[ ['B','N'],['S','Q'],['K','H'],['Y','J'],['D'],
         ['Q','X'],['H','Z'],['J','E'],['D','P'],['T'],
         ['Z','F'],['E','M'],['P','L'],['T','U'],['G'],
         ['M'],['L'],['U'],['G'],['U']]

graph2=[]
for g in range(len(roadmap)):
    m=roadmap[g]

    n=[nodepoint.index(i) for i in m]

    graph2.append(n)

    for i in range(len(m)):
        t=m[i]


visitednode = [] # list to check if a node is visited

visitedlist=''   # string to create visited nodes uisng the dash

print("Result obtained from the Depth-First Search")

#Applying the Depth frist search algorithm
def depth_first_search(visitednode, graph,node):

    global visitedlist
    if not(node in visitednode):  
        
        visitedlist+=nodepoint[node]+'-'
        
        visitednode.append(node)  

        
        for adjacentnode in graph[node]:  
            depth_first_search(visitednode, graph, adjacentnode)  

depth_first_search(visitednode,graph2, nodepoint.index('A'))
seqnode=visitedlist[:-1]  #sequence of visted nodes
print(seqnode)

