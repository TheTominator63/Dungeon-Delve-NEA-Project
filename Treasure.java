public class Treasure {
    String currentLevel;

    public Treasure(String currentStage) {
        currentLevel = currentStage;
    }

    public void addPoints(int pointBase) {
        int points = pointBase * Player.scoreMod;
        Player.score += points;
        System.out.println("You got " + points + " points");
    }
    
    public void treasureRoom() {
        if (currentLevel.equals("1")) {
            System.out.println("You got a health potion.");
            Player.potions += 1;
            
        } else if (currentLevel.equals("2f2") || currentLevel.equals("2f1")) {
            int chance = (int)(Math.random()*20 + 1);
            if (chance == 20) {
                System.out.println("You got a better weapon!");
                Player.swordMod += 0.5;
            } else if (chance == 19) {
                System.out.println("You found some better armour! You now have more health");
                Player.maxHealth += 2;
                Player.health += 2;
            } else if (12 <= chance && chance <= 18) {
                System.out.println("You got a health potion.");
                Player.potions += 1;
            } else {
                chance = (int)(Math.random()*26 + 25);
                Player.gold += chance;
                System.out.println("You got " + chance + " gold");
            } 
            
        } else {
            int chance = (int)(Math.random()*20 + 1);
            if (chance == 20) {
                System.out.println("You got a better weapon!");
                Player.swordMod += 0.5;
            } else if (chance == 19) {
                System.out.println("You found some better armour! You now have more health");
                Player.maxHealth += 2;
                Player.health += 2;
            } else if (12 <= chance && chance <= 18) {
                System.out.println("You got a health potion.");
                Player.potions += 1;
            } else {
                chance = (int)(Math.random()*26 + 50);
                Player.gold += chance;
                System.out.println("You got " + chance + " gold");
            }
        }
    }

    public void enemyDrop() {
        if (currentLevel.equals("1")) {
            addPoints(10);
        } else if (currentLevel.equals("2f2") || currentLevel.equals("2f1")) {
            int chance = (int)(Math.random()*10 + 1);
            if (chance == 10) {
                System.out.println("The enemy was carrying a spare health potion!");
                Player.potions += 1;
            } else if (chance == 1 || chance == 2) {
                System.out.println("The enemy wasn't carrying anything of value");
            } else {
                chance = (int)(Math.random()*16 + 10);
                Player.gold += chance;
                System.out.println("The enemy had " + chance + " gold");
            }
            addPoints(10);
        } else if (currentLevel.equals("4")) {
            addPoints(100);
        } else {
            int chance = (int)(Math.random()*10 + 1);
            if (chance == 10) {
                System.out.println("The enemy was carrying a spare health potion!");
                Player.potions += 1;
            } else if (chance == 1 || chance == 2) {
                System.out.println("The enemy wasn't carrying anything of value");
            } else {
                chance = (int)(Math.random()*21 + 15);
                Player.gold += chance;
                System.out.println("The enemy had " + chance + " gold");
            }
            addPoints(20);
        }
    }
}