"""
class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        pass

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount


class Soldier(Unit):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health)
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power


class Archer(Unit):
    def __init__(self, name, health, range_attack_power):
        super().__init__(name, health)
        self.range_attack_power = range_attack_power

    def attack(self, target):
        target.health -= self.range_attack_power

# Создание армии
soldier = Soldier("Солдат", 100, 10)
archer = Archer("Лучник", 80, 8)

# Симуляция боя
while soldier.is_alive() and archer.is_alive():
    soldier.attack(archer)
    if archer.is_alive():
        archer.attack(soldier)

# Определение победителя
if soldier.is_alive():
    print(f"{soldier.name} победил!")
else:
    print(f"{archer.name} победил!")
"""