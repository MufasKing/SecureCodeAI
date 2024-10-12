import java.lang.ref.WeakReference;

class Person {
    private String name;
    private int status;

    public Person(String name) {
        this.name = name;
        this.status = 0; // Initial status set to 0
    }

    public String getName() {
        return name;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "', status=" + status + "}";
    }
}

public class MemoryManagementExample {

    // Simulates memory allocation by creating a new Person object
    public static Person allocPerson(String name) {
        return new Person(name);
    }

    // Simulates memory deallocation by clearing the reference
    public static void deallocPerson(WeakReference<Person> personRef) {
        personRef.clear(); // Clear the reference, allowing garbage collection
    }

    public static void main(String[] args) {
        // Allocating memory for a new Person
        Person person = allocPerson("Alice");
        System.out.println(person);

        // Update status
        person.setStatus(1);
        System.out.println("Updated " + person);

        // Simulating memory deallocation using a WeakReference
        WeakReference<Person> weakPersonRef = new WeakReference<>(person);
        deallocPerson(weakPersonRef);

        // Attempting to retrieve the person after deallocation
        if (weakPersonRef.get() == null) {
            System.out.println("Person has been deallocated.");
        } else {
            System.out.println("Person still exists: " + weakPersonRef.get());
        }
    }
}
