import java.util.Scanner;

class Person {
    int status;
    String name;

    // Constructor to initialize Person
    public Person(int status, String name) {
        this.status = status;
        this.name = name;
    }
}

public class MemoryAllocationExample {

    public static Person allocatePerson(int status, String name) {
        // Secure data handling: Ensure name is not null or empty
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be null or empty");
        }
        // Create a new Person object
        Person person = new Person(status, name);
        return person;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Memory allocation example
        try {
            // Input validation for status
            System.out.print("Enter the status (0 for inactive, 1 for active): ");
            int status = Integer.parseInt(scanner.nextLine());
            if (status < 0 || status > 1) {
                throw new IllegalArgumentException("Status must be 0 or 1");
            }

            // Input for name
            System.out.print("Enter the name: ");
            String name = scanner.nextLine();

            // Allocate memory for a new person and set status and name
            Person newPerson = allocatePerson(status, name);
            System.out.println("Person created: Name = " + newPerson.name + ", Status = " + newPerson.status);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input for status. Please enter a number.");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        } finally {
            scanner.close(); // Close the scanner to prevent resource leak
        }
    }
}
