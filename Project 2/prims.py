def matrix(V, G):
  
  adjMatrix = []
  
  for i in range(0, V):
    adjMatrix.append([])
    for j in range(0, V):
      adjMatrix[i].append(0)
      

  for i in range(0, len(G)):
    adjMatrix[G[i][0]][G[i][1]] = G[i][2]
    adjMatrix[G[i][1]][G[i][0]] = G[i][2]
    
  return adjMatrix

def prims(V,G):
  
  adjMatrix = matrix(V,G)
  vertex = 0 
  spanning_tree = []
  edges = []
  visited = []
  minEdge = [None,None,float('inf')]
  
  while len(spanning_tree) != V-1:
    visited.append(vertex)

    for r in range(0, V):
      if adjMatrix[vertex][r] != 0:
        edges.append([vertex,r,adjMatrix[vertex][r]])
        
    for e in range(0, len(edges)):
      if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
        minEdge = edges[e]
        
    edges.remove(minEdge)
    spanning_tree.append(minEdge)
    vertex = minEdge[1]
    minEdge = [None,None,float('inf')]
    
  return spanning_tree
  

#Change the Filename here to check for different Graphs
f1 = open("input2.txt","r")
l = []
for line in f1.readlines():
        x=line.split()
        l.append(x)

if len(l[-1]) > 1:
  graph = l[1:len(l)]
else:
  graph = l[1:len(l)-1]

nodes = []
info = l[0][2]
if info == 'D':
  print "Please Provide Undirected graph as Input"
  exit()
  
for ele in graph:
        node1 = ele[0]
        node2 = ele[1]
        if (node1 not in nodes):
                nodes.append(node1)
        if(node2 not in nodes):
                nodes.append(node2)


d = {}
for ele in nodes:
	x ={}
	d[ele] = x

for i in range(len(graph)):
	node1 = graph[i][0]
	node_2 = graph[i][1]
	cost = int(graph[i][2])
	d[node1] ={node_2:cost}
	for j in range(len(graph)):
		if node1 in graph[j][0]:
			node2 = graph[j][1]
			cost1 = int(graph[j][2])
			d[node1].update({node2:cost1})
		else:
			continue

vertex = {}
for i in range(len(nodes)):
	vertex[nodes[i]] = i

lst1 = []
lst2 = []
for x,y in d.items():
	if len(y.values())!=0:
		for k,v in y.items():
			lst1.append(x)
			lst1.append(k)
			lst1.append(int(v))
			lst2.append(lst1)
			lst1 = []		


#lst2 contains the graph input with alphabets as it is from input file


lst3 = []
lst4 =[]
for ele in lst2:
	lst3.append(vertex.get(ele[0]))
	lst3.append(vertex.get(ele[1]))
	lst3.append(ele[2])
	lst4.append(lst3)
	lst3 = []

#lst4 contains the graphs with alphabets changed to numbers
#Ex: A-> 0, B-> 1, C-> 2 ..

no_of_vertices = int(l[0][0])
out = prims(no_of_vertices,lst4)

lst5 = []
lst6 = []

for ele in out:
	key1 = vertex.keys()[vertex.values().index(ele[0])]
	key2 = vertex.keys()[vertex.values().index(ele[1])]
	value = ele[2]
	lst5.append(key1)
	lst5.append(key2)
	lst5.append(value)
	lst6.append(lst5)
	lst5 = []


#lst6 contains the output with numbers changes to alphabets i.e., 0 -> A, 1 -> B, 2 -> c ..
print("MINIMUM SPANNING TREE:")
print(lst6)

cost = 0
for ele in lst6:
	cost += ele[2]

print("TOTAL COST: ")
print(cost)	
