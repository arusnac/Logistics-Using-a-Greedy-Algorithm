class HashTable(object):
    def __init__(self, size=3280):
        self.array = [None] * size
        self.size = size

    def create_hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def print_items(self):
        for i in self.array:
            if i is not None:
                print(i)

    def get_all_items(self):
        for item in self.array:
            return item

    def get_by_key(self, key):
        index = self.create_hash(key)
        for item in self.array[index]:
            if item[0] == key:
                return item[1]

    """Updates the status of the package"""
    def update_status(self, key, message, time):
        i = self.create_hash(key)
        for item in self.array[i]:
            if item[0] == key:
                self.array[i][0][1][7] = message
                self.array[i][0][1][8] = time
                break

    def update_address(self, key, address, zip):
        i = self.create_hash(key)
        for item in self.array[i]:
            if item[0] == key:
                self.array[i][0][1][1] = address
                self.array[i][0][1][4] = zip


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
        num = 0

        for i in self.array:
            if i is not None:
                num += 1

        if num == len(self.array):
            self.size *= 2


