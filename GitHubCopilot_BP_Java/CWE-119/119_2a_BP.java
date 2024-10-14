package GitHubCopilot_BP_Java.CWE-119;

import java.util.Scanner;

public class Main {
    private static String[] vehicles = {"Car", "Bike", "Truck", "Bus", "Scooter"};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the index of the vehicle: ");
        String input = scanner.nextLine();
        
        try {
            int index = Integer.parseInt(input);
            printVehicleAtIndex(index);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a valid integer.");
        }
    }

    private static void printVehicleAtIndex(int index) {
        if (index >= 0 && index < vehicles.length) {
            System.out.println("Vehicle at index " + index + ": " + vehicles[index]);
        } else {
            System.out.println("Index out of bounds. Please enter a valid index between 0 and " + (vehicles.length - 1) + ".");
        }
    }
}