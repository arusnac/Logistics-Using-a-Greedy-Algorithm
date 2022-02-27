class Graph:
    def __init__(self, nodes, edges):
        self.adjacency = [None] * node

        for n in range(nodes):
            self.adjacency[n] = []

        for(start, dest, distance) in edges:
            self.adjacency[start].append((dest, distance))

    def PrintGraph(graph):
        for start in range(len(graph.adjacency)):
            for (dest, distance) in graph.adjacency[start]:
                print(f'({start}->{dest}, {distance})')
            print()
