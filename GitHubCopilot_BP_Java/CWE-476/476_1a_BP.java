import java.nio.ByteBuffer;
import java.nio.ByteOrder;

class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class Main {
    public static void main(String[] args) {
        // Allocate memory for a Person object
        ByteBuffer buffer = ByteBuffer.allocateDirect(1024).order(ByteOrder.nativeOrder());

        // Initialize the Person object
        Person person = new Person("John Doe", 30);

        // Store the Person object in the allocated memory
        buffer.put(person.name.getBytes());
        buffer.putInt(person.age);

        // Access members of the Person object
        buffer.flip();
        byte[] nameBytes = new byte[person.name.length()];
        buffer.get(nameBytes);
        String name = new String(nameBytes);
        int age = buffer.getInt();

        System.out.println("Name: " + name);
        System.out.println("Age: " + age);

        // Deallocate memory (in Java, this is handled by the garbage collector)
        buffer.clear();
    }
}