﻿using System;

using MathNet.Numerics.LinearAlgebra;

using NumSharp;

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

        public static void PrintNdArrayToConsole(this NDArray array)
        {
            Console.Write($"{Environment.NewLine}[");
            for (var i = 0; i < array.Shape[0]; i++)
            {

                if (array.shape.Length == 1)
                {
                    Console.Write(i == array.Shape[0] - 1
                        ? $"{double.Parse(array[i].ToString()):f5}"
                        : $"{double.Parse(array[i].ToString()):f5}   ");
                }
                else
                {
                    Console.Write("[");
                    for (var j = 0; j < array[i].Shape[0]; j++)
                    {
                        Console.Write(j == array[i].Shape[0] - 1
                            ? $"{double.Parse(array[i, j].ToString()):f5}"
                            : $"{double.Parse(array[i, j].ToString()):f5}   ");
                    }
                    Console.Write($"] {Environment.NewLine}");
                }

            }

            Console.Write($"] {Environment.NewLine}");
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