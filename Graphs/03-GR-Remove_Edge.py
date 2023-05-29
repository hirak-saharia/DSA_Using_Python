# Write a method called remove_edge that removes an edge between two vertices in the graph's adjacency list.

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
        
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    

    def remove_edge(self, v1, v2):

        # Check that both v1 and v2 are already in the graph
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():

            try:

                # Attempt to remove v2 from the adjacency list of v1 and vice versa
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            
            except ValueError:
                # If either v1 and v2 is not present in the adjacency list of the other, catch the exception and do nothing
                pass
            
            # Return true to indicate that the edge was successfully removed from the graph
            return True
        
        # if wither v1 and v2 is not in the graph, do not attempt to remove the edge
        #  return false to indicate that the edge was not removed from the graph
        return False


my_graph = Graph()

# Create three vertices
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

# Create edge to Connects the vertices all together
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')


# Remove the edge between A and B
my_graph.remove_edge('A', 'B')

# Remove the edge between A and B
my_graph.remove_edge('A', 'D')

my_graph.print_graph()