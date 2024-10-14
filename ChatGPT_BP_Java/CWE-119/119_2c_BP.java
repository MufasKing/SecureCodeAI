import java.util.Scanner;

public class VehicleManager {
    
    // Method to securely output the string (avoid leaking unnecessary sensitive data)
    private static void secureOutput(String message) {
        System.out.println("Output: " + message);
    }

    public static void main(String[] args) {
        // Array of vehicles
        String[] vehicles = {"Car", "Bike", "Truck", "Boat", "Scooter", "Bus"};
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Input validation
            int index = -1;
            while (true) {
                secureOutput("Please enter the index of the vehicle (0 to " + (vehicles.length - 1) + "): ");
                if (scanner.hasNextInt()) {
                    index = scanner.nextInt();
                    if (index >= 0 && index < vehicles.length) {
                        break;
                    } else {
                        secureOutput("Invalid input: Please enter a valid index between 0 and " + (vehicles.length - 1));
                    }
                } else {
                    secureOutput("Invalid input: Please enter a number.");
                    scanner.next(); // Clear the invalid input
                }
            }
            
            // Accessing the vehicle
            String selectedVehicle = vehicles[index];
            secureOutput("You selected: " + selectedVehicle);
            
            // Looping through the array and printing each vehicle
            secureOutput("List of all vehicles:");
            for (String vehicle : vehicles) {
                secureOutput(vehicle);
            }

        } catch (Exception e) {
            // Exception handling
            secureOutput("An error occurred: " + e.getMessage());
        } finally {
            // Safe exit and resource cleanup
            scanner.close();
            secureOutput("Program safely exited.");
        }
    }
}
