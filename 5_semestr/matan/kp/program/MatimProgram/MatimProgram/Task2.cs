using System;
using System.Collections.Generic;
using System.Linq;

using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Double;

using NumSharp;

namespace MatimProgram
{
    public class Task2
    {
        private readonly double _l = 14.0;
        private readonly double _m = 3.0;
        private readonly double _u = 6.0;
        private readonly double _n = 13.0;

        private readonly int _lInt = 14;
        private readonly int _mInt = 3;
        private readonly int _uInt = 6;
        private readonly int _nInt = 13;
        
        public void Make()
        {
            var matrixIntensity = np.zeros(_mInt + _nInt + 1, _mInt + _nInt + 1);

            for (var i = 0; i < _mInt + _nInt; i++)
            {
                matrixIntensity[i, i + 1] = _l;
                if (i < _mInt)
                    matrixIntensity[i + 1, i] = (_uInt * (i + 1));
                else
                    matrixIntensity[i + 1, i] = _u * _m;
            }
            Console.WriteLine("Задание А.");
            Console.WriteLine("Матрица интенсивности переходов");
            matrixIntensity.PrintNdArrayToConsole();

            Console.WriteLine();
            Console.WriteLine("Задание B.");
            Console.WriteLine("Посчтитаем  диаганальную матрицу D");

            var matrixSumm = new int[_mInt + _nInt + 1];

            for (var i = 0; i < matrixIntensity.Shape[0]; i++)
            {
                var sum = 0;
                for (var j = 0; j < matrixIntensity[i].Shape[0]; j++)
                {
                    sum += int.Parse(matrixIntensity[i, j].ToString());
                }
                matrixSumm[i] = sum;
            }

            Console.WriteLine("Сумма строк матрицы интенсивности");
            matrixSumm.PrintArray();
            Console.WriteLine("Размещаем ее на диагонали");
            var matrixD = np.zeros(_mInt + _nInt + 1, _mInt + _nInt + 1);
            for (var i = 0; i < matrixD.Shape[0]; i++)
            {
                for (var j = 0; j < matrixD[i].Shape[0]; j++)
                {
                    if (i == j)
                    {
                        matrixD[i, j] = matrixSumm[i];
                    }
                }
            }

            matrixD.PrintNdArrayToConsole();

            var matrixM = matrixIntensity.T - matrixD;

            Console.WriteLine("Матрица М");
            matrixM.PrintNdArrayToConsole();
            // ReSharper disable once InconsistentNaming
            var matrixM_ = matrixM;
            for (var i = 0; i < matrixM_.Shape[0]; i++)
            {
                for (var j = 0; j < matrixM_[i].Shape[0]; j++)
                {
                    if (i == _mInt + _nInt)
                    {
                        matrixM_[i, j] = 1;
                    }
                }
            }
            Console.WriteLine("Матрица М_");
            matrixM_.PrintNdArrayToConsole();

            Console.WriteLine("Матрица B");
            var bMatrix = np.zeros(matrixM_.Shape[0]);
            bMatrix[matrixM_.Shape[0] - 1] = 1;
            bMatrix.PrintNdArrayToConsole();


            Console.WriteLine("Матрица X");
            var matr = MatrixToTemp(matrixM_);
            
            var inv = matr.Inverse();
            ConvertToNumpyMatrix(inv).PrintNdArrayToConsole();
            var x = ConvertToNumpyMatrix(inv) * bMatrix;

            var xNormal = new double[_mInt + _nInt + 1];

            for (var i = 0; i < x.Shape[0]; i++)
            {
                for (var j = 0; j < x[i].Shape[0]; j++)
                {
                    if (j == x[i].Shape[0] - 1)
                        xNormal[i] = x[i, j];
                }
            }
            xNormal.PrintArray();

            var res = xNormal.Sum();
            Console.WriteLine($"Сумма вероятностей [{res}] почти еденица, но списать можно на погрешность ибо числа слишком маленькие");
            Console.WriteLine();
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
                resOfRight.Add(_m*xNormal[i]);
            }

            Console.WriteLine($"Сумма левой части [{resOfLeft.Sum()}]");
            Console.WriteLine($"Сумма правой части [{resOfRight.Sum()}]");
            Console.WriteLine($"Среднее число занятых каналов [{resOfLeft.Sum()+ resOfRight.Sum()}]");


            Console.WriteLine();
            Console.WriteLine("Задание G.");

            var resOf = new List<double>();
            for (var i = 0; i < _m-1; i++)
            {
                resOf.Add(xNormal[i]);
            }
            Console.WriteLine($"Вероятность того, что поступающая заявка не будет ждать в очереди [{resOf.Sum()}]");

            Console.WriteLine();
            Console.WriteLine("Задание H.");
            Console.WriteLine($"Среднее время простоя системы массового обслуживания [{1.0/_l}]");
        }

        private DenseMatrix MatrixToTemp(NDArray array)
        {
            var res = new DenseMatrix(array.Shape[0], array.Shape[0]);
            for (var i = 0; i < array.Shape[0]; i++)
            {
                for (var j = 0; j < array[i].Shape[0]; j++)
                {
                    res[i, j] = array[i, j];
                }
            }

            return res;
        }

        private NDArray ConvertToNumpyMatrix(Matrix<double> matrix)
        {
            var res = np.zeros(matrix.RowCount, matrix.ColumnCount);

            for (var i = 0; i < matrix.RowCount; i++)
            {
                for (var j = 0; j < matrix.ColumnCount; j++)
                {
                    res[i, j] = matrix[i, j];
                }
            }

            return res;
        }
    }
}