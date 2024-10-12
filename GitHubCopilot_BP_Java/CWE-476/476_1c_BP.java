package GitHubCopilot_BP_Java.CWE-476;

public class Main {
    public static void main(String[] args) {
        try {
            // Allocate memory for a new person
            Person person = allocateMemory();
            System.out.println("Person status: " + person.status);

            // Perform some string handling
            String name = "John Doe";
            person.setName(name);
            System.out.println("Person name: " + person.getName());

            // Deallocate memory
            person = deallocateMemory(person);
            if (person == null) {
                System.out.println("Memory deallocated successfully.");
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to allocate memory for a new person
    public static Person allocateMemory() {
        Person person = new Person();
        person.status = 0;
        return person;
    }

    // Method to deallocate memory (nullify the reference)
    public static Person deallocateMemory(Person person) {
        person = null;
        return person;
    }
}

// Person class definition
class Person {
    int status;
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}