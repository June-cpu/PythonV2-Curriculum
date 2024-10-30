# all planets and their description 
from riddles import riddles
from game import intro
from game import ilavurs
from game import shummoor
from game import lulucia
from game import vixia
from game import arispade
from game import icriss
from game import galem
from game import earth
import random

# Adventurer class to track player's stats and actions
class Adventurer:
    def __init__(self, name):
        self.name = name
        self.health = 100  # Starting health
        self.fuel = 50     # Starting fuel
        self.food = 3      # Starting food

    def use_fuel(self, amount):
        if self.fuel >= amount:
            self.fuel -= amount
            print(f"{self.name} used {amount} fuel. Remaining fuel: {self.fuel}")
        else:
            print(f"{self.name} does not have enough fuel to travel.")

    def eat(self):
        if self.food > 0:
            self.food -= 1  
            self.health += 10  
            print(f"{self.name} ate food. Health restored to {self.health}.")
        else:
            print(f"{self.name} has no food to eat.")

    def is_alive(self):
        return self.health > 0

class Planet:
    def __init__(self, name):
        self.name = name

    def challenge(self, adventurer):
        print(f"{adventurer.name} is facing a challenge on {self.name}!")
        success = random.choice([True, False])
        if success:
            print(f"Challenge on {self.name} succeeded!")
        else:
            print(f"Challenge on {self.name} failed!")
            adventurer.health -= 20  # Reduce health on failure
        return success


ilavurs = Planet("Ilavurs")
shummoor = Planet("Shummoor")
lulucia = Planet("Lulucia")
vixia = Planet("Vixia")
arispade = Planet("Arispade")
icriss = Planet("Icriss")
galem = Planet("Galem")
earth = Planet("Earth")

def intro():
    print("Welcome to 'Astra Lost in Space'!")
    print("In this text-based adventure game, you will join a group of friends stranded in space after a mysterious incident.")
    print("You must explore various planets, solve riddles, and gather resources to survive and find a way back home.")
    print("\nAbout the Anime:")
    print("Astra Lost in Space follows a group of high school students who go on a camping trip in space.")
    print("After an unexpected event, they find themselves on a journey across uncharted planets, facing numerous challenges.")
    print("As they navigate through these strange worlds, they must rely on each other and their wits to survive.")
    print("\nAre you ready to embark on this adventure? Let's begin!")

def start():
    intro()

    adventurer = Adventurer(name="Luna")

    planets = [ilavurs, shummoor, lulucia, vixia, arispade, icriss, galem, earth]

    for planet in planets:
        print(f"\nArriving at planet {planet.name.capitalize()}!")
        
        success = planet.challenge(adventurer)

        if success:
            adventurer.use_fuel(10)  
            adventurer.eat()    
        else:
            if not adventurer.is_alive():
                print(f"{adventurer.name} did not survive the journey. Game Over!")
                return

        if adventurer.fuel <= 0:
            print(f"{adventurer.name} has run out of fuel and cannot continue. Game Over!")
            return
        if not adventurer.is_alive():
            print(f"{adventurer.name} has perished from exhaustion. Game Over!")
            return

    print(f"Congratulations! {adventurer.name} has successfully visited all planets and completed the adventure!")

if __name__ == "__main__":
    start()




start()