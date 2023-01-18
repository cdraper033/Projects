using System;

public class PythagTheoremCalc
{
    public static void Main(string[] args)
    {
        double a,
            b,
            c;
        Console.Write("Pythagorean Theorem Calculator");

        Console.Write("\nWhich side would you like to solve for? ");
        Console.Write("\n1-Side a \n2-Side b \n3-Side c");
        Console.Write("\nChoice: ");
        double choice = Convert.ToInt32(Console.ReadLine());
        // Say the user inputs 2 as their choice, Console.ReadLine() reads the input as a string
        // then it converts it to an integer which it then uses in the following if/else if statements below

        if (choice == 1) // If the choice is 1, then you will calculate the side of a
        {
            Console.Write("Side b: ");
            b = Convert.ToInt32(Console.ReadLine());
            double SquareB = b * b;

            Console.Write("Side c: ");
            c = Convert.ToInt32(Console.ReadLine());
            double SquareC = c * c;

            Console.Write("The length of side a is: {0} ", (double)(Math.Round(Math.Sqrt(SquareC - SquareB),2)));
        }
        else if (choice == 2)
        {
            Console.Write("Side a: ");
            a = Convert.ToInt32(Console.ReadLine());
            double SquareA = a * a;

            Console.Write("Side c: ");
            c = Convert.ToInt32(Console.ReadLine());
            double SquareC = c * c;

            Console.Write("The length of side b is: {0} ", (double)(Math.Round(Math.Sqrt(SquareC - SquareA),2)));
        }
        else if (choice == 3)
        {
            Console.Write("Side a: ");
            a = Convert.ToInt32(Console.ReadLine());
            double SquareA = a * a;

            Console.Write("Side b: ");
            b = Convert.ToInt32(Console.ReadLine());
            double SquareB = b * b;

            Console.Write("The length of side c is: {0} ", (double)(Math.Round(Math.Sqrt(SquareA + SquareB),2)));
        }
    }
}
