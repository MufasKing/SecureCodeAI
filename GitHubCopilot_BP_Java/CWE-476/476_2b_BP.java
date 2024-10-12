package GitHubCopilot_BP_Java.CWE-476;

public class Main {
    public static void main(String[] args) {
        Person person = allocateMemoryForPerson();
        System.out.println("Name: " + person.name + ", Status: " + person.status);
    }

    public static Person allocateMemoryForPerson() {
        Person person = new Person();
        person.status = 0;
        person.name = "John";
        return person;
    }
}

class Person {
    int status;
    String name;
}