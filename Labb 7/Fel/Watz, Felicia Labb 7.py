"""
Felicia Watz
Labbpartner Tove Lindegren
DD1320 Tillämpad Datalogi
Labb 6: Sökning och sortering
2023-10-13
"""
import csv


#  Uppgift 1
class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, key, data):
        self.dict[key] = data


    def __getitem__(self, key):
        return self.dict[key]

    def __contains__(self, key):
        if key in self.dict:
            return True
        else:
            return False


#Kod från lab 1
class Drama:
    def __init__(self, name, rating, actors, viewship_rating, genre, director, writer, year, nr_episodes, network):
        self.name = name
        self.rating = rating
        self.actors = actors
        self.viewship_rating = viewship_rating
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.nr_episodes = nr_episodes
        self.network = network

    def __str__(self):
        info_str = "Name of drama: " + self.name + "\n Actors: " + self.actors + "\n Rating: " + str(self.rating)
        return info_str

    def __lt__(self, other):
        return self.rating < other.rating


def drama_list_from_file(drama_dict):
    with open("kdrama_file.csv", "r") as drama_file:
        csvreader = csv.reader(drama_file)
        for row in csvreader:
            kdrama = Drama(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            drama_dict.store(row[0], kdrama)
    return drama_dict


def main():
    drama_dict = DictHash()
    kd_dict = drama_list_from_file(drama_dict)
    in_drama = input("Vilket kdrama letar du efter?: ")

    if in_drama in kd_dict:
        kdrama = kd_dict[in_drama]
        print(kdrama)
    else:
        print("Det existerar inte något drama vid det namnet på vår lista.")

main()


#  Uppgift 2

class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key="", data=None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data
      self.next = None

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:

   def __init__(self, size):
      """size: hashtabellens storlek"""
      self.size = size
      self.table =[None] * size
      self.krock = 0

   def store(self, key, data):
      """key är nyckeln
         data är objektet som ska lagras
         Stoppar in "data" med nyckeln "key" i tabellen."""
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
      """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
      index = self.hashfunction(key)
      node = self.table[index]

      while node is not None:
          if node.key == key: #and node.next is None:
              return node.data # för att få ut __str__
          node = node.next
      else:
         raise KeyError

   def hashfunction(self, key):
      """key är nyckeln
         Beräknar hashfunktionen för key"""
      return hash(key) % self.size
