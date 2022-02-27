import hashtable

hashtable.HashTable

hash = hashtable.HashTable()

hash.insert("test", "1")
hash.insert("af", "2")
hash.insert("bb", "3")
print(hash.get("test") + hash.get("af"))
