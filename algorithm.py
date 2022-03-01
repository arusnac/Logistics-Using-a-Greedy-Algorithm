import sys

import truck


def greedy(graph):
    start = 'HUB'
    test = []
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
        current = None
        for node in unvisited:
            if current == None:
                current = node
            elif route[node] < route[current]:
                current = node
        # next = current
        print(current)
        n=graph.get_node(current)
        for w in n.get_adjacent():
            nid = n.get_id()
            wid = w.get_id()
            if wid not in unvisited:
                continue
            cost = route[current] + n.get_weight(w)
            next1 = wid

            if cost < route[wid]:
                # print(route[wid])
                #cost = route[current] + n.get_weight(w)
                route[wid] = cost
                previous[wid] = current
                # print(wid)
                # print(cost)
            #print(" current name = " + current + "current = " + str(
                #route[current]) + " neighbor = " + wid + " cost = " + str(cost) + " weight = " + str(n.get_weight(w)))
        unvisited.remove(current)
        """
        for n in graph:
            if n is graph.get_node(current):
                for w in n.get_adjacent():
                    nid = n.get_id()
                    wid = w.get_id()
                    if wid not in unvisited:
                        continue
                    cost = route[current] + n.get_weight(w)
                    next1 = wid

                    if cost < route[wid]:
                        #print(route[wid])
                        next1 = nid
                        #cost = route[current] + n.get_weight(w)
                        route[wid] = cost
                        previous[wid] = current
                        #print(wid)
                        #print(cost)
                    print(" current name = " + current + "current = " + str(route[current]) + " neighbor = " + wid + " cost = " + str(cost) + " weight = " + str(n.get_weight(w)))
        """
        # print(nid, cost)
        # truck.calculate_time(next1, cost)
        # print(current)
        # print(cost)
        # print(test)

        test.append(current)

        returned_route[current] = cost
        # truck.calculate_time(returned_route)
        distance = cost
        #print(returned_route)
    # print(test)
    # print(returned_route)
        print(distance)

    return distance, returned_route
