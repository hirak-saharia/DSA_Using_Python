# Write a method called add_edge to the Graph class that adds a new edge between two vertices in the graph's adjacency list

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return
    
    # The method takes two parameters v1 and v2, which are the vertices that the edge should be added between.
    def add_edge(self, v1, v2):

        # check that both vertex v1 and v2 are already in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():

            # Add v2 to the adjacency list for v1 and vice versa
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

            # Return true to indicate that the edge was successfully added to the grapg
            return True
        
        # if either v1 and v2 is not in the graph, do not add the edge
        # return false to indicate that the edge was not added to the graph
        return False




my_graph = Graph()

# my_graph.add_vertex('A')

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()