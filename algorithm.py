import sys


def greedy(graph):
    start = 'HUB'
    path = []
    distances = []
    returned_route = {}

    route = {}
    previous = {}
    unvisited = []

    for vertex in graph:
        unvisited.append(vertex.get_id())

    max_val = sys.maxsize
    for vertex in unvisited:
        route[vertex] = max_val

    route[start] = 0

    while unvisited:
        current = None
        for vertex in unvisited:
            if current is None:
                current = vertex
            elif route[vertex] < route[current]:
                current = vertex

        n = graph.get_node(current)
        for w in n.get_adjacent():
            nid = n.get_id()
            wid = w.get_id()
            if wid not in unvisited:
                continue

            cost = route[current] + n.get_weight(w)

            if cost < route[wid] + n.get_weight(w):
                route[wid] = n.get_weight(w)
                previous[wid] = current

            returned_route[wid] = route[wid]
        path.append(current)
        unvisited.remove(current)
        distances = []
        i = 0

    count = 0

    # Put the path taken in order into a list
    # Place the distance in a list for later manipulation
    while i < len(path) - 1:
        n = graph.get_node(path[i])
        m = graph.get_node(path[i + 1])
        i += 1
        count += float(n.get_weight(m))
        distances.append(n.get_weight(m))

    return distances, path
