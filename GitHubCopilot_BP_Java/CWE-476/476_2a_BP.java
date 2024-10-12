package GitHubCopilot_BP_Java.CWE-476;

// Define the Person class
class Person {
    public int status;

    // Constructor to initialize status
    public Person() {
        this.status = 0;
    }
}

public class Main {
    public static void main(String[] args) {
        // Allocate memory for a new Person object and handle exceptions
        Person person = null;
        try {
            person = new Person();
            // Memory allocation successful, status is initialized to 0
            System.out.println("Person status: " + person.status);
        } catch (Exception e) {
            System.err.println("Memory allocation failed: " + e.getMessage());
        } finally {
            // Memory cleanup if necessary (not typically needed in Java)
            person = null;
        }
    }
}