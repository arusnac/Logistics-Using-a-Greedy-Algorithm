import algo
import hashtable
import csv

# from weighted_graph import Graph
from vertex import WGraph
from weighted_graph import Graph


hashtable.HashTable

hash = hashtable.HashTable()

file = open('packages.csv')

csvreader = csv.reader(file)

next(csvreader, None)
rows = []

for row in csvreader:
    hash.insert(row[0], row)
test_route = []
i = 1


while i < 10:
    index = str(i)
    address = hash.get(index)
    address = address[1] + " (" + address[4] + ")"
    test_route.append(address)
    i += 1

test_route.append('HUB')

new_file = open('distance_table.csv')

reader = csv.reader(new_file)
header = []
header = next(reader)

new_rows = []

for row in reader:
    new_rows.append(row)
    n = 10

    nList = []
    i = 0

    tHeader = tuple(header)
    nRow = tuple(new_rows)

    i = 0
while i < len(nRow):
    items = []
    item = new_rows
    nList.append(item[i][1])
    i += 1

nodes = []

for i in nList:
    nodes.append(i)



start = {}

for node in nodes:
    start[node] = {}


g = WGraph()

for n in nRow:
    g.add_vertex(n[1])

n = 0
s = 2
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

    n+=1

"""
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print(vid, wid, v.get_weight(w))
"""
"""
for v in g:
    print(v.get_id(), g.vert_dict[v.get_id()])
"""
test_dict = {}
i = 0
print(test_route)
while i < len(test_route):
    print(g.get_vertex(test_route[i]).get_weight(g.get_vertex(test_route[i+1])))
    i+=1

print(g.get_vertex(nRow[0][1]).get_weight(g.get_vertex(nRow[26][1])))


while n < len(nodes):
    start[nRow[0][1]][nRow[n][1]] = nRow[n][2]
    start[nRow[1][1]][nRow[n][1]] = nRow[n][3]
    start[nRow[2][1]][nRow[n][1]] = nRow[n][4]
    start[nRow[3][1]][nRow[n][1]] = nRow[n][5]
    start[nRow[4][1]][nRow[n][1]] = nRow[n][6]
    start[nRow[5][1]][nRow[n][1]] = nRow[n][7]
    start[nRow[6][1]][nRow[n][1]] = nRow[n][8]
    start[nRow[7][1]][nRow[n][1]] = nRow[n][9]
    start[nRow[8][1]][nRow[n][1]] = nRow[n][10]
    start[nRow[9][1]][nRow[n][1]] = nRow[n][11]
    start[nRow[10][1]][nRow[n][1]] = nRow[n][12]
    start[nRow[11][1]][nRow[n][1]] = nRow[n][13]
    start[nRow[12][1]][nRow[n][1]] = nRow[n][14]
    start[nRow[13][1]][nRow[n][1]] = nRow[n][15]
    start[nRow[14][1]][nRow[n][1]] = nRow[n][16]
    start[nRow[15][1]][nRow[n][1]] = nRow[n][17]
    start[nRow[16][1]][nRow[n][1]] = nRow[n][18]
    start[nRow[17][1]][nRow[n][1]] = nRow[n][19]
    start[nRow[18][1]][nRow[n][1]] = nRow[n][20]
    start[nRow[19][1]][nRow[n][1]] = nRow[n][21]
    start[nRow[20][1]][nRow[n][1]] = nRow[n][22]
    start[nRow[21][1]][nRow[n][1]] = nRow[n][23]
    start[nRow[22][1]][nRow[n][1]] = nRow[n][24]
    start[nRow[23][1]][nRow[n][1]] = nRow[n][25]
    start[nRow[24][1]][nRow[n][1]] = nRow[n][26]
    start[nRow[25][1]][nRow[n][1]] = nRow[n][27]
    start[nRow[26][1]][nRow[n][1]] = nRow[n][28]

    n += 1

# start["test3"]["test4"] = nRow[1][2]
# start[tHeader[3]][nRow[1][1]] = nRow[1][2]
# start[tHeader[4], nRow[2][1]] = nRow[2][2]
# start[tHeader[5], nRow[3][1]] = nRow[3][2]
# print(start)
newGraph = Graph(nodes, start)
newStart = {}
#newStart[nRow[1][0]][nRow[n][1]] = nRow[n][28]


# print(newGraph.value(nRow[15][0], nRow[10][0]))
# print(nRow[15][0])
# print(newGraph.value(nRow[15][0], nRow[25][0]))
end = test_route[8]
prev, route = algo.dijkstra_algorithm(newGraph, test_route, start_node=nRow[0][1])
# algo.print_result(prev, route, start_node=nRow[0][1], target_node=test_route[-2])
print(prev)
#algo.print_result(prev, route, start_node=nRow[0][1], target_node=end)
# print(newGraph.get_edges(nRow[0][0]))
# newGraph.create_graph()


# print(edges)
# print('origin= ', header[2], 'location= ', new_rows[0][1], 'distance= ', new_rows[0][2])
# print(new_rows)
