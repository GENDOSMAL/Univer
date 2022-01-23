using System;

namespace MatimProgram
{
    public static class Program
    {
        public static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Выполним задание 1");
                Task1.Make();
                //if (Console.ReadLine() == "1")
                //{
                //    Console.WriteLine("Выполним задание 1");
                //    Task1.Make();
                //}
                //else
                //{
                //    Console.WriteLine("Выполним задание 2");
                //    new Task2().Make();
                //}
            }
            catch (Exception e)
            {
                Console.WriteLine("Ошибка при работе программы");
                Console.WriteLine(e);
            }
        }
    }
}
