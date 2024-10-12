import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

class Person {
    // Struct fields
    private String name;
    private int age;
    private int status;

    // Constructor to initialize the fields
    public Person(String name, int age, int status) {
        this.name = name;
        this.age = age;
        this.status = status;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public int getStatus() {
        return status;
    }

    // Method to represent memory allocation for Person
    public static Person allocate(String name, int age) {
        // Memory allocation simulation
        try {
            // Memory allocation
            ByteBuffer buffer = ByteBuffer.allocate(128); // Allocate memory
            
            // Set values
            Person person = new Person(name, age, 0); // Initialize status to 0

            // Simulating memory initialization (not needed in Java)
            // Here, we're just creating the object.

            // Return the new person object
            return person;

        } catch (Exception e) {
            System.err.println("Memory allocation failed: " + e.getMessage());
            return null; // Indicate failure
        }
    }

    // Resource cleanup method
    public void cleanup() {
        // In Java, cleanup usually isn't required as GC handles it
        System.out.println("Cleaning up resources for " + name);
        // Here, you could nullify or clean up if needed
    }

    public static void main(String[] args) {
        // Memory allocation for a Person object
        Person person = Person.allocate("John Doe", 30);
        
        if (person != null) {
            // Using the pointer equivalent (object reference)
            System.out.println("Name: " + person.getName());
            System.out.println("Age: " + person.getAge());
            System.out.println("Status: " + person.getStatus());

            // Resource management (cleanup)
            person.cleanup();
        } else {
            System.err.println("Failed to allocate memory for Person.");
        }
    }
}
