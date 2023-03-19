using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            List<int> score_list = new List<int>();
            int total = 0, num = 0;
            Console.Write("score=");
            int a = Convert.ToInt32(Console.ReadLine());
            do
            {
                score_list.Add(a);
                total += a;
                num++;
                Console.Write("score=");
                a = Convert.ToInt32(Console.ReadLine());
            }
            while (a >= 0);
            int[] score = score_list.ToArray();
            Console.WriteLine("\n個數 = " + score.Length);
            Console.WriteLine("最大值 = " + score.Max());
            Console.WriteLine("最小值 = " + score.Min());
            Console.WriteLine("平均數 = " + Math.Round(score.Average(),2));
            Console.ReadLine();
        }
    }
}
