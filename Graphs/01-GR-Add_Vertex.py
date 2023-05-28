class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
                  
    def add_vertex(self, vertex):
        # check if the vertex is not already in the graph
        if vertex not in self.adj_list:
            # If the vertex is not already in the grapg, add it as a new key in the adj_list

            # With an empty list as its value
            self.adj_list[vertex] = []
            # Return true to indicate that the vertes was successfully added to the graph
            return True
        # If the vertex is already in the graph, do not add it again
        # Return False to indicate that the vertex was not added to the graph    
        return False
    

my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()