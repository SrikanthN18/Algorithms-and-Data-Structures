from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, node1, node2, both_ends=True):
        if both_ends:
            node_pairs = [[node1, node2], [node2, node1]]
        else:
            node_pairs = [[node1, node2]]
        return node_pairs

    def remove_edge(self, node1, node2, both_ends=True):
        node_pairs = self.get_node_pairs(node1, node2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, node1, node2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(node1, node2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(node1, node2))

        self.edges.append(Edge(start=node1, end=node2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=node2, end=node1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Provided src node is not available'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path,distances



#Change the Filename here to check output for different Graphs
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

g1 = [tuple(ele) for ele in graph]
g2 = ()
g3 = []

for ele in g1:
    g2=(ele[0],ele[1],int(ele[2]))
    g3.append(g2)
    del g2

inp_graph = Graph(g3)

inp_nodes = vertex.keys()
src_node = l[-1]

if info == 'D':
    if len(src_node) > 1:
        print("Available source nodes")
        print(inp_nodes)
        src = raw_input("Enter the src node\n")
    else:
        src = l[-1][0]

else:
    print("Please Provide the directed graph as Input\n")
    exit()


paths = []
for i in range(len(inp_nodes)):
    output = inp_graph.dijkstra(src,inp_nodes[i])
    print"SOURCE NODE: ",src
    print"DESTINATION NODE: ",inp_nodes[i]
    print"SHORTEST PATH: "
    if (output[0]):
        for ele in output[0]:
            print ele
    else:
        print "NO SHORTEST PATH"
    print"COST: ",output[1][inp_nodes[i]],"\n"

