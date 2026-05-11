import random

class Character:
    def __init__(self, name, health, strength, experience=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.experience = experience
        self.level = 1

    def attack(self):
        print(f"{self.name} attacks with {self.strength} strength")

    def defend(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")

        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points!")
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= 100*self.level:
            self.level += 1
            self.strength += 10
            self.health += 20

            print(f"{self.name} has level up to level {self.level}! Strength and health increased")

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name, health, strength, armor):
        super().__init__(name, health, strength)
        self.armor = armor
        self.power_strike_cooldown = 0

    def defend(self, damage):
        reduced_damage = damage - self.armor
        if reduced_damage < 0:
            reduced_damage = 0
        self.health -= reduced_damage
        print(f"{self.name} defends with armor and takes {reduced_damage} damage! Remaining health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def power_strike(self, target):
        if self.power_strike_cooldown == 0:
            damage = self.strength * 2
            target.defend(damage)
            print(f"{self.name} uses Power Strike on {target.name}, dealing {damage} damage!")
            self.power_strike_cooldown = 3 # Cooldown for 3 rounds
        else:
            print(f"{self.name}'s Power Strike is on cooldown for {self.power_strike_cooldown} more turns.")

class Mage(Character):
    def __init__(self, name, health strength, mana):
        super().__init__(name, health, strength)
        self.mana = mana
        self.shield_active = False

    def cast_spell(self, spell_name, mana_cost, target=None):
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            if spell_name == "fireball":
                damage = self.strength*1.5
                if target:
                    target.defend(damage)
                    print(f"{self.name} casts Fireball on {target.name}, dealing {damage} damage!")
            elif spell_name == "shield":
                self.shield_active = True
                print(f"{self.name} casts Shield! Damage will be reduced for the next turn.")
        else:
            print(f"{self.name} doesn't have enough mana to cast {spell_name}!")

    def defend(self, damage):
        if self.shield_active:
            damage /= 2
            self.shield_active = False
            print(f"{self.name}'s shield reduces the damage by half!")
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")

class Rogue (Character):
    def __init__(self, name, health, strength, evasion_chance):
        super().__init__(name, health, strength)
        self.evasion_chance = evasion_chance

    def defend(self, damage):
        if random.random() < self.evasion_chance:
            print(f"{self.name} evades the attack!")
        else:
            self.health -= damage
            print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def backstab(self, target):
        if target.is_alive():
            damage = strength * 1.8
            target.defend(damage)
            print(f"{self.name} uses Backstab om {target.name}, dealing {damage} damage!")

# Battle simulstion
def battle_simulation(character1, character2):
    round_counter = 1
    while character1.is_alive() and character2.is_alive():
        print(f"---Round {round_counter}---")
        character1.attack()
        character2.defend(character1.strength)
        if character2.is_alive():
            character2.attack()
            character1.defend(character2.strength)
            round_counter += 1
            print(f"{character1.name} has {character1.health} health. {character2.name} has {character2.health} health. \n")

knight = Warrior("Sir Arthur",150,25,10)
mage = Mage("Merlin",100,20,50)
rogue = Rogue("Loki",120,15,0.3)

battle_simulation(knight, mage)
