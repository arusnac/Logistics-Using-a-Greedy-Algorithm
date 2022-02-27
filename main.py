import hashtable
import csv

from weighted_graph import Graph

hashtable.HashTable

hash = hashtable.HashTable()
graph_function = Graph
hash.insert("test", "1")
hash.insert("af", "2")
hash.insert("bb", "3")
print(hash.get("test") + hash.get("af"))

file = open('packages.csv')

csvreader = csv.reader(file)

next(csvreader, None)
rows = []

for row in csvreader:
    hash.insert(row[0], row)

new_file = open('distance_table.csv')
reader = csv.reader(new_file)

header = []
header = next(reader)

new_rows = []
for row in reader:
    new_rows.append(row)

n = 10
#edges = [(header[1], new_rows[1], )]

print(header)
print(new_rows)