
class HashNode:
   def __init__(self, nyckel = "", data = None):
      self.nyckel = nyckel
      self.data = data
      self.next = None


class Hashtable():
    def __init__(self, size):
        self.hash = [None] * size
        self.size = size
        # self.krock = 0


    def store(self, nyckel, data):
        index = self.hashfunction(nyckel)

        if self.hash[index] is not None:
            # self.krock += 1
            
            node = self.hash[index]
            if node.nyckel == nyckel:
                node.data = data
            elif node.next is None:
                node.next = HashNode(nyckel, data)
            else:
                while node.next is not None:
                    node = node.next
                    if node.nyckel == nyckel:
                        node.data = data
                        break
                else:
                    node.next = HashNode(nyckel, data)
        else:
            self.hash[index] = HashNode(nyckel, data)


    def search(self, nyckel):
        index = self.hashfunction(nyckel)
        node = self.hash[index]

        while node is not None:
            if node.nyckel == nyckel:
                return node.data
            node = node.next
        else:
            raise KeyError

    def hashfunction(self, nyckel):
        i = 32
        hash_value = 0

        for character in nyckel:
            hash_value = (hash_value * i + ord(character)) % self.size

        return hash_value
    

    def __getitem__(self, nyckel):
        return self.search(nyckel)
    

    def __setitem__(self, nyckel, data):
        self.store(nyckel, data)