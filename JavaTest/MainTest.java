public class MainTest {
    public static void main(String[] args) {
        System.out.println("Running tests...");

        // Example test
        int expected = 4;
        int actual = 2 + 2;
        if (actual == expected) {
            System.out.println("Test passed!");
        } else {
            System.out.println("Test failed: expected " + expected + ", got " + actual);
        }
    }
}