import csv
import algorithm


class Weighted_Graph:
    def __init__(self):
        self.size = 0
        self.nodes = {}

    # Get weight by passed in vertices
    def get_weight_by_v(self, node1, node2):
        if node1 and node2 in self.nodes:
            return self.nodes[node1].get_weight(self.nodes[node2])

    # Add edge from the source node to the destination node
    def add_edge(self, source, dest, distance=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].add_adjacent(self.nodes[dest], distance)
        self.nodes[dest].add_adjacent(self.nodes[source], distance)

    # Add nodes to the graph
    def add_node(self, node):
        self.size = self.size + 1
        new_vertex = Nodes(node)
        self.nodes[node] = new_vertex
        return new_vertex

    # Return all nodes
    def get_nodes(self):
        return self.nodes.keys()

    # Return single node
    def get_node(self, node):
        if node in self.nodes:
            return self.nodes[node]
        else:
            print("Node not found")

    # Make the nodes iterable
    def __iter__(self):
        return iter(self.nodes.values())


class Nodes:
    def __init__(self, node):
        self.node_id = node
        self.adjacent = {}
        self.visited = False
        self.previous = None

    # Get node ID
    def get_id(self):
        return self.node_id

    # Get weight between neighbor node
    def get_weight(self, neighbor):
        return float(self.adjacent[neighbor])

    # Add an adjacent node
    def add_adjacent(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    # Return adjacent nodes
    def get_adjacent(self):
        return self.adjacent.keys()

    # Set previously visited node
    def set_previous(self, prev):
        self.previous = prev

    # get previously visited node
    def get_previous(self):
        return self.previous

    # Set node as visited
    def set_visited(self):
        self.visited = True


def load_graph(to_sort):
    # Open and read the distance table
    new_file = open('distance_table.csv')

    reader = csv.reader(new_file)
    header = []
    header = next(reader)

    new_rows = []
    for row in reader:
        new_rows.append(row)
        nRow = tuple(new_rows)

    g = Weighted_Graph()

    # Use the distance file to create a node out of every address
    for n in nRow:
        g.add_node(n[1])

    n = 0
    # Add all data from the distances file to the graph in order to be able to associate each address with another
    while n < len(nRow):
        g.add_edge(nRow[0][1], nRow[n][1], nRow[n][2])
        g.add_edge(nRow[1][1], nRow[n][1], nRow[n][3])
        g.add_edge(nRow[2][1], nRow[n][1], nRow[n][4])
        g.add_edge(nRow[3][1], nRow[n][1], nRow[n][5])
        g.add_edge(nRow[4][1], nRow[n][1], nRow[n][6])
        g.add_edge(nRow[5][1], nRow[n][1], nRow[n][7])
        g.add_edge(nRow[6][1], nRow[n][1], nRow[n][8])
        g.add_edge(nRow[7][1], nRow[n][1], nRow[n][9])
        g.add_edge(nRow[8][1], nRow[n][1], nRow[n][10])
        g.add_edge(nRow[9][1], nRow[n][1], nRow[n][11])
        g.add_edge(nRow[10][1], nRow[n][1], nRow[n][12])
        g.add_edge(nRow[11][1], nRow[n][1], nRow[n][13])
        g.add_edge(nRow[12][1], nRow[n][1], nRow[n][14])
        g.add_edge(nRow[13][1], nRow[n][1], nRow[n][15])
        g.add_edge(nRow[14][1], nRow[n][1], nRow[n][16])
        g.add_edge(nRow[15][1], nRow[n][1], nRow[n][17])
        g.add_edge(nRow[16][1], nRow[n][1], nRow[n][18])
        g.add_edge(nRow[17][1], nRow[n][1], nRow[n][19])
        g.add_edge(nRow[18][1], nRow[n][1], nRow[n][20])
        g.add_edge(nRow[19][1], nRow[n][1], nRow[n][21])
        g.add_edge(nRow[20][1], nRow[n][1], nRow[n][22])
        g.add_edge(nRow[21][1], nRow[n][1], nRow[n][23])
        g.add_edge(nRow[22][1], nRow[n][1], nRow[n][24])
        g.add_edge(nRow[23][1], nRow[n][1], nRow[n][25])
        g.add_edge(nRow[24][1], nRow[n][1], nRow[n][26])
        g.add_edge(nRow[25][1], nRow[n][1], nRow[n][27])
        g.add_edge(nRow[26][1], nRow[n][1], nRow[n][28])

        n += 1

    r = Weighted_Graph()
    to_sort.insert(0, 'HUB')

    for n in to_sort:
        r.add_node(n)

    n = 0
    # Associate the truck routes with the vertices and edges
    while n < len(to_sort):
        for i in to_sort:
            if i is not to_sort[n]:
                r.add_edge(to_sort[n], i, g.get_node(to_sort[n]).get_weight(g.get_node(i)))
        n += 1

    # Run the routes through the algorithm
    dist = algorithm.greedy(r)

    return dist
