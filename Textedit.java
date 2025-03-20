import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("> ");
        String text = scanner.nextLine();
    }
    public static void Save(String[] args) {
        System.out.println("Enter filepath: ");
        String path = scanner.nextLine();
        try (FileWriter writer = new FileWriter(path)) {
            writer.write(text);
        } catch (IOException e) {
            System.out.println("Try to save again.")
        }
    }
}