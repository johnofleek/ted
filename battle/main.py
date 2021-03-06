# windows colors workaround
import colorama

colorama.init()

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

print("\n\n")

# Create black magic
fire = Spell("Fire      75 ", 10, 75, "black")
thunder = Spell("Thunder   100", 15, 100, "black")
blizzard = Spell("Blizzard  125", 17, 250, "black")
meteor = Spell("Meteor    190", 25, 500, "black")
quake = Spell("Quake     500", 40, 700, "black")

#Create white magic
cure = Spell("Cure", 12, 900, "white")
cura = Spell("Cura", 18, 1200, "white")
        
#Create some items
potion = Item("Potion", "potion", "Heals 50HP", 50)
hipotion = Item("Alex's 'special' potion", "potion", "Heals 100HP", 100)
Bob = Item("Bob piss", "potion", "Heals 200HP", 200)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)   
hielixer = Item("Fruity elixer", "elixer", "Fully restores HP/MP for whole party", 9999)
poison = Item("Literal poison", "potion", "Why would you, you dumb f**k", -10)
battery = Item("Dodgy battery", "attack", "????", 300)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 5}, {"item": hipotion, "quantity": 5},
                {"item": Bob, "quantity":3}, {"item": elixer, "quantity":2},
                {"item": hielixer, "quantity":1}, {"item": poison, "quantity":1},
                {"item": battery, "quantity":1}]
                

#Instantiate people
player1 = Person("Nathan:", 3000, 65, 120, 34, player_spells, player_items)
player2 = Person("Edward:", 2500, 65, 180, 34, player_spells, player_items)
player3 = Person("Ryan  :", 1500, 99, 80, 34, player_spells, player_items)

enemy2 = Person("Steve Hackett", 1000, 200, 250, 120, [], [])
enemy1 = Person("Phil Collins ", 5000, 200, 250, 25, [], [])
enemy3 = Person("Peter Gabriel", 1500, 120, 120, 120, [], [])

players = [player2, player1, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("======================")
    
    print("\n\n")   
    print("NAME                  HP                                  MP")
    for player in players:
        player.get_stats()
        
    print("\n")
    
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    for player in players:
    
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            
            
            enemies[enemy].take_damage(dmg)
            print("You attacked" + enemies[enemy].name + "for", dmg, "points of damage.")
            
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ","") + " has ded")
                del enemies[enemy]
                
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1
            
            if magic_choice == -1:
                continue
            
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            
            current_mp = player.get_mp()
            
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.cost)    
        
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals", str(magic_dmg), "points of damage" + bcolors.ENDC)
            elif spell.type == "black":
            
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_dmg)
                
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace (" ", "") + " has ded")
                    del enemies[enemy]
                
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1
            
            if item_choice == -1:
                continue
                
            item = player.items[item_choice]["item"]
            
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue
                
            player.items[item_choice]["quantity"] -= 1
            
            
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
            
                if item.name == "hielixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":            
                enemy = player.choose_target(enemies)            
                enemies[enemy].take_damage(item.prop)                
                print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has ded")
                        del enemies[enemy]
                        
    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()
    
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg)
        
    defeated_enemies = 0
    defeated_players = 0
    
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
            
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
            
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        
    elif defeated_players == 2:
        print(bcolors.FAIL + "You ded" + bcolors.ENDC)
        running = False
