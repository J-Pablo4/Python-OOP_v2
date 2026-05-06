class Character:
    def __init__(self, name, health, strength):
        self.health = health
        self.name = name
        self.strength = strength

    def attack(self):
        print(f"{self.name} attacks with strength {self.strength}!")

    def defend(self, damage):
        self.health -= damage
        print(f"{self.name} defends and now has {self.health} health left.")

class Knight(Character):
    def __init__(self, name, health, strength, armor):
        super().__init__(name, health, strength)
        self.armor = armor

    def defend(self, damage):
        reduced_damage = damage - self.armor
        if reduced_damage < 0:
            reduced_damage = 0
        self.health -= reduced_damage
        print(f"{self.name} defends with armor and takes {reduced_damage} damage. Health left: {self.health}.")
        