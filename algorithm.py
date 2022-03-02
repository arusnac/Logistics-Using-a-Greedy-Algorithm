import sys

import truck


def greedy(graph):
    start = 'HUB'
    path = []
    distances = []
    returned_route = {}
    test_wid = ''
    weight = 0
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
        # print(current)
        n = graph.get_node(current)
        for w in n.get_adjacent():
            nid = n.get_id()
            wid = w.get_id()
            if wid not in unvisited:
                continue

            cost = route[current] + n.get_weight(w)
            next1 = wid
            # print(route[wid])
            if cost < route[wid] + n.get_weight(w):
                # print(route[wid])
                # cost = route[current] + n.get_weight(w)
                route[wid] = n.get_weight(w)
                previous[wid] = current
                # print(wid)
                # print(cost)
            next_node = n.set_previous(w)
            #print(" current name = " + current + "current = " + str(
                #route[current]) + " neighbor = " + wid + " cost = " + str(cost) + " weight = " + str(n.get_weight(w)))
            test_wid = wid
            #distances.append(route[wid])
            #path.append(wid)

            returned_route[wid] = route[wid]
        path.append(current)
        unvisited.remove(current)
        distances = []
        i=0
        #while i < len(path):


        #print(path)
        #print(previous)



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
        # print(path)

        #path.append(current)

        # truck.calculate_time(returned_route)
        distance = cost
        # print(returned_route)
    # print(route)
    count = 0
    # print(distance)
    while i < len(path):
        n = graph.get_node(path[i])
        m = graph.get_node(path[i+1])
        i += 1
        if i == len(path) - 1:
            n = graph.get_node(path[i])
            m = graph.get_node(path[-1])
            break
        count += float(n.get_weight(m))
        #print(str(n.get_weight(m)))
        distances.append(n.get_weight(m))
    #print(path)
    return distances, path
