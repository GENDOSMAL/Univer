using System;

using MathNet.Numerics.LinearAlgebra;


namespace MatimProgram
{
    public static class Support
    {
        public static void PrintToConsole(this Matrix<double> array)
        {
            array.PrintToConsole(3);
        }

        public static void PrintToConsole(this Matrix<double> array, int countOf)
        {
            Console.WriteLine(array.ToString(array.RowCount, array.ColumnCount, $"f{countOf}").Replace(array.ToTypeString(), ""));
        }

        public static Matrix<double> GetEmptyMatrix(int rowCount, int columnCount)
        {
            return Matrix<double>.Build.Dense(rowCount, columnCount);
        }

        public static Matrix<double> CopyToNew(this Matrix<double> array)
        {
            var res = Matrix<double>.Build.Dense(array.RowCount, array.ColumnCount);
            array.CopyTo(res);

            return res;
        }

        public static void PrintArray(this int[] array)
        {
            Console.Write("[");
            foreach (var t in array)
            {
                Console.Write($"{t} ");
            }
            Console.Write($"]{Environment.NewLine}");
        }

        public static void PrintArray(this double[] array)
        {
            Console.Write("[");
            foreach (var t in array)
            {
                Console.Write($"{t} ");
            }
            Console.Write($"]{Environment.NewLine}");
        }
    }
}