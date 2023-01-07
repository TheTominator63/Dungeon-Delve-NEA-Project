public class MapGeneration {
    public boolean fullyRandomized = false;
    public int placementCounter = 0;
    public boolean hasGoneDown = false;
    int eventPlacement;
    
    public void generateMap2() {
        while (fullyRandomized == false) {
            eventPlacement = (int)(Math.random()*8);
            if (0 <= eventPlacement && eventPlacement <= 3){
                if (Map.map2f2Data[eventPlacement][1].equals("")){
                    switch (Player.difficulty) {
                        case "easy":
                            if (placementCounter < 1){
                                Map.map2f2Data[eventPlacement][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map2f2Data[eventPlacement][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 5) {
                                fullyRandomized = true;
                            }
                            break;
                        case "medium":
                            if (placementCounter < 2){
                                Map.map2f2Data[eventPlacement][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map2f2Data[eventPlacement][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 5) {
                                fullyRandomized = true;
                            }
                            break;
                        case "hard":
                            if (placementCounter < 3){
                                Map.map2f2Data[eventPlacement][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map2f2Data[eventPlacement][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 5) {
                                fullyRandomized = true;

                            }
                            break;
                    }
                }
            } else if (4 <= eventPlacement && eventPlacement <= 7){
                if (Map.map2f1Data[eventPlacement - 4][1].equals("")){
                    switch (Player.difficulty) {
                        case "easy":
                            if (placementCounter < 1){
                                Map.map2f1Data[eventPlacement - 4][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map2f1Data[eventPlacement - 4][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 5) {
                                fullyRandomized = true;
                            }
                            break;
                        case "medium":
                            if (placementCounter < 2){
                                Map.map2f1Data[eventPlacement - 4][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map2f1Data[eventPlacement - 4][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 5) {
                                fullyRandomized = true;
                            }
                            break;
                        case "hard":
                            if (placementCounter < 3){
                                Map.map2f1Data[eventPlacement - 4][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map2f1Data[eventPlacement - 4][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 5) {
                                fullyRandomized = true;
                            }
                            break;
                    }
                }
            }
        }
    }

    public void generateMap3(){
        eventPlacement = (int)(Math.random() * 4);
        Map.map3f4Data[eventPlacement][4] = "down";
        Map.map3f3Data[eventPlacement][4] = "up";

        while (hasGoneDown == false) {
            eventPlacement = (int)(Math.random() * 4);
            if (Map.map3f3Data[eventPlacement][4].equals("")){
                Map.map3f3Data[eventPlacement][4] = "down";
                Map.map3f2Data[eventPlacement][4] = "up";
                hasGoneDown = true;
            }
        }

        hasGoneDown = false;

        while (hasGoneDown == false) {
            eventPlacement = (int)(Math.random() * 4);
            if (Map.map3f2Data[eventPlacement][4].equals("")){
                Map.map3f2Data[eventPlacement][4] = "down";
                Map.map3f1Data[eventPlacement][4] = "up";
                hasGoneDown = true;
            }
        }

        eventPlacement = (int)(Math.random() * 4);
        Map.map3f1Data[eventPlacement][1] = "exit";

        fullyRandomized = false;
        placementCounter = 0;
        while (fullyRandomized == false) {
            eventPlacement = (int)(1 + Math.random() * 15);
            if (1 <= eventPlacement && eventPlacement <= 3){
                if (Map.map3f4Data[eventPlacement][1].equals("")){
                    switch (Player.difficulty) {
                        case "easy":
                            if (placementCounter < 4){
                                Map.map3f4Data[eventPlacement][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f4Data[eventPlacement][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 11) {
                                fullyRandomized = true;
                            }
                            break;
                        case "medium":
                            if (placementCounter < 5){
                                Map.map3f4Data[eventPlacement][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f4Data[eventPlacement][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 12) {
                                fullyRandomized = true;
                            }
                            break;
                        case "hard":
                            if (placementCounter < 6){
                                Map.map3f4Data[eventPlacement][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f4Data[eventPlacement][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 13) {
                                fullyRandomized = true;
                            }
                            break;

                    }
                }
            } else if (4 <= eventPlacement && eventPlacement <= 7){
                if (Map.map3f3Data[eventPlacement - 4][1].equals("")){
                    switch (Player.difficulty) {
                        case "easy":
                            if (placementCounter < 4){
                                Map.map3f3Data[eventPlacement - 4][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f3Data[eventPlacement - 4][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 11) {
                                fullyRandomized = true;
                            }
                            break;
                        case "medium":
                            if (placementCounter < 5){
                                Map.map3f3Data[eventPlacement - 4][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f3Data[eventPlacement - 4][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 12) {
                                fullyRandomized = true;
                            }
                            break;
                        case "hard":
                            if (placementCounter < 6){
                                Map.map3f3Data[eventPlacement - 4][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f3Data[eventPlacement - 4][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 13) {
                                fullyRandomized = true;
                            }
                            break;
                    }
                }
            } else if (8 <= eventPlacement && eventPlacement <= 11){
                if (Map.map3f2Data[eventPlacement - 8][1].equals("")){
                    switch (Player.difficulty) {
                        case "easy":
                            if (placementCounter < 4){
                                Map.map3f2Data[eventPlacement - 8][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f2Data[eventPlacement - 8][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 11) {
                                fullyRandomized = true;
                            }
                            break;
                        case "medium":
                            if (placementCounter < 5){
                                Map.map3f2Data[eventPlacement - 8][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f2Data[eventPlacement - 8][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 12) {
                                fullyRandomized = true;
                            }
                            break;
                        case "hard":
                            if (placementCounter < 6){
                                Map.map3f2Data[eventPlacement - 8][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f2Data[eventPlacement - 8][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 13) {
                                fullyRandomized = true;
                            }
                            break;
                    }
                }
            } else if (12 <= eventPlacement && eventPlacement <= 15){
                if (Map.map3f1Data[eventPlacement - 12][1].equals("")){
                    switch (Player.difficulty) {
                        case "easy":
                            if (placementCounter < 4){
                                Map.map3f1Data[eventPlacement - 12][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f1Data[eventPlacement - 12][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 11) {
                                fullyRandomized = true;
                            }
                            break;
                        case "medium":
                            if (placementCounter < 5){
                                Map.map3f1Data[eventPlacement - 12][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f1Data[eventPlacement - 12][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 12) {
                                fullyRandomized = true;
                            }
                            break;
                        case "hard":
                            if (placementCounter < 6){
                                Map.map3f1Data[eventPlacement - 12][1] = "enemy";
                                placementCounter += 1;
                            } else {
                                Map.map3f1Data[eventPlacement - 12][1] = "treasure";
                                placementCounter += 1;
                            }
                            if (placementCounter == 13) {
                                fullyRandomized = true;
                            }
                            break;
                    }
                }
            }
        }
    }
}
