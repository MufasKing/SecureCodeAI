package GitHubCopilot_BP_Java.CWE_125;

public class Main {

    public static void main(String[] args) {
        System.out.println(getValueAtIndex(5));  // Example usage
        System.out.println(getValueAtIndex(10)); // Example usage
    }

    public static int getValueAtIndex(int index) {
        int[] array = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        
        try {
            if (index >= 0 && index < array.length) {
                return array[index];
            } else {
                return -1;
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
            return -1;
        }
    }
}