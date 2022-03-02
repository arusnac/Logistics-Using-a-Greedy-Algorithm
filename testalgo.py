import sys

def greedy(graph):
    start = 'HUB'
    test=[]
    returned_route = {}
    returned_route['HUB'] = 0;
    route = {}
    previous = {}
    unvisited = []
    distance = 0
    next1 = None
    for node in graph:
        unvisited.append(node.get_id())

    max_val = sys.maxsize
    for node in unvisited:
        route[node] = max_val

    route[start] = 0

    while unvisited:
        current = graph.get_node(unvisited[1])
        current.set_visited()

        for next in current.get_adjacent():
            if next.visited:
                continue
            dist = current.get_weight() + current.get_weight(next)

            #if dist < next:

