import java.util.Scanner;

public class Enemy {
    String currentLevel;
    String enemyType;
    String enemyMod = "";
    double health;
    double attackMod;
    boolean battle = true;
    String[] elements = {"Fire", "Water", "Earth"};
    Scanner input = new Scanner(System.in);
    String playerElement;

    public Enemy(String currentStage) {
        currentLevel = currentStage;
    }

    
    
    public void generateEnemy() {
        if (currentLevel.equals("1")) {
            enemyType = "Goblin";
            health = 1.0;
            attackMod = 1.0;
        } else if (currentLevel.equals("2f2") || currentLevel.equals("2f1")) {
            enemyType = "Goblin";
            health = 2.0;
            attackMod = 1.0;
            int chance = (int)(Math.random()*3);
            enemyMod = elements[chance];
        } else if (currentLevel.equals("4")) {
            enemyType = "Ogre";
            switch(Player.difficulty) {
                case "easy":
                health = 8.0;
                attackMod = 1.5;   
                break;
            case "medium":
                health = 12.0;
                attackMod = 2.0; 
                break;
            case "hard":
                health = 16.0;
                attackMod = 2.0; 
                break;
            }
        } else {
            int chance = (int)(Math.random()*3 + 1);
            if (chance == 3) {
                enemyType = "Troll";
                health = 5.0;
                attackMod = 1.5;
            } else {
                enemyType = "Goblin";
                health = 2.0;
                attackMod = 1.0;
            }
            chance = (int)(Math.random()*3);
            enemyMod = elements[chance];
            }
        }

    public void fight() {
        String playerMove = "";
        String enemyMove = "";
        int turnCounter = 0;
        String previousPlayerMove;
        String previousEnemyMove;
        boolean optionSelected;
        boolean hasFleed = false;
        double playerDamage;
        double enemyDamage;
        double elementMod = 1;
        int enemyChance;
        int dialogue = (int)(Math.random()*4);
        String[] dialogueLines = {"jumps out of the shadows to attack you!",
            "was waiting in the room you just walked into, get ready for a fight!",
            "stands up and points its weapon at you, shouting a warcry!",
            "pushes you back as you stumble through the door, and tries to stab you!"};
        String[] moveList = {"attack", "defend", "boost"};
        
        if (currentLevel.equals("4")) {
            System.out.println("As you step through the large doorway, you hear loud snoring.\nYou tiptoe forward, trying not to wake it, but soon you hear a loud roar as a gigantic ogre lumbers forward.\nYou ready your sword one last time.");
        } else {
            System.out.println("A " + enemyMod + " " + enemyType + " " + dialogueLines[dialogue]);
        }
        //Player Element Selection
        if (enemyMod != "") {
            System.out.println("The monster is a " + enemyMod + " type, what do you want to imbue your sword with?\n~");
            while (true) {
                playerElement = input.nextLine();
                playerElement = playerElement.toLowerCase();
                if (playerElement.equals("fire") || playerElement.equals("water") || playerElement.equals("earth")) {
                    break;
                } else {
                    System.out.println("That's not a valid element. You can imbue your sword with fire, water or earth.");
                }
            }
            switch (playerElement) {
                case "fire":
                    switch (enemyMod) {
                        case "water":
                            elementMod = 0.5;
                            break;
                        case "earth":
                            elementMod = 1.5;
                            break;
                    }
                case "water":
                    switch (enemyMod) {
                        case "earth":
                            elementMod = 0.5;
                            break;
                        case "fire":
                            elementMod = 1.5;
                            break;
                    }
                case "earth":
                    switch (enemyMod) {
                        case "fire":
                            elementMod = 0.5;
                            break;
                        case "water":
                            elementMod = 1.5;
                            break;
                    }
            }
        }
        //Main Battle Loop
        while (battle == true) {
            optionSelected = false;
            turnCounter += 1;
            previousPlayerMove = playerMove;
            previousEnemyMove = enemyMove;
            System.out.println("Turn " + turnCounter);
            
            //The enemy will always attack after a boost, otherwise they will either attack, defend or boost.
            if (previousEnemyMove.equals("boost")) {
                enemyMove = "attack";
            } else {
                enemyChance = (int)(Math.random()*3);
                enemyMove = moveList[enemyChance];
            }
            if (turnCounter % 2 == 1) {
                System.out.println("The enemy is getting ready to " + enemyMove);
            } else {
                System.out.println("You can't tell what the enemy is about to do!");
            }
            //Much of the validation code is repeated to add the option to flee, I was rushing this part in the original code, if I had more time I would redesign this system to make it more modular
            while (optionSelected == false) {
                if (previousPlayerMove.equals("defend") && currentLevel != "4") {
                    System.out.print("Do you want to attack, defend, heal, or flee?\n~");
                    playerMove = input.nextLine();
                    playerMove = playerMove.toLowerCase();

                    if (playerMove.equals("status")) {
                        Player.printStats();
                    } else if (playerMove.equals("attack") || playerMove.equals("defend") || playerMove.equals("flee")) {
                        optionSelected = true;
                    } else if (playerMove.equals("heal")) {
                        if (Player.potions > 0 && Player.health < Player.maxHealth) {
                            optionSelected = true;
                        } else {
                            if (Player.potions <= 0) {
                                System.out.println("You have no healing potions left.");
                            } else if (Player.health == Player.maxHealth) {
                                System.out.println("You are already at maximum health.");
                            }
                        }
                    } else {
                        System.out.println("That isn't a valid action!");
                    }
                } else {
                    System.out.print("Do you want to attack, defend, or use a healing potion? (enter heal to do that)\n~");
                    playerMove = input.nextLine();
                    playerMove = playerMove.toLowerCase();

                    if (playerMove.equals("status")) {
                        Player.printStats();
                    } else if (playerMove.equals("attack") || playerMove.equals("defend")) {
                        optionSelected = true;
                    } else if (playerMove.equals("heal")) {
                        if (Player.potions > 0 && Player.health < Player.maxHealth) {
                            optionSelected = true;
                        } else {
                            if (Player.potions <= 0) {
                                System.out.println("You have no healing potions left.");
                            } else if (Player.health == Player.maxHealth) {
                                System.out.println("You are already at maximum health.");
                            }
                        }
                    } else if (playerMove.equals("flee")) {
                        if (currentLevel.equals("4")) {
                            System.out.println("There's no turning back now");
                        } else {
                            System.out.println("You need to sucessfully defend the previous turn if you want to try to flee");
                        }
                    } else {
                        System.out.println("That isn't a valid action!");
                    }
                }
            }
            //Damage Calculations
            playerDamage = 1 * elementMod * Player.swordMod;
            if (previousEnemyMove.equals("boost")){
                enemyDamage = (1 * attackMod) * 2;
            } else {
                enemyDamage = 1 * attackMod;
            }

            if (playerMove.equals("attack")) {
                if (enemyMove.equals("attack")) {
                    Player.health -= enemyDamage;
                    health -= playerDamage;
                    Player.displayHealth();
                    System.out.println("You both trade blows, each taking a sizeable amount of damage");
                } else if (enemyMove.equals("defend")) {
                    enemyChance = (int)(Math.random()*2 + 1);
                    if (enemyChance == 0) {
                        System.out.println("You try to get in a hit, but the enemy blocks your attack!");
                    } else {
                        System.out.println("You manage to attack them before they have a chance to block you!");
                        health -= playerDamage;
                    }
                } else if (enemyMove.equals("boost")) {
                    System.out.println("The enemy was too busy boosting their next attack to stop you from damaging them!");
                    health -= playerDamage;
                }
            } else if (playerMove.equals("defend")) {
                if (enemyMove.equals("attack")) {
                    System.out.println("You quickly raise your shield, and you take no damage since the enemy's weapon bounces off with a loud 'clang'!");
                } else if (enemyMove.equals("defend")) {
                    System.out.println("You both make defensive manoeuvres at each other, neither one of you successfully strike each other.");
                } else if (enemyMove.equals("boost")) {
                    System.out.println("You ready yourself to block their next attack, but the enemy seems to be trying to strengthen its next attack.");
                }
            } else if (playerMove.equals("heal")) {
                if (enemyMove.equals("attack")) {
                    System.out.println("You manage to quick chug down a healing potion, but the enemy still gets in a few hits while you were busy with that!");
                    Player.health -= enemyDamage;
                    Player.drinkPotion();
                    Player.displayHealth();
                } else if (enemyMove.equals("defend")) {
                    System.out.println("The enemy starts trying to block your attacks, so you take the chance to use a healing potion.");
                    Player.drinkPotion();
                    Player.displayHealth();
                } else if (enemyMove.equals("boost")) {
                    System.out.println("You drink a healing potion while the enemy starts to strengthen its next attack.");
                    Player.drinkPotion();
                    Player.displayHealth();
                }
            } else if (playerMove.equals("flee")) {
                enemyChance = (int)(Math.random()*2);
                if (enemyChance == 0) {
                    System.out.println("You try to run from the " + enemyType + ", but it catches up with you!");
                } else if (enemyChance == 1) {
                    System.out.println("You try to run from the " + enemyType + ", and manage to hide for long enough that it leaves the room");
                    battle = false;
                    hasFleed = true;
                }
            }

            if (Player.health <= 0) {
                System.out.println("You have run out of health\nY\nO\nU\n\nD\nI\nE\nD");
                battle = false;
                Player.death = true;
            } else if (health <= 0){
                System.out.println("You have defeated the enemy!");
                battle = false;
            }
        }
    }
}