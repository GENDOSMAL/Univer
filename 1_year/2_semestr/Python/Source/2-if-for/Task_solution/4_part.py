import traceback
import math


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
    d = math.fabs(float(input("Введите значение d => ")))
    c = math.fabs(float(input("Введите значение c => ")))
    Xexpeted = float(input("Введите x точки которую желаете проверить => "))
    Yexpeted = float(input("Введите y точки, которую желаете проверить => "))
    print("Введено значение с=[{0}] d=[{1}]".format(c, d))
    print("Введено точки для проверки вхождения [{0};{1}] ".format(
        Xexpeted, Yexpeted))
    if (Xexpeted >= d or Xexpeted <= -d) and Yexpeted == 0:
        print("Указанная точка [{0};{1}]  НАХОДИТСЯ на линии графика".format(
            Xexpeted, Yexpeted))
        return
    if Xexpeted == 0 and Yexpeted == -c:
        print("Указанная точка [{0};{1}]  НАХОДИТСЯ на линии графика".format(
            Xexpeted, Yexpeted))
        return
    ffNeg = c*Xexpeted+d*Yexpeted+d*c  # Для отрицательной стороны
    ffPol = c*Xexpeted-d*Yexpeted-d*c  # Для отрицательной стороны
    if(ffNeg == 0 or ffPol == 0):
        print("Указанная точка [{0};{1}]  НАХОДИТСЯ на линии графика".format(
            Xexpeted, Yexpeted))
    else:
        print("Указанная точка [{0};{1}]  НЕ находится на линии графика".format(
            Xexpeted, Yexpeted))


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
