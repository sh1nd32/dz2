class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 20:
            self.hunger -= 20
            print(f"{self.name} смачно поїв!")
        else:
            print(f"{self.name} не голодний зараз.")

    def play(self):
        if self.energy > 20:
            self.happiness += 10
            self.energy -= 20
            self.hunger += 10
            print(f"{self.name} весело грається!")
        else:
            print(f"{self.name} занадто втомлений, щоб гратися.")

    def sleep(self):
        if self.energy < 80:
            self.energy += 20
            self.hunger += 10
            print(f"{self.name} міцно спить.")
        else:
            print(f"{self.name} зараз не хоче спати.")

    def status(self):
        print(f"Статус {self.name}:")
        print(f"  Голод: {self.hunger}/100")
        print(f"  Енергія: {self.energy}/100")
        print(f"  Щастя: {self.happiness}/100")

my_pet = Pet("Барсик", "кіт")
my_pet.status()
my_pet.feed()
my_pet.play()
my_pet.sleep()
my_pet.status()
