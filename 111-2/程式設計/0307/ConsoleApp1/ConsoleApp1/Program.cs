using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            double h, w;
            Console.Write("身高(公尺):");
            h = Convert.ToDouble(Console.ReadLine());
            Console.Write("體重(公斤):");
            w = Convert.ToDouble(Console.ReadLine());
            Console.Write("BMI:");
            Console.WriteLine(Math.Round(w/Math.Pow(h,2)));
        }
    }
}
