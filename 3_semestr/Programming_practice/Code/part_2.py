# Основное задание
# Задачи для второго задания Практикума по программированию. Общая тема задания «текстовый калькулятор».
# Базовая часть (выполняется всеми самостоятельно!):
# Написать калькулятор для строковых выражений вида '<число> <операция> <число>', где <число> - не отрицательное целое число меньшее 100, записанное словами, например "тридцать четыре",
# <арифметическая операция> - одна из операций "плюс", "минус", "умножить". Результат выполнения операции вернуть в виде текстового представления числа. Пример calc("двадцать пять плюс тринадцать")
# -> "тридцать восемь"
# Оформить калькулятор в виде функции, которая принимает на вход строку и возвращает строку.

# Доп задания

# Реализовать текстовый калькулятор для выражения из произвольного количества операций с учетом приоритета операций. Пример: calc("пять плюс два умножить на три минус один") -> "десять".
# (Для реализации рекомендуется использовать алгоритмы основанные на польской инверсной записи см. например, https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C )
# Сложность 3
# Расширение задания 3. Добавить поддержку приоритета операций с помощью скобок. Пример: calc("скобка открывается пять плюс два скобка закрывается умножить на три минус один") -> "двадцать".
# Сложность 3
# Добавить возможность использования отрицательных чисел. Пример: calc("пять минус минус один") -> "шесть".
# Сложность 1


# Для понимания где начинаются и заканчиваются скобки
dictBracket = {"открывается": "(", "закрывается": ")"}
# Некоторые знаки операций
operands = {"плюс": "+", "минус": "-", "умножить": "*"}
# Для преобразования из строки в число чисел от 0 до 9
digitSmallThenTen = {"ноль": 0, "один": 1, "два": 2, "три": 3,
                     "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9}
# Для преобразования странных и особенных чисел 11-19
digitThatVeryStrange = {"одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
                        "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19}
# Для круглых чисел  от 10 до 90
digitThatCanBeDivByTen = {"десять": 10, "двадцать": 20, "тридцать": 30, "сорок": 40,
                          "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90}
# словарь для обратного преобразования
digitForRevert = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
                  6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
                  11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
                  15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать",
                  19: "девятнадцать", 20: "двадцать",
                  30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят",
                  70: "семьдесят", 80: "восемьдесят", 90: "девяносто",
                  100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот",  600: "шестьсот",  700: "семьсот",  800: "восемьсот", 900: "девятьсот",
                  1000: "одна тысяча ", 2000: "две тысячи "}

# Операторы для некоторых действия при вычислении
operators = {"+": (1, lambda x, y: x + y),
             "-": (1, lambda x, y: x - y),
             "*": (2, lambda x, y: x * y)}


def GetDigitLikeStr(digit):  # Получить строку из числа результата
    if(digit == 0):
        return "ноль"
    res = ""
    if(digit < 0):
        res += "минус "
        digit = digit*-1
    res += IntToStr(digit)
    return res


def IntToStr(num):  # Метод помощник для получения строки, разделяет чило на части для постепенного их преобразования
    k = 1000
    m = k * 1000

    if (num < 20):
        return digitForRevert[num]

    if (num < 100):
        if num % 10 == 0:
            return digitForRevert[num]
        else:
            return digitForRevert[num // 10 * 10] + " " + digitForRevert[num % 10]

    if (num < k):
        if num % 100 == 0:
            return digitForRevert[(num//100)*100]
        else:
            return digitForRevert[(num//100)*100] + " " + IntToStr(num % 100)
    if (num < m):
        if num % k == 0:
            if((num // k) == 1):
                return digitForRevert[1000]
            elif((num // k) == 2):
                return digitForRevert[2000]
            else:
                return IntToStr(num // k) + " тысяч"
        else:
            if((num // k) == 1):
                return digitForRevert[1000] + IntToStr(num % k)
            elif((num // k) == 2):
                return digitForRevert[2000] + IntToStr(num % k)
            else:
                return IntToStr(num // k) + " тысяч " + IntToStr(num % k)


def Calc(inputStr):  # Основной метод для вычисления данных, приходит строка которая содержит в себе пример
    partsOfInput = OperateWithMinusImputValue(GetStringLikeoperands(inputStr))
    preaparedInStrFormula = "".join([str(integer) for integer in partsOfInput])
    print(f"В числовом представление было введено {preaparedInStrFormula}")
    resultOf = CalcPolishData(PrepareStackToCalc(ParseInputStr(partsOfInput)))
    return GetDigitLikeStr(resultOf)


def ParseInputStr(formulaInStr):  # Разбиение вхожнодной строки на операнды или скобки для дальнейшей передачи в другие методы которые с помощью алгоритма сортировочной станции и польской натации будет вычислять значение результат для введенного примера
    for s in formulaInStr:
        if(type(s) is int):
            yield s
            continue
        elif str(s) in operators or str(s) in "()":
            yield s
            continue
        else:
            print("Что-то пошло не совсем туда куда должно было")


def PrepareStackToCalc(parsedFormula):  # Некоторый алгоритм сортировочной станции
    localStack = []
    for token in parsedFormula:
        # Если элемент - оператор, то отправляем дальше все операторы из стека,
        # Чей приоритет больше или равен пришедшему,
        # До открывающей скобки или опустошения стека.
        # Здесь мы пользуемся тем, что все операторы право-ассоциативны
        if token in operators:
            while localStack and localStack[-1] != "(" and operators[token][0] <= operators[localStack[-1]][0]:
                yield localStack.pop()
            localStack.append(token)
        elif token == ")":
            # Если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
            # А открывающую скобку выкидываем из стека.
            while localStack:
                x = localStack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            # Если элемент - открывающая скобка, просто положим её в стек
            localStack.append(token)
        else:
            # Если элемент - число, отправим его сразу на выход
            yield token
    while localStack:
        yield localStack.pop()


def CalcPolishData(polishData):  # Подсчитать элементы в стеке
    stack = []
    for token in polishData:
        if token in operators:  # Если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # Забираем 2 числа из стека
            # Вычисляем оператор, возвращаем в стек
            stack.append(operators[token][1](x, y))
        else:
            stack.append(token)
    return stack[0]  # Результат вычисления - единственный элемент в стеке


# Из входной строки сделать лист из операторов и цифр
def GetStringLikeoperands(inputStr):
    operandinStr = inputStr.lower().strip().split()
    tempList = []

    isNeedBracketType = False

    openBracket = 0
    closeBracket = 0

    nextNumberOr = False
    isOperandLast = False
    for oper in operandinStr:
        oper = oper.strip()
        if oper == "скобка":
            isNeedBracketType = True
            nextNumberOr = False
            continue
        if isNeedBracketType:
            nextNumberOr = False
            if(oper in dictBracket):
                if(oper == "открывается"):
                    openBracket += 1
                elif (oper == "закрывается"):
                    closeBracket += 1
                tempList.append(dictBracket.get(oper))
                isNeedBracketType = False
            else:
                raise Exception(
                    f"Ожидалось описание скобки, было введено [{inputStr}]")

        if(oper in operands):
            nextNumberOr = False
            tempList.append(operands.get(oper))
            isOperandLast = True
            continue

        if(oper in digitSmallThenTen):
            if(nextNumberOr):
                tempList[-1] += digitSmallThenTen.get(oper)
                nextNumberOr = False
            else:
                tempList.append(digitSmallThenTen.get(oper))
            isOperandLast = False
            continue

        if(oper in digitThatVeryStrange):
            nextNumberOr = False
            tempList.append(digitThatVeryStrange.get(oper))
            isOperandLast = False
            continue

        if(oper in digitThatCanBeDivByTen):
            if(oper != "десять"):
                nextNumberOr = True
            tempList.append(digitThatCanBeDivByTen.get(oper))
            isOperandLast = False
            continue

    if(openBracket != closeBracket):
        raise Exception(
            f"Ожидалось одинкавое количество входных и выходных скобок всего открывающих [{openBracket}] всего закрывающих [{closeBracket}] [{inputStr}]")

    if(isOperandLast):
        raise Exception(
            f"Ожидалось что последний символ будет отличен от знаков операций [{inputStr}]")

    return tempList


# Некоторый костыль и проверка на то что нет слишком странных последовательностей операци
def OperateWithMinusImputValue(inputListOf):
    IndexItemsForDelete = []
    i = 0
    while i < len(inputListOf):
        if(i == 0):
            if(inputListOf[i] == "-"):
                if(type(inputListOf[i+1]) is not int):
                    raise Exception(
                        f"По условиям задачи, после знака отрицание должно быть число")
                inputListOf[i+1] = inputListOf[i+1]*-1
                i += 1
                IndexItemsForDelete.append(0)
                continue
            if(inputListOf[i] == "+"):
                IndexItemsForDelete.append(0)
                i += 1
                continue

        if(type(inputListOf[i]) is not int and inputListOf[i] in "-+*("):
            if(i+1 <= (len(inputListOf)-1) and i+2 <= (len(inputListOf)-1)):
                if(inputListOf[i+1] == "-" and type(inputListOf[i+2]) is int):
                    inputListOf[i+2] = inputListOf[i+2]*-1
                    IndexItemsForDelete.append(i+1)
                    i += 2
                    continue
                elif(type(inputListOf[i+1]) is not int and inputListOf[i+1] in "+*()"):
                    raise Exception(
                        f"2 знака операций не возможно быть помимо связки +- и --")
        i += 1

    if(len(IndexItemsForDelete) != 0):
        i = len(IndexItemsForDelete)-1
        while i > -1:
            del inputListOf[IndexItemsForDelete[i]]
            i -= 1
    return inputListOf


def main():  # Собственно главная первызванная часть
    try:
        print("Некоторые тесты")
        SomeTest()
        print("|ВНИМАНИЕ\n Слова должны отделяться проблемами и в случае проблем с расшифровкой будет выведена ошибка\n Проблемы могут быть связаны как с ошибками при вводе, \n так и проблема в логике программы\n Всего хорошего)) Очень люблю писать код ночью(нет)))\n Введите пример для решения:")
        while True:
            try:
                inputStr = input("\nДля выхода нажмите ентер\n=>")
                if not inputStr:
                    print(f"Выходим")
                    return
                print(Calc(inputStr))
            except Exception as e:
                print("Ошибка при работе программы ", str(e))
    except Exception:
        print("Ошибка при работе программы ", str(e))


def SomeTest():  # Некоторые тест чтобы точно ничего не сломалось при доработках
    testData = {"скобка открывается пять плюс восемь умножить на минус один скобка закрывается плюс четыре умножить на минус один": "минус семь",
                "пять минус минус один": "шесть",
                "скобка открывается пять плюс два скобка закрывается умножить на три минус один": "двадцать",
                "пять плюс два умножить на три минус один": "десять",
                "скобка открывается сорок пять плюс сорок пять скобка закрывается минус девяносто умножить на пять плюс десять минус одиннадцать": "минус триста шестьдесят один"}
    for testStr, res in testData.items():
        if(res != Calc(testStr)):
            raise Exception(f"Ответ не совадает с ожиданемым")


if __name__ == "__main__":  # Чтобы вызвался именно мой main метод а не другой
    main()
