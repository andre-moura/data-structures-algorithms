class HashTable:
    def __init__(self, size = 7 ):
        # Creating a list of size = 7 filled  with None
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)