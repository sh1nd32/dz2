class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger, self.energy, self.happiness = 50, 50, 50

    def adjust(self, hunger=0, energy=0, happiness=0):
        self.hunger = min(max(self.hunger + hunger, 0), 100)
        self.energy = min(max(self.energy + energy, 0), 100)
        self.happiness = min(max(self.happiness + happiness, 0), 100)

    def feed(self):
        if self.hunger > 20:
            print(f"{self.name} поїла.")
            self.adjust(hunger=-60)
        else:
            print(f"{self.name} неїлась.")

    def play(self):
        if self.energy > 20:
            print(f"{self.name} грає")
            self.adjust(happiness=50, energy=-10, hunger=50)
        else:
            print(f"{self.name} устала.")

    def sleep(self):
        if self.energy < 80:
            print(f"{self.name} хропить.")
            self.adjust(energy=30, hunger=20)
        else:
            print(f"{self.name} не хоче хропіти .")

    def status(self):
        print(f"\n--- {self.name} ---\nГолод: {self.hunger}/100\nЗаряд: {self.energy}/100\nЩастя: {self.happiness}/100")

my_pet = Pet("Луна", "Собака")
my_pet.feed()
my_pet.play()
my_pet.sleep()
my_pet.status()
