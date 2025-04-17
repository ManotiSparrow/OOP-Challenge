# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  
        self.energy = 5  
        self.happiness = 5  
        self.tricks = []  
    def eat(self):
        """Decreases hunger by 3 points (not below 0) and increases happiness by 1."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate and feels a bit happier!")

    def sleep(self):
        """Increases energy by 5 points (not above 10)."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is well-rested and ready to go!")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had a lot of fun!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        """Prints the current state of the pet."""
        print(f"{self.name}'s Current Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        """Teaches the pet a new trick and stores it in the tricks list."""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """Prints all learned tricks."""
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
