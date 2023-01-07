import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Dungeon Delve!");
        boolean mainMenu = true;
        boolean difficultyChosen = false;
        String menuChoice;
        String playerName;
        int store;
        MapGeneration mapGen = new MapGeneration();
        //Leaderboard leaderboard = new Leaderboard();
        
        while (mainMenu == true){
            System.out.print("Please enter what you would like to do:\nstart game\nview leaderboard\ncontrols\n~");
            menuChoice = input.nextLine();
            menuChoice = menuChoice.toLowerCase();
            if (menuChoice.equals("controls")){
                System.out.println("Unfortunately, due to java's rules around multi-line strings, converting the tutorial would take far too long to do and I would gain no meaningful knowledge, please check out the python of version of Dungeon Delve for a tutorial!");
            //} else if (menuChoice.equals("leaderboard") || menuChoice.equals("view leaderboard")){
            //    Leaderboard leaderboard = new Leaderboard();
                
            } else if (menuChoice.equals("start game")){
                System.out.print("Please enter your name\n~");
                playerName = input.nextLine();
                while (playerName.length() > 80){
                    System.out.print("That name is too long, please re-enter your name\n");
                    playerName = input.nextLine();
                }
                while (difficultyChosen == false){
                    System.out.print("What difficulty level would you like to play on?\nEasy\nMedium\nHard\n~");
                    Player.difficulty = input.nextLine();
                    Player.difficulty = Player.difficulty.toLowerCase();
                    if (Player.difficulty.equals("easy") || Player.difficulty.equals("medium") || Player.difficulty.equals("hard")){
                        difficultyChosen = true;
                    } else {
                        System.out.println("That isn't a valid difficulty level");
                    }
                }
                Player player = new Player();
                player.setScoreModifier();
                System.out.println("You enter the first level of the dungeon");
                mainMenu = false;
            } else {
                System.out.println("That isn't a valid choice");
            }
        }

        Map map1 = new Map(Map.map1Data, Map.currentLevel);
        while (Map.currentLevel.equals("1") && Player.death == false){
            System.out.println("Level 1");
            map1.printMap();
            map1.move();
            map1.checkRoom();
        }
        if (Player.death == false){
            mapGen.generateMap2();
            Map map2f1 = new Map(Map.map2f1Data, Map.currentLevel);
            Map map2f2 = new Map(Map.map2f2Data, Map.currentLevel);
            while (Map.currentLevel.equals("2f1") || Map.currentLevel.equals("2f2")){
                if (Player.death == false){
                    if (Map.currentLevel == "2f1"){
                        store = map2f1.findPlayer();
                        System.out.println("Level 2, Floor 1");
                        map2f2.printMap();
                        map2f1.printMap();
                        map2f1.move();
                        if (Map.currentLevel.equals("2f2")){
                            map2f2.updateMapElement(store);
                            map2f2.checkRoom();
                        } else {
                            map2f1.checkRoom();
                        }
                    } else if (Map.currentLevel == "2f2"){
                        store = map2f2.findPlayer();
                        System.out.println("Level 2, Floor 2");
                        map2f2.printMap();
                        map2f1.printMap();
                        map2f2.move();
                        if (Map.currentLevel.equals("2f1")){
                            map2f2.updateMapElement(store);
                            map2f1.checkRoom();
                        } else {
                            map2f2.checkRoom();
                        }
                    }
                } else if (Player.death == true){
                    Map.currentLevel = "";
                }
            }
        }

        if (Player.death == false){
            mapGen.generateMap3();
            Map map3f1 = new Map(Map.map3f1Data, Map.currentLevel);
            Map map3f2 = new Map(Map.map3f2Data, Map.currentLevel);
            Map map3f3 = new Map(Map.map3f3Data, Map.currentLevel);
            Map map3f4 = new Map(Map.map3f4Data, Map.currentLevel);
            while (Map.currentLevel.equals("3f1") || Map.currentLevel.equals("3f2") || Map.currentLevel.equals("3f3") || Map.currentLevel.equals("3f4")){
                if (Player.death == false){
                    if (Map.currentLevel.equals("3f4")){
                        store = map3f4.findPlayer();
                        System.out.println("Level 3, Floor 4");
                        map3f4.printMap();
                        map3f3.printMap();
                        map3f2.printMap();
                        map3f1.printMap();
                        map3f4.move();
                        if (Map.currentLevel.equals("3f3")){
                            map3f3.updateMapElement(store);
                            map3f3.checkRoom();
                        } else {
                            map3f4.checkRoom();
                        }
                    } else if (Map.currentLevel.equals("3f3")){
                        store = map3f3.findPlayer();
                        System.out.println("Level 3, Floor 3");
                        map3f4.printMap();
                        map3f3.printMap();
                        map3f2.printMap();
                        map3f1.printMap();
                        map3f3.move();
                        if (Map.currentLevel.equals("3f2")){
                            map3f2.updateMapElement(store);
                            map3f2.checkRoom();
                        } else if (Map.currentLevel.equals("3f4")){
                            map3f4.updateMapElement(store);
                            map3f4.checkRoom();
                        } else {
                            map3f3.checkRoom();
                        }
                    } else if (Map.currentLevel.equals("3f2")){
                        store = map3f2.findPlayer();
                        System.out.println("Level 3, Floor 2");
                        map3f4.printMap();
                        map3f3.printMap();
                        map3f2.printMap();
                        map3f1.printMap();
                        map3f2.move();
                        if (Map.currentLevel.equals("3f1")){
                            map3f1.updateMapElement(store);
                            map3f1.checkRoom();
                        } else if (Map.currentLevel.equals("3f3")){
                            map3f3.updateMapElement(store);
                            map3f3.checkRoom();
                        } else {
                            map3f2.checkRoom();
                        }
                    } else if (Map.currentLevel.equals("3f1")){
                        store = map3f1.findPlayer();
                        System.out.println("Level 3, Floor 1");
                        map3f4.printMap();
                        map3f3.printMap();
                        map3f2.printMap();
                        map3f1.printMap();
                        map3f1.move();
                        if (Map.currentLevel.equals("3f2")){
                            map3f2.updateMapElement(store);
                            map3f2.checkRoom();
                        } else {
                            map3f1.checkRoom();
                        }
                    }
                } else{
                    Map.currentLevel = "";
                }
            }
        }

        if (Player.death == false){
            Map map4 = new Map(Map.map4Data, Map.currentLevel);
            boolean gameFinished = false;
            while (Map.currentLevel.equals("4") && gameFinished == false){
                System.out.println("Level 4");
                map4.printMap();
                map4.move();
                map4.checkRoom();
                if (map4.mapData[2][0].equals("@")){
                    gameFinished = true;
                }
            }
        }

        if (Player.death == false){
            Player.score += Player.gold * Player.scoreMod;
            System.out.println("Congratulations!\nYou have beaten Dungeon Delve!\nYour score was " + Player.score + ".");
            Player.printStats();
        } else {
            System.out.println("You Died");
            System.out.println("Your score was " + Player.score + ".");
        }
        //try {
            //leaderboard.createNewFile();
            
       //} catch (IOExeption e) {
           // System.out.println("An error occurred. The leaderboard could not be created or accessed.");
       //}
    }
}
