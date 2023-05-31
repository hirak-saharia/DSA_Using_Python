# The remove_vertex method removes a vertex from the graph along with all edges connected to it. The method takes a single parameter, vertex, which is the name of the vertex to be removed.


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
        
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    


    def remove_vertex(self, vertex):

        # Check if the vertex to be removed is in the adjacency list
        if vertex in self.adj_list.keys():
            
            # If it does, loop over all vertices adjacent to the vertex to be removed
            for other_vertex in self.adj_list[vertex]:

                # Remove the vertex to be removed from the list of adjacent vertices of the other vertices
                self.adj_list[other_vertex].remove(vertex)
            
            # After removing all the edges, remove the vertex from the adjaceny list
            del self.adj_list[vertex]

            # Return True to indicate that the vertex was successfully removed the graph
            return True

        # If the vertex to be removed is not in the graph, return False
        return False






my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

print('Graph before remove_vertex():')
my_graph.print_graph()

my_graph.remove_vertex('D')

print('\nGraph after remove_vertex():')
my_graph.print_graph()

