#1 Create class and methods
class Animal:
    def __init__(self, genus, name, year_of_birth, movie):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.movie = movie

    def get_age(self, year):
        return current_year - self.year_of_birth

    def get_info(self):
        print(f"{self.name} is a(n) {self.genus}")

    def get_movie(self):
        print(f"{self.name} is from the movie '{self.movie}'")

# 2. Create a list of animals
animals = [
  Animal("elephant", "Dumbo", 1941, "Dumbo"),
  Animal("dog", "Balto", 1995, "Balto"),
  Animal("python", "Kaa", 1967, "The Jungle Book"),
  Animal("fox", "Nick", 2016, "Zootopia"),
  Animal("rat", "Remy", 2007, "Ratatouille"),
]

# Run methods for each animal
for animal in animals:
    print(f"Name: {animal.name}")
    animal.get_info()
    animal.get_movie()
    current_year = 2024
    age = animal.get_age(current_year)
    print(f"{animal.name} is {age} years old in {current_year}\n")

# 3. Find the oldest animal
def find_oldest_animal(animals):
    oldest_animal = animals[0]
    for animal in animals:
        if animal.get_age(2024) > oldest_animal.get_age(2024):
              oldest_animal = animal
    return oldest_animal

oldest = find_oldest_animal(animals)
print(f"The oldest animal is {oldest.name}, a(n) {oldest.genus}, {oldest.get_age(2024)} years old.")

# 4. Write animal information to a text file
with open("animals.txt", "w") as file:
    for animal in animals:
        file.write(f"{animal.name} is a(n) {animal.genus}\n")