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
  
  def details(self):
    return f"Name: {self.get_name()} \n Life: {self.get_life()} \n Leve: {self.get_level()}"
  
class Hero(Character):
  def __init__(self, name, life, level, special_abilities):
    super().__init__(name, life, level)
    self.__special_abilities = special_abilities

  def get_special_abilities(self):
    return self.__special_abilities
  
  def details(self):
    return f"{super().details()} \nSpecial Abilities: {self.get_special_abilities()} \n"
  
class Enemy(Character):
  def __init__(self, name, life, level, kind):
    super().__init__(name, life, level)
    self.__Kind = kind

  def get_kind(self):
    return self.__Kind
  
  def details(self):
    return f"{super().details()} \n Kind: {self.get_kind()} \n"


hero_1 = Hero(name="John Doe", life=100, level=5, special_abilities="Blizzard")
enemy_1 = Enemy(name="Dragon", life=70, level=3, kind="Fire")

print(hero_1.details())
print(enemy_1.details())