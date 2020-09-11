from collections import defaultdict,OrderedDict 
  
class Graph:

	def distance(self,dist,queue): 
		minimum = float("Inf") 
		min_index = -1
          
		for i in range(len(dist)): 
			if dist[i] < minimum and i in queue: 
				minimum = dist[i] 
				min_index = i 
		return min_index 
  
	def Path(self, parent, j): 
          
		if parent[j] == -1 :  
			print j, 
			return
		self.Path(parent , parent[j]) 
		print j, 
          
  
	def Solution(self, dist, parent,src): 
		print "SOURCE VERTEX IS ",src
		print("Vertex \t\tCost from Source\t\t\tPath") 
		for i in range(0, len(dist)): 
			print("\n%d \t\t%d \t\t\t\t\t" % (i, dist[i])), 
			self.Path(parent,i) 
  
  
	def dijkstra(self, graph, src): 
  
		row = len(graph) 
		col = len(graph[0]) 
  
		dist = [float("Inf")] * row 
  
		parent = [-1] * row 
  
		dist[src] = 0
      
		queue = [] 
		for i in range(row): 
			queue.append(i) 
              
        #Find shortest path for all vertices 
		while queue: 
  
			u = self.distance(dist,queue)  
  
			queue.remove(u) 
  
			for i in range(col): 
				if graph[u][i] and i in queue: 
					if dist[u] + graph[u][i] < dist[i]: 
						dist[i] = dist[u] + graph[u][i] 
						parent[i] = u 
  
  

		self.Solution(dist,parent,src) 
  



###################### Create Adjacency Matrix ######################
def matrix(V,G):
	adjMatrix = []
 
	for i in range(0, V):
		adjMatrix.append([])
		for j in range(0, V):
			adjMatrix[i].append(0)
      

	for i in range(0, len(G)):
		adjMatrix[G[i][0]][G[i][1]] = G[i][2]
		adjMatrix[G[i][1]][G[i][0]] = G[i][2]
   
	return adjMatrix
 
#####################################################################

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


#Info tells whether graph is directed or undirected
info = l[0][2]


nodes = []
for ele in graph:
        node1 = ele[0]
        if (node1 not in nodes):
                nodes.append(node1)

for ele in graph:
        node2 = ele[1]
        if(node2 not in nodes):
                nodes.append(node2)


d = OrderedDict()
for ele in nodes:
	x =OrderedDict()
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

if info == 'U':
	for k,v in d.items():
		for i,j in v.items():
			d[i].update({k: j})


vertex = OrderedDict()
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
graph = matrix(no_of_vertices,lst4)

nodes = vertex.keys()

############Get the src node############
src_node = l[-1]
if info == 'U':
	if len(src_node) > 1:
		print("Available source nodes")
		print(nodes)
		src = raw_input("Enter the src node\n")
	else:
		src = l[-1][0]

else:
	print("Please Provide the undirected graph as Input\n")
	exit()


src_vertex = vertex[src]
print ("FYI. In the output,Each vertex is assigned a number .Ex: A--> 0,B --> 1 and so on.\n")
print "Following are the vertices"
print vertex
g= Graph() 
g.dijkstra(graph,src_vertex)
