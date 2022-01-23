﻿using System;
using System.Collections.Generic;
using System.Linq;
using MathNet.Numerics.LinearAlgebra;

namespace MatimProgram
{
    public class Task2
    {
        private readonly double _l = 14.0;
        private readonly double _m = 3.0;
        private readonly double _u = 6.0;
        private readonly double _n = 13.0;
        
        private readonly int _mInt = 3;
        private readonly int _uInt = 6;
        private readonly int _nInt = 13;

        public void Make()
        {
            var matrixNew = Matrix<double>.Build.Dense(_mInt + _nInt + 1, _mInt + _nInt + 1);

            for (var i = 0; i < _mInt + _nInt; i++)
            {
                matrixNew[i, i + 1] = _l;
                if (i < _mInt)
                    matrixNew[i + 1, i] = (_uInt * (i + 1));
                else
                    matrixNew[i + 1, i] = _u * _m;
            }
            Console.WriteLine("Задание А.");
            Console.WriteLine("Матрица интенсивности переходов");
            matrixNew.PrintToConsole();
            
            var matrixSumm = new double[_mInt + _nInt + 1];

            for (var i = 0; i < matrixNew.RowCount; i++)
            {
                var sum = 0.0;
                for (var j = 0; j < matrixNew.ColumnCount; j++)
                {
                    sum += matrixNew[i, j];
                }
                matrixSumm[i] = sum;
            }
            
            var matrixD = Matrix<double>.Build.Dense(_mInt + _nInt + 1, _mInt + _nInt + 1);

            for (var i = 0; i < matrixD.RowCount; i++)
            {
                for (var j = 0; j < matrixD.ColumnCount; j++)
                {
                    if (i == j)
                    {
                        matrixD[i, j] = matrixSumm[i];
                    }
                }
            }

            var matrixM = matrixNew.Transpose() - matrixD;
            // ReSharper disable once InconsistentNaming
            var matrixM_ = matrixM.CopyToNew();
            for (var i = 0; i < matrixM_.RowCount; i++)
            {
                for (var j = 0; j < matrixM_.ColumnCount; j++)
                {
                    if (i == _mInt + _nInt)
                    {
                        matrixM_[i, j] = 1;
                    }
                }
            }
            
            var bMatrix = Matrix<double>.Build.Dense(_mInt + _nInt + 1, 1);
            bMatrix[bMatrix.RowCount - 1, 0] = 1;
            
            var inv = matrixM_.Inverse();
            var x = inv * bMatrix;

            var xNormal = new double[_mInt + _nInt + 1];

            for (var i = 0; i < x.RowCount; i++)
            {
                for (var j = 0; j < x.ColumnCount; j++)
                {
                    if (j == x.ColumnCount - 1)
                        xNormal[i] = x[i, j];
                }
            }
            xNormal.PrintArray();

            var res = xNormal.Sum();
            Console.WriteLine($"Сумма вероятностей [{res}] почти еденица, но списать можно на погрешность ибо числа слишком маленькие");
            Console.WriteLine();
            Console.WriteLine("Задание B.");
            Console.WriteLine($"Вероятность отказа от обслуживания [{xNormal[_nInt + _mInt]}]");
            Console.WriteLine();
            Console.WriteLine("Задание C.");
            Console.WriteLine($"Отсносительная пропускная способность [{1 - xNormal[_nInt + _mInt]}]");
            Console.WriteLine($"Абсолютная пропускная способность [{(1 - xNormal[_nInt + _mInt]) * _l}]");
            Console.WriteLine();
            Console.WriteLine("Задание D.");

            var resOfLength = new List<double>();

            for (var i = 1; i < _n + 1; i++)
            {
                resOfLength.Add(i * xNormal[_mInt + i]);
            }
            Console.WriteLine($"Средняя длина очереди [{resOfLength.Sum()}]");
            Console.WriteLine();
            Console.WriteLine("Задание E.");
            resOfLength = new List<double>();
            for (var i = 0; i < _nInt; i++)
            {
                resOfLength.Add((i + 1.0) / (_mInt * _uInt) * xNormal[_mInt + i]);
            }

            Console.WriteLine($"Среднее время в очереди [{resOfLength.Sum()}]");
            Console.WriteLine();
            Console.WriteLine("Задание F.");
            var resOfLeft = new List<double>();
            var resOfRight = new List<double>();
            for (var i = 0; i < _m + 1; i++)
            {
                resOfLeft.Add(i * xNormal[i]);
            }

            for (var i = _mInt + 1; i < _mInt + _nInt + 1; i++)
            {
                resOfRight.Add(_m * xNormal[i]);
            }

            Console.WriteLine($"Сумма левой части [{resOfLeft.Sum()}]");
            Console.WriteLine($"Сумма правой части [{resOfRight.Sum()}]");
            Console.WriteLine($"Среднее число занятых каналов [{resOfLeft.Sum() + resOfRight.Sum()}]");


            Console.WriteLine();
            Console.WriteLine("Задание G.");

            var resOf = new List<double>();
            for (var i = 0; i < _m; i++)
            {
                resOf.Add(xNormal[i]);
            }
            Console.WriteLine($"Вероятность того, что поступающая заявка не будет ждать в очереди [{resOf.Sum()}]");

            Console.WriteLine();
            Console.WriteLine("Задание H.");
            Console.WriteLine($"Среднее время простоя системы массового обслуживания [{1.0 / _l}]");
        }
    }
}