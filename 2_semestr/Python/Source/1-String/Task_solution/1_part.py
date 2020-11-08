import traceback

al = " АБВГДЕЁЖЗИЙКЛМНОПРСТУФЧХЦШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхчцшщъыьэюя0123456789.,;?:!()-|\"«»\'"


def CheckValueAndReturnNormal(inputValue):
    if inputValue in al:
        return al.index(inputValue)+1
    else:
        aistr = al.join(",")
        raise Exception("Индекс не находится в массиве для работы для элемента [{0}].\n Обратитесь к разрабам чтобы его добавить если это знак препинания или иной символ который должен тут быть по заданию.\n В настоящий момент имеются следующие данные\n [{1}]".format(
            inputValue, aistr))


def mainEncryptSoulition(inputString, step):
    resultStr = ""
    for inpuInfo in inputString:
        oldIndexNormal = CheckValueAndReturnNormal(inpuInfo)
        newIndex = oldIndexNormal+step-1
        if newIndex > len(al):
            newIndex = newIndex-len(al)
        resultStr += al[newIndex]
    return resultStr


def mainDecryptSoulition(inputString, step):
    resultStr = ""
    for inpuInfo in inputString:
        oldIndexNormal = CheckValueAndReturnNormal(inpuInfo)
        newIndex = oldIndexNormal-step-1        
        if newIndex > len(al):
            newIndex = newIndex-len(al)            
        resultStr += al[newIndex]
    return resultStr


def checkStep(step):
    if not step.isdigit():
        raise Exception("Введенное значение не является числом", step)
    step = int(step)
    lenOfal = len(al)
    if step > lenOfal:
        print("Длина шага больше длины алфавита, поэтому просто передвигаем на определенное количество символов ", lenOfal, step)
        step=step%26
        print("Итоговый шаг ", step)
    return int(step)


def main():
    try:
        step = checkStep(
            input("Введите шаг (больше {0} не имеет смысла): ".format(len(al))))
        typeOfWork = input(
            "Тип работы:\nШифрование - 1\nДешифровка - 2 \nИ туда и сюда - 3\n")
        print("Шаг для работы {0}".format(step))
        if int(typeOfWork) == 1:
            print(mainEncryptSoulition(
                input("Введите данные для шифрования\n"), step))
        elif int(typeOfWork) == 2:
            print(mainDecryptSoulition(
                input("Введите данные для дешифрованния\n"), step))
        elif int(typeOfWork) == 3:
            encriptStr = mainEncryptSoulition(
                input("Введите данные для шифрования\n"), step)
            decrStr = mainDecryptSoulition(encriptStr, step)
            print("Зашифрованная строка\n{0}\nРасшифрованная строка\n{1}\n".format(
                encriptStr, decrStr))
        else:
            print("Ничего не выбрано")
        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
