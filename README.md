![banner](https://res.cloudinary.com/dloadb2bx/image/upload/v1704943653/python_rvcah5.png)
# RPG Battle Simulator

This Python project is part of the second class in the **[Rocketseat Python specialization](https://www.rocketseat.com.br/)**. It serves as a simple RPG (Role-Playing Game) Battle Simulator, focusing on reinforcing and applying essential concepts such as inheritance, polymorphism, encapsulation, and decorators. The primary objective is to provide hands-on experience and comfort with Object-Oriented Programming (OOP) principles in Python.

## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Classes

### `Character`

The `Character` class serves as the base class for both heroes and enemies. It encapsulates essential attributes such as name, life, and level. The class also provides methods for displaying character details, reducing life based on damage, and performing basic attacks.

### `Hero`

The `Hero` class inherits from `Character` and introduces additional attributes, like special abilities. It overrides the `show_details` method to include the hero's unique features and implements a `special_attack` method for a more powerful attack.

### `Enemy`

Similarly, the `Enemy` class inherits from `Character` and introduces a unique attribute, such as the enemy's kind (e.g., Fire, Dragon). The `show_details` method is overridden to include the enemy's specific information.

### `Game`

The `Game` class orchestrates the battles between a predefined hero and enemy. It includes a method `start_battle` that simulates a turn-based battle until either the hero or the enemy runs out of life points. The battle supports both normal and special attacks.

## Getting Started

To run the RPG Battle Simulator, instantiate the `Game` class and execute the `start_battle` method. Follow the on-screen prompts to choose between normal and special attacks during the battle.

```python
# Example usage
game = Game()
game.start_battle()
