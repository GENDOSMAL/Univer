import traceback
import math
from decimal import Decimal


def SomeFunction(x):
    dd = (math.pow(x, 5)+math.pow(math.e, -2*math.fabs(x))) / \
        (math.pow(9-math.pow(x, 2), 1/4))
    dd2 = math.pow(math.tan(math.fabs(math.pow(math.cos(x), 2))), 3)
    y = (dd)*(dd2)
    print("При значении х [{0}] значение y [{1}]".format(x, y))


def FirstTask():
    typeOfWork = int(input("Введите тип работы \n1 - if\n2 - for\n: "))
    if typeOfWork == 1:
        x = float(input("Введите значение x: "))
        print("Работаем в промежутке: [1;2]")
        if not(x >= 1 and x <= 2):
            print("Ожидается что значение  будет в промежутке [1;2]")
            print("Конец работы программы")
            return
        SomeFunction(x)

    elif typeOfWork == 2:
        print("Работаем в промежутке: [1;2] c шагом 0,1 ")
        for i in range(10, 20, 1):
            SomeFunction(i/10)
    else:
        print("Ничего не выбрано")


def SecondTask():
    n = int(math.fabs(int(input("Введите значение n(точность) => "))))
    x = math.fabs(
        float(input("Введите значение x(число для нахождения косинуса) => ")))

    print("Введено значение x=[{0}] n=[{1}] ".format(x, n))
    cos = 1
    x = x * (math.pi / 180.0)
    for i in range(1, n*2, 1):
        mainInfo = (math.pow(x, i*2)/math.factorial(i*2))
        if math.pow(-1, i) == 1:
            cos += mainInfo
        else:
            cos -= mainInfo
    print("Итоговое значение при введенном [{0}] равно [{1}]".format(x, cos))


def Main():
    try:
        print("Начало работы программы")
        typeOfWork = int(
            input("Введите тип работы \n1 - Часть номер 1 \n2 - Часть номер 2 \n: "))
        if typeOfWork == 1:
            FirstTask()
        elif typeOfWork == 2:
            SecondTask()
        else:
            print("Ничего не выбрано")
        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    Main()
