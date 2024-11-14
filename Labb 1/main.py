import csv


drama_list = []


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


def two_drama_objs():
    drama1 = Drama('Baby Driver', 9.0, ['Big Ben', 'Scooby Doo'], 21.7, 'Mafia', 'Steven Spielberg', 'Arnold Schwarznegger', 2019, 12, 'Disney+')
    drama2 = Drama('NØG', 10, ['Heinz', 'Kancans'], 100, 'Reality', 'Toto', 'Gidfors', 2024, 1, 'MAX')

    print(drama1)
    print(drama2)

    print(drama1 < drama2)
    print(drama1.rating)
    print(drama2.rating)

    print(drama1.network)
    print(drama2.network)


def read_csv():
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
            drama_list.append(drama)


def search_drama():
    search = input('Enter drama name: ')
    print("Search results:")
    for drama in drama_list:
        if search.lower() in drama.drama_name.lower():
            print(drama)


def main():    
    read_csv()
    two_drama_objs()
    print()
    search_drama()


if __name__ == "__main__":
    main()