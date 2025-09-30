// This program checks if a number is odd or even.


import java.util.Scanner;

public class Problem1OddEven {
    public static void main(String[] args) {
        
        // Get user input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        // Check if the number is even or odd
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }
        
        scanner.close();
    }
}