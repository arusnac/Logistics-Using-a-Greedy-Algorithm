class HashTable(object):
    def __init__(self, size=80):
        self.array = [None] * size

    def create_hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def print_items(self):
        for i in self.array:
            print(i)

    def get_all_items(self):
        for item in self.array:
            return item

    def get_by_key(self, key):
        index = self.create_hash(key)
        #if self.array[index] is None:
            #raise KeyError()
        #else:
        for item in self.array[index]:
            if item[0] == key:
                return item[1]

            #raise KeyError()
    """Updates the status of the package"""
    def update_status(self, key, message):
        i = self.create_hash(key)
        for item in self.array[i]:
            if item[0] == key:
                self.array[i][0][1][7] = message
    """Returns package status"""
    def get_status(self, key):
        i = self.create_hash(key)
        for item in self.array[i]:
            if item[0] == key:
                return self.array[i][0][1][7]

    def insert(self, key, value):
        i = self.create_hash(key)
        if self.array[i] is not None:
            for item in self.array[i]:
                if item[0] == key:
                    item[1] = value
                    break
                else:
                    self.array[i].append([key, value])
        else:
            self.array[i] = []
            self.array[i].append([key, value])

        self.is_full()

    def is_full(self):
        items = 0

        for item in self.array:
            if item is not None:
                items += 1

        if items > len(self.array)/2:
            size = 120


    #def __setitem__(self, key, value):
        #self.add(key, value)

    #def __getitem__(self, key):
        #return self.get(key)


