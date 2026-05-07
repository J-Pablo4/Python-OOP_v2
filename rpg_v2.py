class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        print(f"{self.name} attack with {self.strength} strength!")

    def defend(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0

class Knight(Character):
    def __init__(self, name, health, strength, armor):
        super().__init__(name, health, strength)
        self.armor = armor

class Mage(Character):
    def __init__(self, name, health, strength, mana):
        super().__init__(name, health, strength)
        self.mana = mana

class Archer(Character):
    def __init__(self, name, health, strength, range):
        super().__init__(name, health, strength)
        self.range = range