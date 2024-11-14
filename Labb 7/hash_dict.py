import csv


class DictHash():
    def __init__(self):
        self.hash = {}


    def store(self, nyckel, data):
        self.hash[nyckel] = data


    def search(self, nyckel):
        if nyckel not in self.hash:
            return None
        return self.hash[nyckel]


    def __getitem__(self, nyckel):
        return self.hash[nyckel]


    def __contains__(self, nyckel):
        return nyckel in self.hash          # Returnerar True om nyckeln finns i hashen, annars False
    

class Drama:
    def __init__(self, drama_name, rating, actors, viewship_rate, genre, director, writer, year, no_of_episodes, network):
        self.drama_name = drama_name
        self.rating = rating
        self.actors = actors
        self.viewship_rate = viewship_rate
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.no_of_episodes = no_of_episodes
        self.network = network


    def __str__(self):
        return f'{self.drama_name} ({self.year})'
    

    def __lt__(self, other):
        return self.rating < other.rating
    

    def rating(self):
        return self.rating
    

    def network(self):
        return self.network
    

def read_csv():
    drama_table = DictHash()
    with open('kdrama.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            drama_name = row[0]
            rating = row[1]
            actors = row[2]
            viewship_rate = row[3]
            genre = row[4]
            director = row[5]
            writer = row[6]
            year = row[7]
            no_of_episodes = row[8]
            network = row[9]

            drama = Drama(drama_name, rating, actors, viewship_rate, genre, director, writer, year, no_of_episodes, network)
            drama_table.store(drama_name, drama)
    return drama_table


def main():
    drama_table = read_csv()
    print("Sökning som finns med:", drama_table.search('The Heirs'))  
    print("Sökning som INTE finns med:", drama_table.search('Baby Driver'))


if __name__ == '__main__':
    main()