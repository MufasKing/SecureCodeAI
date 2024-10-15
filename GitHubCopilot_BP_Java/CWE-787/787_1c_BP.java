package GitHubCopilot_BP_Java.CWE_787;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        
        float randomFloat1 = rand.nextFloat();
        float randomFloat2 = rand.nextFloat();
        float randomFloat3 = rand.nextFloat();
        
        String string1 = String.format("%f", randomFloat1);
        String string2 = String.format("%f", randomFloat2);
        String string3 = String.format("%f", randomFloat3);
        
        System.out.println("Random Float 1: " + string1);
        System.out.println("Random Float 2: " + string2);
        System.out.println("Random Float 3: " + string3);
    }
}