package GitHubCopilot_BP_Java.CWE_476;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) {
        Main main = new Main();
        main.allocateAndCopy();
    }

    public void allocateAndCopy() {
        byte[] buf = new byte[1024];
        byte[] buf1 = new byte[1024];

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            System.out.println("Enter up to 100 characters for the first buffer:");
            String input1 = reader.readLine();
            if (input1.length() > 100) {
                System.out.println("Input exceeds 100 characters. Truncating to 100 characters.");
                input1 = input1.substring(0, 100);
            }
            System.arraycopy(input1.getBytes(), 0, buf, 0, input1.length());

            System.out.println("Enter up to 100 characters for the second buffer:");
            String input2 = reader.readLine();
            if (input2.length() > 100) {
                System.out.println("Input exceeds 100 characters. Truncating to 100 characters.");
                input2 = input2.substring(0, 100);
            }
            System.arraycopy(input2.getBytes(), 0, buf1, 0, input2.length());

        } catch (IOException e) {
            System.err.println("Error reading input: " + e.getMessage());
        }
    }
}