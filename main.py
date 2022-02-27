import hashtable
import csv

hashtable.HashTable

hash = hashtable.HashTable()

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

print(hash.get("4"))
