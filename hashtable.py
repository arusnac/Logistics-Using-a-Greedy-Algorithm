class HashTable(object):
    def __init__(self, length=3124):
        self.array = [None] * length

    def hash(self, key):
        """get index of array for specific key"""
        length = len(self.array)
        return hash(key) % length

    def insert(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
                else:
                    self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            raise KeyError()


    def is_full(self):
        items = 0

        for item in self.array:
            if item is not None:
                items +=1

        return items > len(self.array)/2

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def printItems(self):
        for i in self.array:
            print(i)