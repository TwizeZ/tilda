
class HashNode:
    def __init__(self, key = "", data = None):
      self.key = key
      self.data = data
      self.next = None


class Hashtable:
   def __init__(self, size):
      self.size = size
      self.table =[None] * size
      self.krock = 0


   def store(self, key, data):
      index = self.hashfunction(key)


      if self.table[index] is None:
          self.table[index] = HashNode(key, data)
      else:
          self.krock += 1

          current_node = self.table[index]
          if current_node.key == key:
              current_node.data = data
          elif current_node.next is None:
              current_node.next = HashNode(key, data)
          else:
              while current_node.next is not None:
                  current_node = current_node.next
                  if current_node.key == key:
                      current_node.data = data
                      break
                  elif current_node.next is None:
                      current_node.next = HashNode(key, data)
                      break


   def search(self, key):
      index = self.hashfunction(key)
      node = self.table[index]

      while node is not None:
          if node.key == key: #and node.next is None:
              return node.data # för att få ut __str__
          node = node.next
      else:
         raise KeyError


   def hashfunction(self, key):
      return hash(key) % self.size