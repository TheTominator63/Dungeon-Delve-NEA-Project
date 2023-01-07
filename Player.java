public class Player {
    //Player Stats
    public static double maxHealth = 5;
    public static double health = 5;
    public static double swordMod = 1;
    public static int score = 0;
    public static int gold = 0;
    public static int potions = 0;
    public static boolean death = false;
    public static int scoreMod = 1;
    public static String difficulty;
    public static String name = "";
    //double scoreMod = 1;
    //Constructor for Stats that are input by the player

    static void printStats() {
        System.out.println("Health:" + Player.health + "/" + Player.maxHealth);
        System.out.println("Name:" + Player.name);
        System.out.println("Gold:" + Player.gold);
        System.out.println("Potions:" + Player.potions);
        System.out.println("Sword upgrades: +" + (Player.swordMod-1)*2);
        System.out.println("Score:" + Player.score);
    }

    static void displayHealth() {
        System.out.println("You have " + Player.health + "/" + Player.maxHealth + " left");
    }

    static void drinkPotion() {
        Player.health += 1;
        Player.potions -= 1;
        System.out.println("You healed 1 health");
    }
    
    //Sets score modifier based on difficulty
    public void setScoreModifier() {
        switch(Player.difficulty) {
            case "easy":
                Player.scoreMod = 1;
                break;
            case "medium":
                Player.scoreMod = 2;
                break;
            case "hard":
                Player.scoreMod = 3;
                break;
        }
    }
    //Method to output the player's stats
//    public void printStats() {
//        System.out.println("Health:" + Player.health + "/" + Player.maxHealth);
//        System.out.println("Name:" + name);
//        System.out.println("Gold:" + Player.gold);
//        System.out.println("Potions:" + Player.potions);
//        System.out.println("Sword upgrades: +" + (Player.swordMod-1)*2);
//        System.out.println("Score:" + Player.score);
//    }
    
    }