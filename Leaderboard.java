//import java.io.File;
//import java.io.IOException
//import java.io.FileNotFoundException;
//import java.io.FileWriter;
//import java.util.Arrays;
//
//public class Leaderboard {
//    public void createLeaderboard() {
//        try {
//            File file = new File("leaderboard.txt");
//            if (file.createNewFile()) {
//                System.out.println("File created: " + file.getName());
//            } else {
//                System.out.println("Leaderboard already exists.");
//            }
//        } catch (IOException e) {
//            System.out.println("An error occurred. The leaderboard could not be created or accessed.");
//        }
//    }
//    public void printLeaderboard() {
//        try {
//            File file = new File("leaderboard.txt");
//            Scanner readFile = new Scanner(file);
//            while (readFile.hasNextLine()) {
//                boardData = ArrayUtils.add(boardData, readFile.nextLine());
//            }
//            file.close();
//        } catch (FileNotFoundException e) {
//            System.out.println("An error occurred. The leaderboard could not be created or accessed.");
//        }
//    }
//}