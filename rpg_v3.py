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
