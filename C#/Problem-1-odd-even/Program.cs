// This program checks if a number is odd or even.

using System;

class Program
{
    static void Main()
    {
        // Get user input
        Console.WriteLine("Enter a number:");

        int number = Convert.ToInt32(Console.ReadLine());

        // Check if the number is even or odd

        if (number % 2 == 0)
        {
            Console.WriteLine("{0} is even.", number);
        }
        else
        {
            Console.WriteLine("{0} is odd.", number);
        }
    }
}
