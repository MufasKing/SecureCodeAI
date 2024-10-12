import java.util.Scanner;

class Person {
    private String name;
    private int age;
    private int status;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        this.status = 0; // Initialize status to 0
    }

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        } else {
            System.out.println("Error: Age cannot be negative.");
        }
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", status=" + status +
                '}';
    }
}

public class MemoryAllocationExample {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter name: ");
            String name = scanner.nextLine();

            System.out.print("Enter age: ");
            int age = Integer.parseInt(scanner.nextLine());

            // Memory allocation by creating a new Person object
            Person person = new Person(name, age);

            // Print the person details
            System.out.println("Person created: " + person);

            // Simulate memory deallocation
            person = null; // Allow garbage collection to reclaim memory

        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid age input. Please enter a valid integer.");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close(); // Close the scanner
        }
    }
}
