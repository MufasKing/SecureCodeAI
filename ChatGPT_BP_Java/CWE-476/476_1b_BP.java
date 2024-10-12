import java.util.ArrayList;
import java.util.List;

class Person {
    int status;

    // Constructor to initialize a person
    public Person() {
        this.status = 0; // Set status to 0
    }
}

public class MemoryManagementExample {
    private List<Person> persons; // List to store Person objects

    public MemoryManagementExample() {
        this.persons = new ArrayList<>();
    }

    // Method to allocate memory for a new Person
    public Person allocateMemory() {
        try {
            Person newPerson = new Person(); // Allocate memory
            persons.add(newPerson); // Keep reference to avoid garbage collection
            return newPerson; // Return reference to the allocated Person
        } catch (Exception e) {
            System.err.println("Error during memory allocation: " + e.getMessage());
            return null; // Return null if allocation fails
        }
    }

    // Method to deallocate memory (not needed in Java, but can be simulated)
    public void deallocateMemory(Person person) {
        if (person != null) {
            persons.remove(person); // Remove reference to allow garbage collection
        }
    }

    // Method to handle data safely
    public void handleData(Person person) {
        if (person == null) {
            System.err.println("Null Pointer Exception: Person reference is null.");
            return;
        }

        // Safely accessing the person's status
        System.out.println("Person status: " + person.status);
    }

    // Method to simulate secure coding practices
    public void securePracticeExample() {
        // Example of buffer overflow prevention (not applicable in Java directly)
        String userInput = "SafeInput"; // Simulating safe input
        if (userInput.length() > 100) {
            System.err.println("Input too long! Preventing buffer overflow.");
            return;
        }

        System.out.println("Processed safe input: " + userInput);
    }

    public static void main(String[] args) {
        MemoryManagementExample example = new MemoryManagementExample();

        // Allocating memory for a new Person
        Person person1 = example.allocateMemory();
        example.handleData(person1);

        // Deallocating memory
        example.deallocateMemory(person1);
        
        // Attempting to handle a null person
        example.handleData(null);

        // Secure coding practice example
        example.securePracticeExample();
    }
}
