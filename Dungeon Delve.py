import random
import time
import pyfiglet

#In every following variable, the word 'modifier' has been shortened to mod
class Player:
    def __init__(self, name, difficulty_level):
        self.max_health = 5.0
        self.health = 5.0
        self.name = name
        self.sword_mod = 1.0
        self.score = 0
        self.gold = 0
        self.potions = 0
        self.death = False
        self.difficulty = difficulty_level
        self.score_mod = 1
#Method to set the amount of points the player should get in each difficulty.
    def set_score_modifier(self):
        if self.difficulty == "easy":
            self.score_mod = 0.5
        elif self.difficulty == "medium":
            self.score_mod = 1
        elif self.difficulty == "Hard":
            self.score_mod = 1.5
    def print_stats(self):
        print("Health: ",
                              self.health,
                              "/",
                              self.max_health,
                              sep="")
        print("Name:", self.name)
        print("Gold:", self.gold)
        print("Potions:", self.potions)
        print("Sword upgrades: +", (self.sword_mod - 1) * 2,
              sep="")
        print("Score:", self.score)

class Treasure:
    def __init__(self, current_level):
        self.current_level = current_level
# method to generate the contents of a treasure room for each different level.
    def treasure_room(self):
        #Level 1- they can only have health potions
        if self.current_level == "1":
            print("You got a health potion.")
            player.potions += 1
        #Level 2- 5% chance for a sword upgrade, 5% chance for an armour upgrade, 35% chance for a healing potion, 55% chance for 25-50 gold.
        elif self.current_level == "2f2" or self.current_level == "2f1":
            treasure = random.randint(1, 20)
            if treasure == 20:
                print("You got a better weapon!")
                player.sword_mod += 0.5
            elif treasure == 19:
                print(
                    "You found some better armour! You now have more health.")
                player.max_health += 2
                player.health += 2
            elif 12 <= treasure <= 18:
                print("You got a health potion.")
                player.potions += 1
            else:
                treasure = random.randint(25, 50)
                player.gold += treasure
                print("You got", treasure, "gold")
        #Level 3- Same probabilities as level 2, except with 50-75 gold instead of 25-50
        elif self.current_level == "3f4" or self.current_level == "3f3" or self.current_level == "3f2" or self.current_level == "3f1":
            treasure = random.randint(1, 20)
            if treasure == 20:
                print("You got an upgrade for your sword!")
                player.sword_mod += 0.5
            elif treasure == 19:
                print(
                    "You found some better armour! You now have more health.")
                player.max_health += 2
                player.health += 2
            elif 12 <= treasure <= 18:
                print("You got a health potion.")
                player.potions += 1
            else:
                treasure = random.randint(50, 75)
                player.gold += treasure
                print("You got", treasure, "gold")
# All commented point gains are described at medium difficulty- they will be multiplied by the difficulty score modifier
    def enemy_drop(self):
        #Level 1- defeating an enemy awards 10 points
        if self.current_level == "1":
            points = 10 * player.score_mod
            player.score += points
            print("You got", points, "points")
        #level 2- defeating an enemy has a 10% chance for a health potion, a 70% chance for 10-25 gold or a 20% chance to get nothing. The player is also awarded 10 points
        elif self.current_level == "2f2" or self.current_level == "2f1":
            treasure = random.randint(1, 10)
            if treasure == 10:
                print("The enemy was carrying a spare health potion!")
                player.potions += 1
            elif treasure == 1 or treasure == 2:
                print("The enemy wasn't carrying anything of value")
            else:
                treasure = random.randint(10, 25)
                player.gold += treasure
                print("The enemy had", treasure, "gold on them.")
            points = 10 * player.score_mod
            player.score += points
            print("You got", points, "points")
        #Level 3- Same probabilities as level 2, except with 15-35 gold instead of 10-25, and they are awarded 20 instead of 10 points.
        elif self.current_level == "3f4" or self.current_level == "3f3" or self.current_level == "3f2" or self.current_level == "3f1":
            treasure = random.randint(1, 10)
            if treasure == 10:
                print("The enemy was carrying a spare health potion!")
                player.potions += 1
            elif treasure == 1 or treasure == 2:
                print("The enemy wasn't carrying anything of value")
            else:
                treasure = random.randint(15, 35)
                player.gold += treasure
                print("The enemy had", treasure, "gold on them.")
            points = 20 * player.score_mod
            player.score += points
            print("You got", points, "points")
        #Level 4- the only enemy is the final boss, which awards 100 points when defeated.
        elif self.current_level == "4":
            points = 100 * player.score_mod
            player.score += points
            print("You got", points, "points")


class Enemy:
    def __init__(self, current_level):
        self.current_level = current_level
        self.enemy_type = ""
        self.enemy_mod = ""
        self.health = 0
        self.attack_mod = 0
        self.battle = True
    
    def generate_enemy(self):
        #Level 1- The enemy is a goblin, with 1 health and 1 attack
        if self.current_level == "1":
            self.enemy_type = "Goblin"
            self.health = 1
            self.attack_mod = 1
        #Level 2- The enemies are goblins that have 2 health and 1 attack, and have a 25% chance to be either a fire, water, earth or normal goblin
        elif self.current_level == "2f1" or self.current_level == "2f2":
            self.enemy_type = "Goblin"
            self.health = 2
            self.attack_mod = 1
            self.enemy_mod = random.choice(["Fire", "Water", "Earth", ""])
        #Level 3- The enemies have a 2/3 to be a goblin that has 3 health and 1 attack, or a 1/3 chance to be a troll that has 5 health and 1.5 attack. Either enemy has a 1/4 chance to be fire, water, earth or a normal enemy.
        elif self.current_level == "3f1" or self.current_level == "3f2" or self.current_level == "3f3" or self.current_level == "3f4":
            random_gen = random.randint(1, 3)
            if random_gen == 3:
                self.enemy_type = "Troll"
                self.health = 5
                self.attack_mod = 1.5
            else:
                self.enemy_type = "Goblin"
                self.health = 3
                self.attack_mod = 1
            self.enemy_mod = random.choice(["Fire", "Water", "Earth", ""])
        #Level 4 only has the final boss, an ogre which has 8 health and 1.5 attack on easy difficulty, 12 health and 2 attack on medium difficulty, or 16 health and 2 attack on hard difficulty.
        elif self.current_level == "4":
            self.enemy_type = "Ogre"
            if player.difficulty == "easy":
                self.health = 8
                self.attack_mod = 1.5
            elif player.difficulty == "medium":
                self.health = 12
                self.attack_mod = 2
            elif player.difficulty == "hard":
                self.health = 16
                self.attack_mod = 2

    def fight(self):
        player_move = ""
        enemy_move = ""
        turn_counter = 0
        previous_player_move = ""
        previous_enemy_move = ""
        #A random message is shown when a fight begins, and a unique one is shown for the final boss.
        random_choice = random.choice([
            "jumps out of the shadows to attack you!",
            "was waiting in the room you just walked into, get ready for a fight!",
            "stands up and points its weapon at you, shouting a warcry!",
            "pushes you back as you stumble through the door, and tries to stab you!"
        ])
        if self.current_level == "4":
            print(
                "As you step through the large doorway, you hear loud snoring.\nYou tiptoe forward, trying not to wake it, but soon you hear a loud roar as a gigantic ogre lumbers forward.\nYou ready your sword one last time."
            )
        else:
            print("A", self.enemy_mod, self.enemy_type, random_choice)
        while self.battle == True:
            #At the start of a turn of combat, the variables to keep track of the previous turn's moves are set, the option_selected ceck variable and element modifier are reset and the turn counter is incremented.
            option_selected = False
            element_mod = 1
            turn_counter += 1
            print("Turn", turn_counter)
            previous_player_move = player_move
            previous_enemy_move = enemy_move
            #The enemy will always attack after a boost, otherwise they will either attack, defend or boost.
            if previous_enemy_move == "boost":
                enemy_move = "attack"
            else:
                enemy_move = random.choice(["attack", "defend", "boost"])
            #Every odd-numbered turn, the player can see the enemy's next turn, while every even-numbered turn they cannot.
            if turn_counter % 2 == 1:
                print("The enemy is getting ready to", enemy_move)
            else:
                print("You can't tell what the enemy is about to do!")
            #Validation loop for the player to choose their move, they can only 
            while option_selected == False:
                #The player can try to flee if they defended the previous turn and they aren't fighting the final boss.
                if previous_player_move == "defend" and self.current_level != "4":
                    player_move = input(
                        "Do you want to attack, defend, heal, or flee?\n~")
                    player_move = player_move.lower()
                    #The validation loop will only end when the player selects a valid move- attack, defend, in this case, flee and if the are missing health and have potions, heal. They can also view their stats, but that won't end their turn.
                    if player_move == "attack" or player_move == "defend" or player_move == "flee":
                        option_selected = True
                    elif player_move == "heal":
                        if player.potions > 0 and player.health < player.max_health:
                            option_selected = True
                        else:
                            if player.potions <= 0:
                                print("You have no healing potions left.")
                            elif player.health == player.max_health:
                                print("You are already at maximum health.")
                    elif player_move == "status":
                        player.print_status()
                    else:
                        print("That isn't a valid action")
                #This input is used when the player didn't defend the previous turn, so they can't flee.
                else:
                    player_move = input(
                        "Do you want to attack, defend, or use a healing potion? (enter heal to do that)\n~"
                    )
                    player_move = player_move.lower()
                    if player_move == "attack" or player_move == "defend":
                        option_selected = True
                    elif player_move == "heal":
                        if player.potions > 0 and player.health < player.max_health:
                            option_selected = True
                        else:
                            if player.potions <= 0:
                                print("You have no healing potions left.")
                            elif player.health == player.max_health:
                                print("You are already at maximum health.")
                    elif player_move == "status":
                        player.print_status()
                    else:
                        print("That isn't a valid action")

            option_selected = False
            #if the player is attacking an enemy with an elemental modifier, they must choose an element to imbue their attack with. These two elements are then compared, if the attacking element is strong against the enemy's, it does 1.5 times the damage, if it's weak, it does 0.5 times the damage, and if the elements are the same the damage is normal.
            if self.current_level != "1" and player_move == "attack" and self.enemy_mod != "":
                while option_selected == False:
                    weapon_element = input(
                        "Which element do you want to imbue your attack with, out of fire, water or earth?\n~"
                    )
                    weapon_element = weapon_element.lower()
                    if weapon_element == "fire" or weapon_element == "water" or weapon_element == "earth":
                        option_selected = True
                    else:
                        print("That isn't a valid element")
            if self.enemy_mod == "fire":
                if weapon_element == "water":
                    element_mod = 1.5
                elif weapon_element == "earth":
                    element_mod = 0.5
            elif self.enemy_mod == "earth":
                if weapon_element == "fire":
                    element_mod = 1.5
                elif weapon_element == "water":
                    element_mod = 0.5
            elif self.enemy_mod == "water":
                if weapon_element == "earth":
                    element_mod = 1.5
                elif weapon_element == "fire":
                    element_mod = 0.5
            #Player damage is 1 * the element modifier * the sword modifier(increased with sword upgrades)
            player_damage = 1 * element_mod * player.sword_mod
            #Enemy attacks deal double damage after they boost.
            if previous_enemy_move == "boost":
                enemy_damage = (1 * self.attack_mod) * 2
            else:
                enemy_damage = 1 * self.attack_mod
            #When the player attacks, if the enemy attacks, both of them take damage. If the Enemy defends, the player has a 50% chance to hit the enemy. If the enemy is boosting, the player can freely attack them.
            if player_move == "attack":
                if enemy_move == "attack":
                    player.health -= enemy_damage
                    self.health -= player_damage
                    print("You have", player.health, "health left")
                    print(
                        "You both trade blows, each taking a sizeable amount of damage"
                    )
                elif enemy_move == "defend":
                    random_chance = random.randint(0, 1)
                    if random_chance == 0:
                        print(
                            "You try to get in a hit, but the enemy blocks your attack!"
                        )
                    elif random_chance == 1:
                        print(
                            "You manage to attack them before they have a chance to block you!"
                        )
                        self.health -= player_damage
                elif enemy_move == "boost":
                    print(
                        "The enemy was too busy boosting their next attack to stop you from damaging them!"
                    )
                    self.health -= player_damage
            # When the player defends, it will block an enemy's attack and let them try to flee next turn
            elif player_move == "defend":
                if enemy_move == "attack":
                    print(
                        "You quickly raise your shield, and you take no damage since the enemy's weapon bounces off with a loud 'clang'!"
                    )
                elif enemy_move == "defend":
                    print(
                        "You both make defensive manoeuvres at each other, neither one of you successfully strike each other."
                    )
                elif enemy_move == "boost":
                    print(
                        "You ready yourself to block their next attack, but the enemy seems to be trying to strengthen its next attack."
                    )
            #When the player heals, the enemy will be able to attack it, but if the enemy defends or boosts the player can freely heal.
            elif player_move == "heal":
                if enemy_move == "attack":
                    print(
                        "You manage to quick chug down a healing potion, but the enemy still gets in a few hits while you were busy with that!"
                    )
                    print("You healed 1 health")
                    player.health += 1
                    player.health -= enemy_damage
                    player.potions -= 1
                    print("You have", player.health, "health left")
                    print("You have", player.potions, "healing potions left")
                elif enemy_move == "defend":
                    print(
                        "The enemy starts trying to block your attacks, so you take the chance to use a healing potion."
                    )
                    print("You healed 1 health")
                    player.health += 1
                    player.potions -= 1
                    print("You have", player.health, "health left")
                    print("You have", player.potions, "healing potions left")
                elif enemy_move == "boost":
                    print(
                        "You drink a healing potion while the enemy starts to strengthen its next attack."
                    )
                    print("You healed 1 health")
                    player.health += 1
                    player.potions -= 1
                    print("You have", player.health, "health left")
                    print("You have", player.potions, "healing potions left")
            #There is a 50% chance the player can flee.
            elif player_move == "flee":
                random_chance = random.randint(0,1)
                if random_chance == 1:
                    print(
                        "You try to run from the", self.enemy_type +
                        ", and manage to hide for long enough that it leaves this room."
                    )
                    self.battle = False

                elif random_chance == 0:
                    print("You try to run from the",
                          self.enemy_type + ", but it catches up with you!")
            #The battle only ends if the player or enemy runs out of health, and in the case of the former the game ends. 
            if player.health <= 0:
                print("You have run out of health")
                death_screen = pyfiglet.figlet_format("You Died")
                print(death_screen)
                self.battle = False
                player.death = True

            elif self.health <= 0:
                print("You have defeated the enemy!")
                self.battle = False

class map:
    def __init__(self, map_data, current_level):
        self.map_data = map_data
        self.vertical_border = " ---     "
        self.opening_up = " -↑-     "
        self.opening_down = " -↓-     "
        self.current_level = current_level
        self.shop_potions = 5
        self.sword_upgrades = 2
        self.armour_upgrades = 2
#Scrapped map printing code (Bits of it are useful, but when implemented fully it looks like nonsense)
# def room(map_data, Type):
#     vertical_border = " ---"
#     wall = "|"
#     corridor = "==="
#     if Type == "entrance":
#         print(vertical_border,"\n", wall, map_data[find_player(map_data)][0], corridor, "\n", vertical_border, end="")
#     if Type == "corridor":
#         print(vertical_border,"\n", corridor, map_data[find_player(map_data)][0], corridor, "\n", vertical_border, end="")
#     if Type == "exit":
#         print(vertical_border,"\n", corridor, map_data[find_player(map_data)][0], wall, "\n", vertical_border, end="")

#Refined map printing algorithm, works much better
    #Method to find the player's location on the map
    def find_player(self):
        for i in range(0, len(self.map_data)):
            if self.map_data[i][0] == 1:
                return (i)
    #Each row of rooms is made up of 3 layers- the top, which shows the ceilings and openings to go up, the middle, which shows the player's location, corridors, horizontal walls and the exit room's location, and the bottom, which shows the floor and openings down.
    def print_map(self):
        #Top layer- If the player has entered this room before, and there an opening to go up then an opening up is printed, if there isn't an opening up a section of ceiling is printed, and if the room hasn't been discovered a blank space is printed.
        for i in range(0, len(self.map_data)):
            if self.map_data[i][2] == True and self.map_data[i][4] != "up":
                print((self.vertical_border), end="")
            elif self.map_data[i][2] == True:
                print((self.opening_up), end="")
            else:
                print("         ", end="")
        print("")
        #Middle layer- If the player has entered this room before, the current_room subclass is instantiated with the room's data, and its print_room method is used, and if the room hasn't been discovered a blank space is printed.
        for i in range(0, len(self.map_data)):
            current_room = room(self.map_data[i][3], i, self.map_data)
            if self.map_data[i][2] == True:
                current_room.print_room()
            else:
                print("        ", end="")
        print("")
        #Bottom layer- If the player has entered this room before, and there an opening to go down then an opening down is printed, if there isn't an opening up a section of floor is printed, and if the room hasn't been discovered a blank space is printed.
        for i in range(0, len(self.map_data)):
            if self.map_data[i][2] == True and self.map_data[i][4] != "down":
                print((self.vertical_border), end="")
            elif self.map_data[i][2] == True:
                print((self.opening_down), end="")
            else:
                print("         ", end="")
        print("")
    #Method to check the contents of a room when a player enters it, and run the appropriate interactions with it- if there's an enemy, a fight begins, if there's treasure, the treasure is generated and the player collects it, if it's a shop, the player enters the shop, if it's the exit room, the player is told and are able to exit the current level. Room contents such as enemies and treasure should be cleared from the room after the player interacts with them.
    def check_room(self):
        current_room = self.map_data[self.find_player()][1]
        if current_room == "enemy":
            enemy = Enemy(self.current_level)
            enemy.generate_enemy()
            enemy.fight()
            #If the player defeats the enemy, the enemy's loot is generated and given to the player.
            if enemy.battle == False and enemy.health <= 0:
                current_treasure = Treasure(self.current_level)
                current_treasure.enemy_drop()
            self.map_data[self.find_player()][1] = ""
        elif current_room == "treasure":
            current_treasure = Treasure(self.current_level)
            current_treasure.treasure_room()
            self.map_data[self.find_player()][1] = ""
        elif current_room == "exit":
            print(
                "\nYou found the exit room, you can now advance to the next level of the dungeon"
            )
        elif current_room == "shop":
            print(
                "As you step into the next room, you see a blacksmith working on some nice-looking weaponry, and an alchemist carefully arranging small coloured bottles.\nThe blacksmith greets you: 'Hey! If you're planning to step into the next room, there's a fearsome monster in there, you should buy some helpful items from us first!'"
            )
            has_left_shop = False
            #The player can continue choosing items to buy until they choose to leave the shop. They have a choice of buying health potions, sword upgrades or armour upgrades. If they run out of gold, or the shop runs out of stock, then they can't buy any more.
            while has_left_shop == False:
                player_choice = input(
                    "What would you like to buy?\nHealth Potions- {} in stock, 40 gold\nSword Upgrades- {} in stock, 100 gold\nArmour upgrades- {} in stock, 100 gold\nYou have {} gold\n~"
                    .format(self.shop_potions, self.sword_upgrades,
                            self.armour_upgrades, player.gold))
                player_choice = player_choice.lower()
                if player_choice == "health potions" or player_choice == "potions" or player_choice == "potion" or player_choice == "health":
                        #The player can choose to buy a certain amount of potions.
                        potions_amount = input("How many potions would you like to buy?\n~")
                        if potions_amount.isnumeric():
                            if self.shop_potions - potions_amount >= 0 and player.gold >= 40*potions_amount:
                                player.potions += 1*potions_amount
                                player.gold -= 40*potions_amount
                                self.shop_potions -= 1*potions_amount
                                print("You bought a potion! You now have", player.potions, "potions.")
                        else:
                            if player.gold < 40*potions_amount:
                                print("You don't have enough money to buy a potion")
                            elif self.shop_potions == 0:
                                print("Sorry, health potions are out of stock!")
                            else:
                                print("Sorry, there aren't enough health potions for you to buy that many!")
                #Sword upgrades increase the player's damage modifier by 0.5
                elif player_choice == "sword upgrades" or player_choice == "sword upgrade" or player_choice == "sword" or player_choice == "swords":
                    if self.sword_upgrades > 0 and player.gold >= 100:
                        player.sword_mod += 0.5
                        player.gold -= 100
                        self.sword_upgrades -= 1
                        print(
                            "You upgraded your sword! It now does more damage."
                        )
                    else:
                        if player.gold < 100:
                            print(
                                "You don't have enough money to buy an upgrade to your sword"
                            )
                        elif self.sword_upgrades == 0:
                            print(
                                "Sorry, I don't have enough materials to upgrade your sword further!"
                            )
                #Armour upgrades increase the player's health and maximum health by 2
                elif player_choice == "armour upgrades" or player_choice == "armour upgrade" or player_choice == "armour":
                    if self.armour_upgrades > 0 and player.gold >= 100:
                        player.max_health += 2
                        player.health += 2
                        player.gold -= 100
                        self.armour_upgrades -= 1
                        print(
                            "You upgraded your armour! You can now take more hits."
                        )
                    else:
                        if player.gold < 100:
                            print(
                                "You don't have enough money to buy an upgrade to your armour"
                            )
                        elif self.armour_upgrades == 0:
                            print(
                                "Sorry, I don't have enough materials to upgrade your armour further!"
                            )

                elif player_choice == "leave":
                    print(
                        "You left the shop, and ready your weapon as you stand before the giant doors."
                    )
                    has_left_shop = True

#Movement subroutine, allows player to move to a different room, and moves the player's location data accordingly

    def move(self):
        move = input("\nWhat direction do you want to move in?\n~")
        move = move.lower()
        #When the player moves right, their new position is stored in the store variable, and if they can go right, their current position in the array is set to 0, their new position in the array is set to 1, and the room is set as discovered.
        if move == "right" or move == "Right":
            store = self.find_player() + 1
            if store < len(self.map_data):
                self.map_data[self.find_player()][0] = 0
                self.map_data[store][0] = 1
                self.map_data[store][2] = True
                print("you move to the right room")
            else:
                print("There's a wall there")
        #The same procedure is used for moving left, except the the store variable subtracts 1 from the player's current position instead of adding one.
        elif move == "left" or move == "Left":
            store = self.find_player() - 1
            if store >= 0:
                self.map_data[self.find_player()][0] = 0
                self.map_data[store][0] = 1
                self.map_data[store][2] = True
                print("you move to the left room")
            else:
                print("There's a wall there")
        #When the player exits the level, they are awarded points, and change their current level to the next one. 30 points are awarded for reaching level 2, 50 for reaching level 3 and 70 for reaching level 4
        elif move == "exit":
            if self.map_data[self.find_player()][1] == "exit":
                print(
                    "You walk down the stairs leading to the next level of the dungeon"
                )
                if self.current_level == "1":
                    self.current_level = "2f1"
                    points = 30 * player.score_mod
                    player.score += points
                    print("You made it to the second floor, you get", points,
                          "points")
                elif self.current_level == "2f2":
                    self.current_level = "3f4"
                    points = 50 * player.score_mod
                    player.score += points
                    print("You made it to the third floor, you get", points,
                          "points")
                elif self.current_level == "3f1":
                    self.current_level = "4"
                    points = 70 * player.score_mod
                    player.score += points
                    print("You made it to the fourth floor, you get", points,
                          "points")
            else:
                print("this room isn't the exit room")

        elif move == "heal":
            #If the player has potions and missing health, they can heal on the map screen.
            if player.potions > 0 and player.health < player.max_health:
                print("You healed 1 health")
                player.health += 1
                player.potions -= 1
                print("You have", player.health, "health left")
                print("You have", player.potions, "healing potions left")
            else:
                if player.potions <= 0:
                    print("You have no healing potions left.")
                elif player.health == player.max_health:
                    print("You are already at maximum health.")
        #When there are multiple floors in a level, each floor is defined as a seperate object of the map class, so the current level attribute is changed for all objects of the current level when the player moves up or down. The same variable reassignments as moving left or right are also used after the current level has been changed.
        elif move == "up":
            if self.map_data[self.find_player()][4] == "up":
                print("you go up to the higher floor of this level")
                if self.current_level == "2f1":
                    map2f1.current_level = "2f2"
                    map2f2.current_level = "2f2"
                    store = self.find_player()
                    map2f1.map_data[store][0] = 0
                    map2f2.map_data[store][0] = 1
                    map2f2.map_data[store][2] = True
                elif self.current_level == "3f1":
                    map3f1.current_level = "3f2"
                    map3f2.current_level = "3f2"
                    map3f3.current_level = "3f2"
                    map3f4.current_level = "3f2"
                    store = self.find_player()
                    map3f1.map_data[store][0] = 0
                    map3f2.map_data[store][0] = 1
                    map3f2.map_data[store][2] = True
                elif self.current_level == "3f2":
                    map3f1.current_level = "3f3"
                    map3f2.current_level = "3f3"
                    map3f3.current_level = "3f3"
                    map3f4.current_level = "3f3"
                    store = self.find_player()
                    map3f2.map_data[store][0] = 0
                    map3f3.map_data[store][0] = 1
                    map3f3.map_data[store][2] = True
                elif self.current_level == "3f3":
                    map3f1.current_level = "3f4"
                    map3f2.current_level = "3f4"
                    map3f3.current_level = "3f4"
                    map3f4.current_level = "3f4"
                    store = self.find_player()
                    map3f3.map_data[store][0] = 0
                    map3f4.map_data[store][0] = 1
                    map3f4.map_data[store][2] = True

            else:
                print("there isn't an opening that goes up in this room")
        elif move == "down":
            if self.map_data[self.find_player()][4] == "down":
                print("you descend to the lower floor of this level")
                if self.current_level == "2f2":
                    map2f1.current_level = "2f1"
                    map2f2.current_level = "2f1"
                    store = self.find_player()
                    map2f2.map_data[store][0] = 0
                    map2f1.map_data[store][0] = 1
                    map2f1.map_data[store][2] = True
                elif self.current_level == "3f2":
                    map3f1.current_level = "3f1"
                    map3f2.current_level = "3f1"
                    map3f3.current_level = "3f1"
                    map3f4.current_level = "3f1"
                    store = self.find_player()
                    map3f2.map_data[store][0] = 0
                    map3f1.map_data[store][0] = 1
                    map3f1.map_data[store][2] = True
                elif self.current_level == "3f3":
                    map3f1.current_level = "3f2"
                    map3f2.current_level = "3f2"
                    map3f3.current_level = "3f2"
                    map3f4.current_level = "3f2"
                    store = self.find_player()
                    map3f3.map_data[store][0] = 0
                    map3f2.map_data[store][0] = 1
                    map3f2.map_data[store][2] = True
                elif self.current_level == "3f4":
                    map3f1.current_level = "3f3"
                    map3f2.current_level = "3f3"
                    map3f3.current_level = "3f3"
                    map3f4.current_level = "3f3"
                    store = self.find_player()
                    map3f4.map_data[store][0] = 0
                    map3f3.map_data[store][0] = 1
                    map3f3.map_data[store][2] = True

            else:
                print("there isn't an opening that goes down in this room")
        elif move == "status":
            player.print_stats()
        else:
            print(
                "That isn't a valid action, you can try to move left, right, up, or down. \nYou can also heal using your potions with 'heal' and check your inventory with 'status'"
            )


#Move used to need move_right and move_left subroutines, they're now incorporated in the move function

#     def move_right(self):
#         store = find_player(self.map_data)+1
#         if store < len(self.map_data):
#             self.map_data[find_player(self.map_data)][0] = 0
#             self.map_data[store][0] = 1
#             self.map_data[store][2] = True
#             print("you move to the right room")
#         else:
#             print("There's a wall there")
#
#     def move_left(self):
#         store = find_player(self.map_data)-1
#         if store >= 0:
#             self.map_data[find_player(self.map_data)][0] = 0
#             self.map_data[store][0] = 1
#             self.map_data[store][2] = True
#             print("you move to the left room")
#         else:
#             print("There's a wall there")

#Room class used to generate the middle layer of the visual map
class room:
    def __init__(self, Type, current_room_index, map_data):
        self.wall = "|"
        self.corridor = "==="
        self.Type = Type
        self.current_room_index = current_room_index
        self.map = map(map_data, True)
    #Rooms are printed based on their type, and whether they contain the player or an exit. The contents of the room will be a P if it has a player, an X if it's the exit, or blank if it's empty. The room's type decides what is placed beside the contents. If the type is left side, it will place a wall on the left, and a corridor on the right. If the type is right side, it will place a wall on the right, and a corridor on the left. If the type is corridor, it will place a corridor on both sides.
    def print_room(self):
        if self.Type == "left_side":
            if self.map.find_player() == self.current_room_index:
                print(self.wall, "P", self.corridor, end="")
            else:
                if self.map.map_data[self.current_room_index][1] == "exit":
                    print(self.wall, "X", self.corridor, end="")
                else:
                    print(self.wall, " ", self.corridor, end="")
        if self.Type == "corridor":
            if self.map.find_player() == self.current_room_index:
                print(self.corridor, "P", self.corridor, end="")
            else:
                if self.map.map_data[self.current_room_index][1] == "exit":
                    print(self.corridor, "X", self.corridor, end="")
                else:
                    print(self.corridor, " ", self.corridor, end="")
        if self.Type == "right_side":
            if self.map.find_player() == self.current_room_index:
                print(self.corridor, "P", self.wall, end="")
            else:
                if self.map.map_data[self.current_room_index][1] == "exit":
                    print(self.corridor, "X", self.wall, end="")
                else:
                    print(self.corridor, " ", self.wall, end="")


#the names of the map_data variables storing each floor have been shortened from 'map_floor4' to mapf4.
class map_generation:
    #Map floor variables are listed from top to bottom
    def __init__(self, map_data1, map_data2, map_data3, map_data4,
                 difficulty_level):
        self.mapf4 = map_data1
        self.mapf3 = map_data2
        self.mapf2 = map_data3
        self.mapf1 = map_data4
        self.has_gone_down = False
        self.difficulty = difficulty_level
    #Refer to 2.5 on the design document for the exact values of how many enemies and treasure rooms are generated for each level and difficulty. Once a level has reached the maximum limit of enemies (indicated by the placement counter), treasure rooms are placed instead until the placement counter reaches the maximum amount of events in the level, which sets fully_randomised as True, ending the loop.
    def generate_map2(self):
        fully_randomised = False
        placement_counter = 0
        while fully_randomised == False:
            #The event_placement variable randomly selects 1 of the 8 rooms in level 2, if the selected room already has something stored in it, the value is rerolled until an empty room is found.
            event_placement = random.randint(0, 7)
            #rooms 0-3 are the ones on the second floor, rooms 4-7 are the ones on the first floor
            if 0 <= event_placement <= 3:
                if self.mapf4[event_placement][1] == "":
                    if self.difficulty == "easy":
                        if placement_counter < 1:
                            self.mapf4[event_placement][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf4[event_placement][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 5:
                            fully_randomised = True
                    elif self.difficulty == "medium":
                        if placement_counter < 2:
                            self.mapf4[event_placement][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf4[event_placement][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 5:
                            fully_randomised = True
                    elif self.difficulty == "hard":
                        if placement_counter < 3:
                            self.mapf4[event_placement][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf4[event_placement][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 5:
                            fully_randomised = True

            elif 4 <= event_placement <= 7:
                if self.mapf3[event_placement - 4][1] == "":
                    if self.difficulty == "easy":
                        if placement_counter < 1:
                            self.mapf3[event_placement - 4][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf3[event_placement - 4][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 5:
                            fully_randomised = True
                    elif self.difficulty == "medium":
                        if placement_counter < 2:
                            self.mapf3[event_placement - 4][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf3[event_placement - 4][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 5:
                            fully_randomised = True
                    elif self.difficulty == "hard":
                        if placement_counter < 3:
                            self.mapf3[event_placement - 4][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf3[event_placement - 4][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 5:
                            fully_randomised = True

    def generate_map3(self):
        #For each pair of floors on map 3, a random room is picked to connect the two floors, providing the player with a new layout each playthrough.
        event_placement = random.randint(0, 3)
        self.mapf4[event_placement][4] = "down"
        self.mapf3[event_placement][4] = "up"
        self.has_gone_down = True

        self.has_gone_down = False
        #Connections between floors are only placed if connections don't already exist in that particular room to stop the existing connection being overwritten, locking the player out of re-entering the upper floor, and so a straight line to the exit isn't formed, making the player explore more of the level.
        while self.has_gone_down == False:
            event_placement = random.randint(0, 3)
            if self.mapf3[event_placement][4] == "":
                self.mapf3[event_placement][4] = "down"
                self.mapf2[event_placement][4] = "up"
                self.has_gone_down = True

        self.has_gone_down = False

        while self.has_gone_down == False:
            event_placement = random.randint(0, 3)
            if self.mapf2[event_placement][4] == "":
                self.mapf2[event_placement][4] = "down"
                self.mapf1[event_placement][4] = "up"
                self.has_gone_down = True
        #The same procedure is used to place the exit room.
        event_placement = random.randint(0, 3)
        self.mapf1[event_placement][1] = "exit"
        #The same event_placement algorithm for enemies and treasure rooms from level 2 applies for level 3, except it's scaled up for 4 floors instead of 2.
        fully_randomised = False
        placement_counter = 0
        while fully_randomised == False:
            event_placement = random.randint(1, 15)

            if 1 <= event_placement <= 3:
                if self.mapf4[event_placement][1] == "":
                    if self.difficulty == "easy":
                        if placement_counter < 4:
                            self.mapf4[event_placement][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf4[event_placement][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 11:
                            fully_randomised = True
                    elif self.difficulty == "medium":
                        if placement_counter < 5:
                            self.mapf4[event_placement][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf4[event_placement][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 12:
                            fully_randomised = True
                    elif self.difficulty == "hard":
                        if placement_counter < 6:
                            self.mapf4[event_placement][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf4[event_placement][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 13:
                            fully_randomised = True

            elif 4 <= event_placement <= 7:
                if self.mapf3[event_placement - 4][1] == "":
                    if self.difficulty == "easy":
                        if placement_counter < 4:
                            self.mapf3[event_placement - 4][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf3[event_placement - 4][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 11:
                            fully_randomised = True
                    elif self.difficulty == "medium":
                        if placement_counter < 5:
                            self.mapf3[event_placement - 4][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf3[event_placement - 4][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 12:
                            fully_randomised = True
                    elif self.difficulty == "hard":
                        if placement_counter < 6:
                            self.mapf3[event_placement - 4][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf3[event_placement - 4][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 13:
                            fully_randomised = True

            elif 8 <= event_placement <= 11:
                if self.mapf2[event_placement - 8][1] == "":
                    if self.difficulty == "easy":
                        if placement_counter < 4:
                            self.mapf2[event_placement - 8][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf2[event_placement - 8][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 11:
                            fully_randomised = True
                    elif self.difficulty == "medium":
                        if placement_counter < 5:
                            self.mapf2[event_placement - 8][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf2[event_placement - 8][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 12:
                            fully_randomised = True
                    elif self.difficulty == "hard":
                        if placement_counter < 6:
                            self.mapf2[event_placement - 8][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf2[event_placement - 8][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 13:
                            fully_randomised = True

            elif 12 <= event_placement <= 15:
                if self.mapf1[event_placement - 12][1] == "":
                    if self.difficulty == "easy":
                        if placement_counter < 4:
                            self.mapf1[event_placement - 12][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf1[event_placement - 12][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 11:
                            fully_randomised = True
                    elif self.difficulty == "medium":
                        if placement_counter < 5:
                            self.mapf1[event_placement - 12][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf1[event_placement - 12][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 12:
                            fully_randomised = True
                    elif self.difficulty == "hard":
                        if placement_counter < 6:
                            self.mapf1[event_placement - 12][1] = "enemy"
                            placement_counter = placement_counter + 1
                        else:
                            self.mapf1[event_placement - 12][1] = "treasure"
                            placement_counter = placement_counter + 1
                        if placement_counter == 13:
                            fully_randomised = True



def main():

    # level map is stored as a multidimensional array, the 1st dimension stores the rooms, the second stores player's
    # location in the 1st index, then the contents of the room at the second, whether or not the room has been
    # explored at the third, what shape of room it is at the fourth, and if the room has an opening up or down in the fifth.
    # Most fields are empty due to level generation taking place after the player has started the game.
    map1_data = [[1, "entrance", True, "left_side", ""],
                 [0, "enemy", False, "corridor", ""],
                 [0, "treasure", False, "corridor", ""],
                 [0, "exit", False, "right_side", ""]]

    map2_dataf2 = [[0, "exit", False, "left_side", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "corridor", "down"],
                   [0, "", False, "right_side", ""]]
    map2_dataf1 = [[1, "entrance", True, "left_side", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "corridor", "up"],
                   [0, "", False, "right_side", ""]]

    map3_dataf4 = [[1, "entrance", True, "left_side", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "right_side", ""]]
    map3_dataf3 = [[0, "", False, "left_side", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "right_side", ""]]
    map3_dataf2 = [[0, "", False, "left_side", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "right_side", ""]]
    map3_dataf1 = [[0, "", False, "left_side", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "corridor", ""],
                   [0, "", False, "right_side", ""]]

    map4_data = [[1, "entrance", True, "left_side", ""],
                 [0, "shop", False, "corridor", ""],
                 [0, "enemy", False, "right_side", ""]]
    #Main Program
    #Printing title screen
    title_screen = pyfiglet.figlet_format("Dungeon Delve")
    print(title_screen)
    main_menu = True
    difficulty_chosen = False
    #Main menu player input- Player can start game, view the leaderboard or see controls.
    while main_menu == True:
        menu_choice = input(
            "Please enter what you would like to do:\nstart game\nview leaderboard\ncontrols\n~"
        )
        menu_choice = menu_choice.lower()
        if menu_choice == "start game":
            #Before the game starts, the player must enter a name and choose a difficulty, after which the player object can be created and the game can begin.
            player_name = input("Please enter your name\n~")
            while len(player_name) > 80:
                player_name = input(
                    "That name is too long, please re-enter your name\n~")

            while difficulty_chosen == False:
                difficulty = input(
                    "What difficulty level would you like to play on?\nEasy\nMedium\nHard\n~"
                )
                difficulty = difficulty.lower()
                if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                    difficulty_chosen = True
                else:
                    print("That isn't a valid difficulty level")
            global player
            player = Player(player_name, difficulty)
            player.set_score_modifier()
            print("You enter the first level of the dungeon")
            main_menu = False

        elif menu_choice == "leaderboard" or menu_choice == "scoreboard" or menu_choice == "view leaderboard":
            #If a leaderboard file doesn't already exist, then first one is created. Then, the data is taken from the text file and is output, going back to the main menu afterwards.
            print("==| Leaderboard |==")
            file = open('scoreboard.txt', 'a+')
            file.close()
            file = open('scoreboard.txt', 'r')
            f = file.readlines()
            leaderboard = []
            for line in f:
                leaderboard.append(line.strip())
            for i in range(0, int(len(leaderboard)), 2):
                print(leaderboard[i], ": ", leaderboard[i + 1], sep="")
            file.close()
            print("==| End of Leaderboard |==")
    
        elif menu_choice == "controls":
            #When controls is chosen, a short tutorial is shown to the player to teach them how to interact with the game.
            print(
                "In the game, you will perform actions by entering commands into this:\n~"
            )
            input("Try it now!\n~")
            print("""Rooms look like this:
     ---                                
    |   ===                        
     --- 
    In the game the player will start in a room like this, your location is indicated with a 'p':
     ---                                
    | P ===                        
     ---
    As you can see, there's an opening to the right. When the map screen is showing with the prompt seen above you can move left, right, up and down by entering those into the prompt.
    When on the map screen you can also type in 'status' to see various information about yourself, such as your current health, gold or healing potions.
    You can also type 'heal' to use a healing potion and restore some of your health.
    When you find the exit room, the game will, mark it on the map with an 'X':
     ---      --- 
    | P ====== X |
     ---      --- 
     When you're in the exit room, you can type the command 'exit' to proceed to the next level of the game."""
                  )
            input("Press enter to continue.\n~")
            print(
                "In combat, you have the actions 'attack', 'defend' and 'heal' available to you.\nIf you successfully defended the previous turn, you also can 'flee' to try to run away from the battle if it's too difficult."
            )
            input(
                "That is everything you need to know to interact with the game! Press enter to return to the main menu\n~"
            )

        else:
            print("That isn't a valid choice")
    # As the player progresses through each level, first a map object is created for the current level, then the primary gameplay loop of printing the map, letting the player move, and checking the room that they've moved into. This is looped until they either exit the level, changing their current level, or the player dies in combat. Once the loop ends, if the player hasn't died, then the next map object is created, which continues the game until the end of level 4, where if they defeat the boss, they will end the game.
    map1 = map(map1_data, "1")
    while map1.current_level == "1" and player.death == False:
        print("Level 1")
        map1.print_map()
        map1.move()
        map1.check_room()
    if player.death == False:
        #Before the map object is created, a map_generation object is created to randomise the layouts and contents of a level.
        map2 = map_generation(map2_dataf2, map2_dataf1, 0, 0,
                              player.difficulty)
        map2.generate_map2()
        map2_dataf2, map2_dataf1 = map2.mapf4, map2.mapf3
        #On maps 2 and 3, each floor of the map is created as a different object.
        global map2f1
        global map2f2
        map2f1 = map(map2_dataf1, "2f1")
        map2f2 = map(map2_dataf2, "2f2")

        while map2f1.current_level == "2f1" or map2f2.current_level == "2f2":
            if player.death == False:
                if map2f1.current_level == "2f1":
                    print("Level 2, Floor 1")
                    map2f2.print_map()
                    map2f1.print_map()
                    map2f1.move()
                    if map2f1.current_level == "2f2":
                        map2f2.check_room()
                    elif map2f1.current_level == "2f1":
                        map2f1.check_room()
                if map2f1.current_level == "2f2":
                    print("Level 2, Floor 2")
                    map2f2.print_map()
                    map2f1.print_map()
                    map2f2.move()
                    if map2f1.current_level == "2f2":
                        map2f2.check_room()
                    elif map2f1.current_level == "2f1":
                        map2f1.check_room()
            elif player.death == True:
                map2f1.current_level, map2f2.current_level = False, False

    if player.death == False:
        map3 = map_generation(map3_dataf4, map3_dataf3, map3_dataf2,
                              map3_dataf1, player.difficulty)
        map3.generate_map3()
        map3_dataf4, map3_dataf3, map3_dataf2, map3_dataf1 = map3.mapf4, map3.mapf3, map3.mapf2, map3.mapf1

        global map3f1
        global map3f2
        global map3f3
        global map3f4
        map3f1 = map(map3_dataf1, "3f4")
        map3f2 = map(map3_dataf2, "3f4")
        map3f3 = map(map3_dataf3, "3f4")
        map3f4 = map(map3_dataf4, "3f4")

        while map3f1.current_level == "3f1" or map3f2.current_level == "3f2" or map3f3.current_level == "3f3" or map3f4.current_level == "3f4":
            if player.death == False:
                if map3f1.current_level == "3f1":
                    print("Level 3, Floor 1")
                    map3f4.print_map()
                    map3f3.print_map()
                    map3f2.print_map()
                    map3f1.print_map()
                    map3f1.move()
                    if map3f1.current_level == "3f2":
                        map3f2.check_room()
                    elif map3f1.current_level == "3f1":
                        map3f1.check_room()
                if map3f1.current_level == "3f2":
                    print("Level 3, Floor 2")
                    map3f4.print_map()
                    map3f3.print_map()
                    map3f2.print_map()
                    map3f1.print_map()
                    map3f2.move()
                    if map3f1.current_level == "3f3":
                        map3f3.check_room()
                    if map3f1.current_level == "3f2":
                        map3f2.check_room()
                    elif map3f1.current_level == "3f1":
                        map3f1.check_room()
                if map3f1.current_level == "3f3":
                    print("Level 3, Floor 3")
                    map3f4.print_map()
                    map3f3.print_map()
                    map3f2.print_map()
                    map3f1.print_map()
                    map3f3.move()
                    if map3f1.current_level == "3f4":
                        map3f4.check_room()
                    elif map3f1.current_level == "3f3":
                        map3f3.check_room()
                    elif map3f1.current_level == "3f2":
                        map3f2.check_room()
                if map3f1.current_level == "3f4":
                    print("Level 3, Floor 4")
                    map3f4.print_map()
                    map3f3.print_map()
                    map3f2.print_map()
                    map3f1.print_map()
                    map3f4.move()
                    if map3f1.current_level == "3f4":
                        map3f4.check_room()
                    elif map3f1.current_level == "3f3":
                        map3f3.check_room()
            else:
                map3f1.current_level, map3f2.current_level, map3f3.current_level, map3f4.current_level == False, False, False, False

    if player.death == False:
        map4 = map(map4_data, "4")
        has_finished_game = False
        while map4.current_level == "4" and player.death == False and has_finished_game == False:
            print("Level 4")
            map4.print_map()
            map4.move()
            map4.check_room()
            if map4.map_data[2][0] == 1:
                has_finished_game = True
    #Once the loop on level 4 has ended, and the player hasn't died, they have won the game, so their gold is converted into their score, and their stats are output.
    if player.death == False:
        player.score += player.gold * player.score_mod
        congratulations = pyfiglet.figlet_format("Congratulations")
        print(congratulations)
        time.sleep(5)
        print("You have beaten Dungeon Delve!\nYour score was", player.score,
              "\nYour score has been added to the leaderboard.")
        time.sleep(1)
        print("Health: ", player.health, "/", player.max_health, sep="")
        print("Name:", player.name)
        print("Gold:", player.gold)
        print("Potions:", player.potions)
        print("Sword upgrades: +", (player.sword_mod - 1) * 2, sep="")
    #Once the player's final score has been obtained, first the current leaderboard's data is entered into the program, then the player's score is sorted into the correct position with all of the data in the leaderboard. Once the player's name and score has been added and sorted to make the new leaderboard data, It rewrites the data in the file, and then prints the new leaderboard before the program ends.
    file = open('scoreboard.txt', 'a+')
    file.close()
    
    file = open('scoreboard.txt', 'r')
    f = file.readlines()
    scoreboard = []
    new_scoreboard = []
    for i in range(0, len(f)):
        entry = f[i]
        entry = entry[:-1]
        scoreboard.append(entry)
    score_on_leaderboard = False
    for i in range(1, int(len(scoreboard) / 2), 2):
        if player.score < int(scoreboard[i]):
            new_scoreboard.append(scoreboard[i - 1])
            new_scoreboard.append(scoreboard[i])
        elif player.score == int(scoreboard[i]):
            if score_on_leaderboard == False:
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])
                new_scoreboard.append(player.name)
                new_scoreboard.append(player.score)
                score_on_leaderboard = True
            else:
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])

        else:
            if score_on_leaderboard == False:
                new_scoreboard.append(player.name)
                new_scoreboard.append(player.score)
                score_on_leaderboard = True
            else:
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])

    file = open('scoreboard.txt', 'r')
    f = file.readlines()
    scoreboard = []
    new_scoreboard = []
    for line in f:
        scoreboard.append(line.strip())
    score_on_leaderboard = False
    scoreboard.append("placeholder")
    scoreboard.append("-1")
    for i in range(1, int(len(scoreboard)), 2):
        if player.score < int(scoreboard[i]):
            new_scoreboard.append(scoreboard[i - 1])
            new_scoreboard.append(scoreboard[i])
        elif player.score == int(scoreboard[i]):
            if score_on_leaderboard == False:
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])
                new_scoreboard.append(player.name)
                new_scoreboard.append(str(player.score))
                score_on_leaderboard = True
            else:
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])

        else:
            if score_on_leaderboard == False:
                new_scoreboard.append(player.name)
                new_scoreboard.append(str(player.score))
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])
                score_on_leaderboard = True
            else:
                new_scoreboard.append(scoreboard[i - 1])
                new_scoreboard.append(scoreboard[i])
    new_scoreboard.pop()
    new_scoreboard.pop()
    file.close()

    file = open("scoreboard.txt", "w")
    file.write("")
    file.close()

    file = open("scoreboard.txt", "a")
    for i in range(0, len(new_scoreboard)):
        file.write(str(new_scoreboard[i]) + "\n")
    file.close()

    print("==| Leaderboard |==")
    file = open('scoreboard.txt', 'r')
    f = file.readlines()
    leaderboard = []
    for line in f:
        leaderboard.append(line.strip())
    for i in range(0, int(len(leaderboard)), 2):
        print(leaderboard[i], ": ", leaderboard[i + 1], sep="")
    file.close()
    print("==| End of Leaderboard |==")


main()
