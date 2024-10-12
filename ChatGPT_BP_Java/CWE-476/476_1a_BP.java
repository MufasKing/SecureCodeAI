// Person.java
class Person {
    String name;
    int age;

    // Constructor to initialize the Person object
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display person details
    public void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

// MemoryManager.java
class MemoryManager {
    
    // Method to allocate memory for a Person object
    public Person allocatePerson(String name, int age) {
        return new Person(name, age); // Allocates memory and initializes the object
    }

    // Method to deallocate memory (in Java, just nullifying the reference)
    public void deallocatePerson(Person person) {
        person = null; // This marks the object for garbage collection
    }
}

public class Main {
    public static void main(String[] args) {
        MemoryManager memoryManager = new MemoryManager();

        // Allocate memory for a Person
        Person person = memoryManager.allocatePerson("John Doe", 30);
        person.display(); // Display person details

        // Deallocate memory (marking person for garbage collection)
        memoryManager.deallocatePerson(person);
        person = null; // Good practice to set the reference to null after deallocation
    }
}
