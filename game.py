import random
class Character:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name
  
  def get_life(self):
    return self.__life
  
  def get_level(self):
    return self.__level
  
  def show_details(self):
    return f"Name: {self.get_name()} \n Life: {self.get_life()} \n Level: {self.get_level()}"
  
  def reduce_life(self, damage):
    self.__life -= damage
    if self.__life < 0:
      self.__live = 0

  def attack(self, target):
    damage = random.randint(self.get_level() * 2, self.get_level() * 4)
    target.reduce_life(damage)
    print(f"{self.get_name()} has attacked {target.get_name()} and caused {damage} damage.")

  
class Hero(Character):
  def __init__(self, name, life, level, special_abilities):
    super().__init__(name, life, level)
    self.__special_abilities = special_abilities

  def get_special_abilities(self):
    return self.__special_abilities
  
  def show_details(self):
    return f"{super().show_details()} \nSpecial Abilities: {self.get_special_abilities()} \n"
  
  def special_attack(self, target):
    damage = random.randint(self.get_level() * 5, self.get_level() * 8)
    target.reduce_life(damage)
    print(f"{self.get_name()} has use an speccial attack {self.get_special_abilities()} on {target.get_name()} and caused {damage} damage.")
  
class Enemy(Character):
  def __init__(self, name, life, level, kind):
    super().__init__(name, life, level)
    self.__Kind = kind

  def get_kind(self):
    return self.__Kind
  
  def show_details(self):
    return f"{super().show_details()} \n Kind: {self.get_kind()} \n"


class Game:
  def __init__(self) -> None:
    self.hero = Hero(name="John Doe", life=100, level=5, special_abilities="Blizzard")
    self.enemy = Enemy(name="Dragon", life=90, level=4, kind="Fire")


  def start_battle(self):
    print("Starting battle: ")
    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      print("\n Characters details: ")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      print("Press Enter to attack...")
      choice = input("Choose 1 - Normal Attack, 2 - Special Attack: ")

      if choice == '1':
        self.hero.attack(self.enemy)
      elif choice == '2':
        self.hero.special_attack(self.enemy)
      else:
        print("Choice not avaialable.")

      if self.enemy.get_life() > 0:
        print(f"It's the {self.enemy.get_name()} turn.")
        self.enemy.attack(self.hero)

    if self.hero.get_life() > 0:
      print(f"\n The enemy {self.enemy.get_name()} has no life anymore.")
      print(f"\nCongratulations!!! You won the battle.")
    else:
      print(f"\n You lost!!!")

game = Game()
game.start_battle()

