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

clasa Healer(Character):
    def __init__(self, name, health, strength, healing_power):
        super().__init__(name, health, strength)
        self.healing_power = healing_power

    def heal(self, ally):
        print(f"{self.name} heals {ally.name} for {self.healing_power} health points!")
        ally.health += self.healing_power

        if ally.health > 100:
            ally.health = 100

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

    def attack(self):
        print(f"{self.name} shoots an arrow from {self.range} meters away with {self.strength} strength!")


# Test classes
def battle_round(character1, character2):
    print(f"{character1.name} vs {character2.name}")

    character1.attack()
    character2.defend(character1.strength)

    if character2.is_alive():
        character2.attack()
        character1.defend(character2.strength)
    
    print(f"End of round: {character1.name} has {character1.health} health, {character2.name} has {character2.health} health\n")

knight = Knight("Sir Lancelot", 100, 20, 5)
mage = Mage("Gandalf", 80, 10, 50)
archer = Archer("Robin Hood", 90, 15, 25)

battle_round(knight, mage)
battle_round(archer, knight)
battle_round(mage, archer)

healer = Healer("Florence", 60, 5, 30)
healer.heal(knight)
print(f"{knight.name}'s health after healing: {knight.health}")

