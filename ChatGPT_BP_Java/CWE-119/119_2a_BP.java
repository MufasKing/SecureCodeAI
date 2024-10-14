import java.util.Scanner;

public class VehicleArray {

    // Array of vehicles
    private static String[] vehicles = {"Car", "Bike", "Truck", "Bus", "Van"};

    public static void main(String[] args) {
        int index = getInput(); // Get valid input from the user
        printVehicle(index);    // Print the vehicle at the provided index
    }

    // Method to get valid input from the user
    private static int getInput() {
        Scanner scanner = new Scanner(System.in);
        int index = -1; // Initial invalid index

        while (true) {
            try {
                System.out.print("Enter the index of the vehicle (0 to " + (vehicles.length - 1) + "): ");
                String input = scanner.nextLine();

                index = Integer.parseInt(input); // Convert input to an integer
                
                // Validate if index is within the array range
                if (index >= 0 && index < vehicles.length) {
                    break; // Exit loop if valid
                } else {
                    System.out.println("Error: Index out of range. Please enter a valid index.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid input. Please enter a number.");
            }
        }

        return index;
    }

    // Method to print the vehicle at the provided index
    private static void printVehicle(int index) {
        System.out.println("Vehicle at index " + index + ": " + vehicles[index]);
    }
}
