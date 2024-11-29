#Example of Superhero and superman games 
# Base Superhero Class
class Superhero:
    def __init__(self, name, superpower, health, level):
        self.name = name  # Superhero's name
        self.superpower = superpower  # Superhero's power
        self._health = health  # Private health attribute (encapsulated)
        self.level = level  # Hero's level or experience
        
    # Getter for health (encapsulation)
    def get_health(self):
        return self._health
    
    # Setter for health (encapsulation)
    def set_health(self, value):
        if value > 0:
            self._health = value
        else:
            print(f"{self.name}'s health can't be less than 0.")
    
    # Method to display superhero info
    def display_info(self):
        print(f"Superhero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Health: {self.get_health()}")
        print(f"Level: {self.level}")
    
    # Method for a superhero to attack
    def attack(self):
        print(f"{self.name} uses {self.superpower} to attack!")
    
    # Method to heal the superhero
    def heal(self, amount):
        new_health = self.get_health() + amount
        self.set_health(new_health)
        print(f"{self.name} has healed and now has {self.get_health()} health.")

# Subclass of Superhero to represent a Flying Hero
class FlyingHero(Superhero):
    def __init__(self, name, superpower, health, level, flying_ability):
        # Inherit attributes from the Superhero class
        super().__init__(name, superpower, health, level)
        self.flying_ability = flying_ability  # Unique attribute for FlyingHero
    
    # Overridden method to display FlyingHero info
    def display_info(self):
        super().display_info()  # Call the parent class's display_info method
        print(f"Flying Ability: {self.flying_ability}")
    
    # Polymorphic attack method for FlyingHero
    def attack(self):
        print(f"{self.name} flies high and uses {self.superpower} to attack from the sky!")

# Create a Superhero object
hero1 = Superhero("Ironman", "Repulsor Rays", 100, 5)

# Create a FlyingHero object
hero2 = FlyingHero("Superman", "Heat Vision", 150, 10, "Super Speed Flying")

# Display hero info
hero1.display_info()
print()
hero2.display_info()

# Demonstrate attack and healing
hero1.attack()
hero2.attack()

# Heal the heroes
hero1.heal(20)
hero2.heal(50)