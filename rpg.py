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

class MagicUser:
    def __init__(self, mana):
        self.mana = mana

    def cast_spell(self):
        print("Casting a spell...")
        self.mana -= 10

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

class Archer(Character):
    def __init__(self, name, health, strength, range):
        super().__init__(name, health, strength)
        self.range = range

    def attack(self):
        print(f"{self.name} shoots an arrow from {self.range} meters away with strength {self.strength}.")

class Mage(Character, MagicUser):
    def __init__(self, name, health, strength, mana):
        Character.__init__(self, name, health, strength)
        MagicUser.__init__(self, mana)
    
    def attack(self):
        self.cast_spell()
        print(f"{self.name} casts a magic attack with strenght {self.strength}!")

knight = Knight("Sir Rose", 100, 50, 20)
archer = Archer("Robin Hood", 80, 40, 30)

knight.attack()
knight.defend(40)

archer.attack()
archer.defend(40)

mage = Mage("Merlin", 60, 20, 100)
mage.attack()
mage.cast_spell()
mage.defend(30)
