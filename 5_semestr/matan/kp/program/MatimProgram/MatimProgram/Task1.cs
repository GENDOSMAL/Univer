using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

using MathNet.Numerics.LinearAlgebra;

namespace MatimProgram
{
    public class Task1
    {
        public static void Make()
        {
            Console.WriteLine("Считываем исходную матрицу из файла!");
            var matrix = ReadSourceMatrix();
            Console.WriteLine("Матрица считана!");
            matrix.PrintToConsole();
            Console.WriteLine();
            Console.WriteLine("Задание 1.");
            Console.WriteLine("Возводим матрицу в степень 5");
            var matrixOfFirst = matrix.Power(5);
            Console.WriteLine($"Вероятность перехода [{matrixOfFirst[9, 5]}]");

            Console.WriteLine();
            Console.WriteLine("Задание 2.");
            var arraySupport = GetSupportMatrix();
            var res = arraySupport * matrixOfFirst;
            res.PrintToConsole(18);

            Console.WriteLine();
            Console.WriteLine("Задание 3.");
            Console.WriteLine($"Вероятность первого перехода за 6 шагов из состояния 6 в состояние 11 равно [{Task3(matrix, 6, 6, 11)}]");

            Console.WriteLine();
            Console.WriteLine("Задание 4.");
            Console.WriteLine($"Вероятность перехода из состояния 4 в состояние 7 не позднее чем за 8 равно [{Task4(matrix, 4, 7, 8)}]");

            Console.WriteLine();
            Console.WriteLine("Задание 5.");
            Console.WriteLine($"Среднее количество шагов для перехода из состояния 1 в состояние 10 [{Task5(matrix, 1, 10, 10000)}]");

            Console.WriteLine();
            Console.WriteLine("Задание 6.");
            Console.WriteLine($"Вероятность первого возвращения в состояние 3 за 7 шагов [{Task6(matrix, 3, 7)}]");

            Console.WriteLine();
            Console.WriteLine("Задание 7.");
            Console.WriteLine($"Вероятность возвращения в состояние 13 не позднее чем за 7 шагов [{Task7(matrix, 13, 7)}]");

            Console.WriteLine();
            Console.WriteLine("Задание 8.");
            Console.WriteLine($"Среднее время возвращение в состояние 11 [{Task8(matrix, 11)}]");


            Console.WriteLine();
            Console.WriteLine("Задание 9.");

            var eMatr = Matrix<double>.Build.DenseDiagonal(matrix.RowCount, 1);
          

            var matrM = matrix.Transpose() - eMatr;
        
            // ReSharper disable once InconsistentNaming
            var matrixM_ = matrM.CopyToNew();
            for (var i = 0; i < matrixM_.RowCount; i++)
            {
                for (var j = 0; j < matrixM_.ColumnCount; j++)
                {
                    if (i == matrix.RowCount - 1)
                    {
                        matrixM_[i, j] = 1;
                    }
                }
            }

            var bMatrix = Support.GetEmptyMatrix(matrix.RowCount, 1);
            bMatrix[matrix.RowCount - 1, 0] = 1;
            var inv = matrixM_.Inverse();
            var x = inv * bMatrix;

            var xNormal = new double[matrix.RowCount];

            for (var i = 0; i < x.RowCount; i++)
            {
                for (var j = 0; j < x.ColumnCount; j++)
                {
                    if (j == x.ColumnCount - 1)
                        xNormal[i] = x[i, j];
                }
            }
            xNormal.PrintArray();

            var result = xNormal.Sum();
            Console.WriteLine($"Сумма вероятностей [{result}] единица");

        }

        private static double Task8(Matrix<double> sourse, int desteny)
        {
            var buffer = new List<double>();
            for (var i = 1; i < 20; i++)
            {
                buffer.Add(i * Task6(sourse, desteny - 1, i));
            }

            return buffer.Sum();
        }

        private static double Task7(Matrix<double> sourse, int desteny, int n)
        {
            var buffer = new List<double>();
            for (var i = 1; i < n + 1; i++)
            {
                buffer.Add(Task6(sourse, desteny - 1, i));
            }

            return buffer.Sum();
        }

        private static double Task6(Matrix<double> sourse, int start, int n)
        {
            var resultM = Support.GetEmptyMatrix(sourse.RowCount, sourse.ColumnCount);
            for (var i = 1; i < n; i++)
            {
                resultM += Task6(sourse, start, i) * sourse.Power(n - i);
            }

            resultM = sourse.Power(n) - resultM;
            return resultM[start - 1, start - 1];
        }

        private static double Task5(Matrix<double> sourse, int start, int end, int iteration)
        {
            var resultMatr = sourse.CopyToNew();
            var result = resultMatr[start - 1, end - 1];

            for (var i = 2; i < iteration; i++)
            {
                resultMatr = Task3(sourse, resultMatr);
                result += (i * resultMatr[start - 1, end - 1]);
            }

            return result;
        }

        private static double Task4(Matrix<double> sourse, int start, int end, int n)
        {
            var previousM = sourse.CopyToNew();
            var resultM = sourse.CopyToNew();
            var tempMatr = sourse.CopyToNew();

            for (var i = 1; i < n; i++)
            {
                previousM = Task4(tempMatr, previousM);
                resultM += previousM;
            }

            return resultM[start - 1, end - 1];
        }

        private static Matrix<double> Task4(Matrix<double> curentM, Matrix<double> previosM)
        {
            var resMatrix = Matrix<double>.Build.Dense(curentM.RowCount, curentM.ColumnCount);

            for (var i = 0; i < curentM.RowCount; i++)
            {
                for (var j = 0; j < curentM.ColumnCount; j++)
                {
                    var bufList = new List<double>();
                    for (var m = 0; m < curentM.RowCount; m++)
                    {
                        if (m != j)
                        {
                            bufList.Add(curentM[i, m] * previosM[m, j]);
                        }
                    }
                    resMatrix[i, j] = bufList.Sum();
                }
            }
            return resMatrix;
        }

        private static double Task3(Matrix<double> sourse, int start, int end, int n)
        {
            var tempMatrix = sourse.CopyToNew();
            for (var i = 2; i < n + 1; i++)
            {
                tempMatrix = Task3(sourse, tempMatrix);
            }
            return tempMatrix[start - 1, end - 1];
        }

        private static Matrix<double> Task3(Matrix<double> sourse, Matrix<double> support)
        {
            var tempMatrix = Matrix<double>.Build.Dense(sourse.RowCount, sourse.ColumnCount);

            for (var i = 0; i < sourse.RowCount; i++)
            {
                for (var j = 0; j < sourse.ColumnCount; j++)
                {
                    var buffer = new List<double>();

                    for (var m = 0; m < sourse.RowCount; m++)
                    {
                        var buf = 0.0;
                        if (m != j)
                        {
                            buf = sourse[i, m] * support[m, j];
                        }
                        buffer.Add(buf);
                    }
                    tempMatrix[i, j] = buffer.Sum();
                }
            }

            return tempMatrix;
        }

        private static Matrix<double> ReadSourceMatrix()
        {
            var filePath = Path.Combine(Directory.GetCurrentDirectory(), "1taskData.txt");
            if (!File.Exists(filePath))
                throw new Exception($"Не удалось найти файл по пути [{filePath}]");

            var allLines = File.ReadAllLines(filePath);

            var length = int.Parse(allLines[0]);

            var resMatrix = Matrix<double>.Build.Dense(length, length);
            var index = 0;
            for (var i = 1; i < allLines.Length; i++)
            {

                var listOf = allLines[i].Split("\t").Select(double.Parse).ToArray();
                if (listOf.Length != length)
                    throw new Exception(
                        $"Не удалось распарсить данные из строки [{i + 1}] " +
                        $"количество распаршенных данных больше [{length}] и равно [{listOf.Length}]");
                for (var j = 0; j < length; j++)
                {
                    resMatrix[index, j] = listOf[j];
                }
                index++;
            }

            return resMatrix;
        }

        private static Matrix<double> GetSupportMatrix()
        {
            var res = Matrix<double>.Build.Dense(1, 14);
            res[0, 0] = double.Parse("0,02");
            res[0, 1] = double.Parse("0,12");
            res[0, 2] = double.Parse("0,03");
            res[0, 3] = double.Parse("0,013");
            res[0, 4] = double.Parse("0,01");
            res[0, 5] = double.Parse("0,07");
            res[0, 6] = double.Parse("0,15");
            res[0, 7] = double.Parse("0,03");
            res[0, 8] = double.Parse("0,04");
            res[0, 9] = double.Parse("0,04");
            res[0, 10] = double.Parse("0,01");
            res[0, 11] = double.Parse("0,08");
            res[0, 12] = double.Parse("0,16");
            res[0, 13] = double.Parse("0,02");
            return res;
        }
    }
}