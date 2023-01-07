import java.util.Scanner;

public class Map {
    public static String currentLevel = "1";
    // level map is stored as a multidimensional array, the 1st dimension stores the rooms, the second stores player's
    // location in the 1st index, then the contents of the room at the second, whether or not the room has been
    // explored at the third, what shape of room it is at the fourth, and if the room has an opening up or down in the fifth.
    public static String[][] map1Data = {{"@", "entrance", "explored", "left_side", ""},
                                  {"",  "enemy", "", "corridor", ""},
                                  {"",  "treasure", "", "corridor", ""},
                                  {"",  "exit", "", "right_side", ""}};
    
    public static String[][] map2f2Data = {{"", "exit", "", "left_side", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "corridor", "down"},
                                  {"",  "", "", "right_side", ""}};
    public static String[][] map2f1Data = {{"@", "entrance", "explored", "left_side", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "corridor", "up"},
                                  {"",  "", "", "right_side", ""}};

    public static String[][] map3f4Data = {{"@", "entrance", "explored", "left_side", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "right_side", ""}};
    public static String[][] map3f3Data = {{"", "", "", "left_side", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "right_side", ""}};
    public static String[][] map3f2Data = {{"", "", "", "left_side", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "right_side", ""}};
    public static String[][] map3f1Data = {{"", "", "", "left_side", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "corridor", ""},
                                  {"",  "", "", "right_side", ""}};

    public static String[][] map4Data = {{"@", "entrance", "explored", "left_side", ""},
                                  {"",  "shop", "", "corridor", ""},
                                  {"",  "enemy", "", "right_side", ""}};
    
    String verticalBorder = " ---     ";
    String openingUp = " -↑-     ";
    String openingDown = " -↓-     ";
    String mapId;
    int shopPotions = 5;
    int swordUpgrades = 2;
    int armourUpgrades = 2;
    Scanner input = new Scanner(System.in);
    String[][] mapData;
    
    public Map( String[][] mapInput, String currentStage) {
        mapId = currentStage;
        mapData = mapInput;
    }

    //Todo: add this after map movement input in main when input = up or down
    public void updateMapElement(int index){
        if (Map.currentLevel.equals("2f1")){
            mapData[index][0] = Map.map2f1Data[index][0];
            mapData[index][2] = Map.map2f1Data[index][2];
        } else if (Map.currentLevel.equals("2f2")){
            mapData[index][0] = Map.map2f2Data[index][0];
            mapData[index][2] = Map.map2f2Data[index][2];     
        } else if (Map.currentLevel.equals("3f4")){
            mapData[index][0] = Map.map3f4Data[index][0];
            mapData[index][2] = Map.map3f4Data[index][2];     
        } else if (Map.currentLevel.equals("3f3")){
            mapData[index][0] = Map.map3f3Data[index][0];
            mapData[index][2] = Map.map3f3Data[index][2];     
        } else if (Map.currentLevel.equals("3f2")){
            mapData[index][0] = Map.map3f2Data[index][0];
            mapData[index][2] = Map.map3f2Data[index][2];     
        } else if (Map.currentLevel.equals("3f1")){
            mapData[index][0] = Map.map3f1Data[index][0];
            mapData[index][2] = Map.map3f1Data[index][2];     
        }
    }

    public int findPlayer() {
        int whereIsPlayer = 0;
        for (int i = 0; i < mapData.length; i++) {
            if (mapData[i][0].equals("@")) {
                whereIsPlayer = i;
            }
        }
        return whereIsPlayer;
    }
    
    class Room {
        String wall = "|";
        String corridor = "===";
        String type;
        int currentRoomIndex;
    
        public Room(String typeIn, int currentRoomNum) {
            type = typeIn;
            currentRoomIndex = currentRoomNum;
        }

        public String printRoom() {
            if (type.equals("left_side")){
                if (findPlayer() == currentRoomIndex) {
                    return(wall + " P " + corridor);
                } else {
                    if (mapData[currentRoomIndex][1].equals("exit")) {
                        return(wall + " X " + corridor);
                    } else {
                        return(wall + "   " + corridor);
                    }
                }
            } else if (type.equals("corridor")){
                if (findPlayer() == currentRoomIndex) {
                    return(corridor + " P " + corridor);
                } else {
                    if (mapData[currentRoomIndex][1].equals("exit")) {
                        return(corridor + " X " + corridor);
                    } else {
                        return(corridor + "   " + corridor);
                    }
                }
            } else if (type.equals("right_side")){
                if (findPlayer() == currentRoomIndex) {
                    return(corridor + " P " + wall);
                } else {
                    if (mapData[currentRoomIndex][1].equals("exit")) {
                        return(corridor + " X " + wall);
                    } else {
                        return(corridor + "   " + wall);
                    }
                }
            }
            return("");
        }
    }
    

    public void printMap() {
        for (int i = 0; i < mapData.length; i++) {
            if (mapData[i][2].equals("explored")) {
                if (mapData[i][4] != "up") {
                    System.out.print(verticalBorder);
                } else {
                    System.out.print(openingUp);
                }
            } else {
                System.out.print("         ");
            }
        }
        
        System.out.print("\n");

        for (int i = 0; i < mapData.length; i++) {
            Room currentRoom = new Room(mapData[i][3], i);
            if (mapData[i][2].equals("explored")) {
                System.out.print("" + currentRoom.printRoom());
            } else {
                System.out.print("        ");
            }
        }

        System.out.print("\n");

        for (int i = 0; i < mapData.length; i++) {
            if (mapData[i][2].equals("explored")) {
                if (mapData[i][4] != "down") {
                    System.out.print(verticalBorder);
                } else {
                    System.out.print(openingDown);
                }
            } else {
                System.out.print("         ");
            }
        }

        System.out.print("\n");
    }

    public void checkRoom() {
        String playerLocation = mapData[findPlayer()][1];
        if (playerLocation.equals("enemy")) {
            Enemy enemy = new Enemy(Map.currentLevel);
            enemy.generateEnemy();
            enemy.fight();

            if (enemy.battle == false) {
                if (enemy.health <= 0) {
                    Treasure currentTreasure = new Treasure(Map.currentLevel);
                    currentTreasure.enemyDrop();
                    mapData[findPlayer()][1] = "";
                } else {
                    mapData[findPlayer()][1] = "";
                }
            } //Exit Room
        } else if (playerLocation.equals("exit")) {
            System.out.println("\nYou found the exit room, you can now advance to the next level of the dungeon");
            //Shop
        } else if (playerLocation.equals("shop")) {
            System.out.println("As you step into the next room, you see a blacksmith working on some nice-looking weaponry, and an alchemist carefully arranging small coloured bottles.\nThe blacksmith greets you: 'Hey! If you're planning to step into the next room, there's a fearsome monster in there, you should buy some helpful items from us first!'");
            boolean hasLeftShop = false;
            String playerChoice;
            int potionsAmount;
            while (hasLeftShop == false){
                System.out.print("What would you like to buy?\nHealth Potions- " + shopPotions + " in stock, 40 gold\nSword Upgrades- " + swordUpgrades + " in stock, 100 gold\nArmour upgrades- " + armourUpgrades + " in stock, 100 gold\nYou have " + Player.gold + " gold\n~");
                playerChoice = input.nextLine();
                playerChoice = playerChoice.toLowerCase();
                if (playerChoice.equals("health potion") || playerChoice.equals("health potions") || playerChoice.equals("potion") || playerChoice.equals("potions")){
                    System.out.print("How many potions would you like to buy?\n~");
                    potionsAmount = input.nextInt();
                    if ((shopPotions - potionsAmount) >= 0 && Player.gold >= (40*potionsAmount)){
                        Player.potions += 1*potionsAmount;
                        Player.gold -= 40*potionsAmount;
                        shopPotions -= 1*potionsAmount;
                        System.out.println("You bought a potion! You now have " + Player.potions + " potions.");
                    } else {
                        if (Player.gold < 40*potionsAmount){
                            System.out.println("You don't have enough money to buy a potion");
                        } else if (shopPotions == 0){
                            System.out.println("Sorry, health potions are out of stock!");
                        } else {
                            System.out.println("Sorry, there aren't enough health potions for you to buy that many!");
                        }
                    }
                } else if (playerChoice.equals("sword") || playerChoice.equals("swords") || playerChoice.equals("sword upgrade") || playerChoice.equals("sword upgrades")){
                    if (swordUpgrades > 0 && Player.gold >= 100){
                        Player.swordMod += 0.5;
                        Player.gold -= 100;
                        swordUpgrades -= 1;
                        System.out.println("I upgraded your sword! It now does more damage.");
                    } else {
                        if (Player.gold < 100){
                            System.out.println("You don't have enough money to buy an upgrade to your sword.");
                        } else if (swordUpgrades == 0){
                            System.out.println("Sorry, I don't have enough materials to upgrade your sword further!");
                        }
                    }
                } else if (playerChoice.equals("armour") || playerChoice.equals("armour upgrade") || playerChoice.equals("armour upgrades")){
                    if (armourUpgrades > 0 && Player.gold >= 100){
                        Player.maxHealth += 2;
                        Player.health += 2;
                        Player.gold -= 100;
                        armourUpgrades -= 1;
                        System.out.println("I upgraded your armour! You can now take more hits.");
                    } else {
                        if (Player.gold < 100){
                            System.out.println("You don't have enough money to buy an upgrade to your armour.");
                        } else if (armourUpgrades == 0){
                            System.out.println("Sorry, I don't have enough materials to upgrade your armour further!");
                        }
                    }
                } else if (playerChoice.equals("leave")){
                    System.out.println("You left the shop, and ready your weapon as you stand before the giant doors.");
                    hasLeftShop = true;
                } else {
                    System.out.println("\"Sorry, I don't understand gibberish\"");
                }
            } 
            // Treasure Room
        } else if (playerLocation.equals("treasure")) {
            Treasure currentTreasure = new Treasure(Map.currentLevel);
            currentTreasure.treasureRoom();
            mapData[findPlayer()][1] = "";
        }
    }

    public void move() {
        int store;
        System.out.print("What would you like to do?\n~");
        String move = input.nextLine();
        move = move.toLowerCase();

        switch (move) {
            case "right":
                store = findPlayer() + 1;
                if (store < mapData.length) {
                    mapData[findPlayer()][0] = "";
                    mapData[store][0] = "@";
                    mapData[store][2] = "explored";
                    System.out.println("You move to the right room");
                } else {
                    System.out.println("There's a wall there");
                }
                break;
            case "left":
                store = findPlayer() - 1;
                if (store >= 0) {
                    mapData[findPlayer()][0] = "";
                    mapData[store][0] = "@";
                    mapData[store][2] = "explored";
                    System.out.println("You move to the left room");
                } else {
                    System.out.println("There's a wall there");
                }
                break;

            case "exit":
                if (mapData[findPlayer()][1].equals("exit")) {
                    System.out.println("You walk down the stairs leading to the next level of the dungeon");
                    int points;
                    switch (Map.currentLevel) {
                        case "1":
                            Map.currentLevel = "2f1";
                            points = 30 * Player.scoreMod;
                            Player.score += points;
                            System.out.println("You made it to the second floor, you get " + points + " points");
                            break;
                        case "2f2":
                            Map.currentLevel = "3f4";
                            points = 50 * Player.scoreMod;
                            Player.score += points;
                            System.out.println("You made it to the third floor, you get " + points + " points");
                            break;
                        case "3f1":
                            Map.currentLevel = "4";
                            points = 70 * Player.scoreMod;
                            Player.score += points;
                            System.out.println("You made it to the fourth floor, you get " + points + " points");
                            break;
                    }
                    break;
                } else {
                    System.out.println("This room isn't the exit room");
                }
                break;

            case "heal":
                if (Player.potions > 0 && Player.health < Player.maxHealth) {
                    Player.drinkPotion();
                    Player.displayHealth();
                } else {
                    if (Player.potions <= 0) {
                        System.out.println("You have no healing potions left");
                    } else if (Player.health == Player.maxHealth) {
                        System.out.println("You are already at maximum health");
                    }
                }
                break;

            case "up":
                if (mapData[findPlayer()][4].equals("up")){
                    System.out.println("You go up to a higher floor of this level");
                    if (Map.currentLevel.equals("2f1")){
                        Map.currentLevel = "2f2";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map2f2Data[store][0] = "@";
                        Map.map2f2Data[store][2] = "explored";
                    } else if (Map.currentLevel.equals("3f1")){
                        Map.currentLevel = "3f2";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map3f2Data[store][0] = "@";
                        Map.map3f2Data[store][2] = "explored";
                    } else if (Map.currentLevel.equals("3f2")){
                        Map.currentLevel = "3f3";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map3f3Data[store][0] = "@";
                        Map.map3f3Data[store][2] = "explored";
                    }  else if (Map.currentLevel.equals("3f3")){
                        Map.currentLevel = "3f4";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map3f4Data[store][0] = "@";
                        Map.map3f4Data[store][2] = "explored";
                    }
                } else {
                    System.out.println("There isn't an opening that goes up in this room");
                }
                break;
            case "down":
                if (mapData[findPlayer()][4].equals("down")){
                    System.out.println("You descend to a lower floor of this level");
                    if (Map.currentLevel.equals("2f2")){
                        Map.currentLevel = "2f1";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map2f1Data[store][0] = "@";
                        Map.map2f1Data[store][2] = "explored";
                    } else if (Map.currentLevel.equals("3f2")){
                        Map.currentLevel = "3f1";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map3f1Data[store][0] = "@";
                        Map.map3f1Data[store][2] = "explored";
                    } else if (Map.currentLevel.equals("3f3")){
                        Map.currentLevel = "3f2";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map3f2Data[store][0] = "@";
                        Map.map3f2Data[store][2] = "explored";
                    }  else if (Map.currentLevel.equals("3f4")){
                        Map.currentLevel = "3f3";
                        store = findPlayer();
                        mapData[store][0] = "";
                        Map.map3f3Data[store][0] = "@";
                        Map.map3f3Data[store][2] = "explored";
                    }
                } else {
                    System.out.println("There isn't an opening that goes down in this room");
                }
                break;
            
            case "status":
                Player.printStats();
                break;
            default:
                System.out.println("That isn't a valid action, you can try to move left, right, up, or down. \nYou can also heal using your potions with 'heal' and check your inventory with 'status'");
        }
    }
}
