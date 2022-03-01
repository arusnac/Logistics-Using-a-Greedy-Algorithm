import sys


def dijkstra_algorithm(graph, truck_route, start_node):

    #print(truck_route)
    #unvisited_nodes = list(graph.get_nodes())
    unvisited_nodes = truck_route
    previous_nodes = {}
    #print(truck_route)
    route = {}
    max_value = sys.maxsize
    for i in unvisited_nodes:
        route[i] = max_value
    route[start_node] = 0
    current_node = start_node

    while unvisited_nodes:
        current_node = None
        for node in unvisited_nodes:
            if current_node == None:
                current_node = node
                #print(current_node)
            elif route[node] < route[current_node]:
                current_node = node
                #print(current_node)
            #current_node = start_node
            #for node in route:
                #if route[node] < route[current_node]:
                    #current_node = node


        neighbors = graph.get_edges(current_node)

        #print(neighbors)
        for item in neighbors:
            tentative_value = route[current_node] + graph.value(current_node, item)
            if tentative_value < route[item]:
                route[item] = tentative_value
                # We also update the best path to the current node
                print(current_node)
                previous_nodes[item] = current_node
        #print(current_node)
            # After visiting its neighbors, we mark the node as "visited"
        #print(unvisited_nodes)
        #print(previous_nodes)
        unvisited_nodes.remove(current_node)


    return previous_nodes, route


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
"""
    while unvisited_nodes:
        current_node = None
        for node in unvisited_nodes:
            if current_node is None:
                current_node = node
            elif route[node] < route[current_node]:
                current_node = node

        adjacent = graph.get_edges(current_node)
        for adj in adjacent:
            test_value = route[current_node] + graph.value(current_node, adj)
            if test_value < route[adj]:
                route[adj] = test_value
                previous_nodes[adj] = current_node

        unvisited_nodes.remove(current_node)

    print(route)
    """

