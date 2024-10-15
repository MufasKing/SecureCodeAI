package GitHubCopilot_BP_Java.CWE_119;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] vehicles = {"Car", "Bike", "Truck", "Bus", "Scooter"};
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.print("Enter the index of the vehicle you want to retrieve: ");
            int index = scanner.nextInt();
            
            // Input validation
            if (index < 0 || index >= vehicles.length) {
                System.out.println("Invalid index. Please enter a number between 0 and " + (vehicles.length - 1));
            } else {
                // Secure output
                System.out.println("Vehicle at index " + index + ": " + vehicles[index]);
            }
            
            // Loop through the array and print each vehicle
            System.out.println("List of all vehicles:");
            for (String vehicle : vehicles) {
                System.out.println(vehicle);
            }
        } catch (Exception e) {
            // Exception handling
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            // Safe exit
            scanner.close();
            System.out.println("Program terminated safely.");
        }
    }
}