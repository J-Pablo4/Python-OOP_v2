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

    def defend(self, damage):
        reduced_damage = damage - self.armor
        if reduced_damage < 0:
            reduced_damage = 0
        self.health -= reduced_damage
        print(f"{self.name} defends with armor and takes {reduced_damage} damage. Remaining health!")

class Mage(Character):
    def __init__(self, name, health, strength, mana):
        super().__init__(name, health, strength)
        self.mana = mana

    def cast_spell(self, spell_name, mana_cost):
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            print(f"{self.name} casts {spell_name} using {mana_cost} mana! Remaining mana: {self.mana}")
        else:
            print(f"{self.name} doesn't have enough mana to cast {spell_name}!")
    
    def attack(self):
        if self.mana > 0:
            self.cast_spell("Fireball", 10)
        else:
            print(f"{self.name} has no mana left and attacks with a staff!")

class Archer(Character):
    def __init__(self, name, health, strength, range):
        super().__init__(name, health, strength)
        self.range = range