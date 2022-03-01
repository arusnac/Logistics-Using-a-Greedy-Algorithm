import csv


class Graph:
    def __init__(self, nodes, start):
        self.nodes = nodes
        self.graph = self.create_graph(nodes, start)

    def create_graph(self, nodes, start):
        graph = {}
        for n in nodes:
            graph[n] = {}

        graph.update(start)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        return self.nodes

    def get_edges(self, node):
        conn = []
        for out in self.nodes:
            if self.graph[node].get(out, False):
                conn.append(out)
        return conn

    def value(self, node1, node2):
        return float(self.graph[node1][node2])




