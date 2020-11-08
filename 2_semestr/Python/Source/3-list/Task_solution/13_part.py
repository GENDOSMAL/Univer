import traceback

al = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def CheckValueAndReturnNormal(inputValue):
    global al
    if inputValue in al:
        return al.index(inputValue)+1
    else:
        aistr = al.join(",")
        raise Exception("Индекс не находится в массиве для работы для элемента [{0}].\n Обратитесь к разрабам чтобы его добавить если это знак препинания или иной символ который должен тут быть по заданию.\n В настоящий момент имеются следующие данные\n [{1}]".format(
            inputValue, aistr))


def mainEncryptSoulition(inputString, step):
    global al
    resultStr = ""
    for inpuInfo in inputString:
        oldIndexNormal = CheckValueAndReturnNormal(inpuInfo)
        newIndex = oldIndexNormal+step-1
        if newIndex > len(al):
            newIndex = newIndex-len(al)
        resultStr += al[newIndex]
    return resultStr


def mainDecryptSoulition(inputString, step):
    global al
    resultStr = ""
    for inpuInfo in inputString:
        oldIndexNormal = CheckValueAndReturnNormal(inpuInfo)
        newIndex = oldIndexNormal-step-1
        if newIndex > len(al):
            newIndex = newIndex-len(al)
        if newIndex < 0:
            newIndex = newIndex*-1
            newIndex = len(al)-1
        resultStr += al[newIndex]
    return resultStr


def checkStep(step):
    global al
    if not step.isdigit():
        raise Exception("Введенное значение не является числом", step)
    step = int(step)
    lenOfal = len(al)
    if step > lenOfal:
        print("Длина шага больше длины алфавита, поэтому просто передвигаем на определенное количество символов ", lenOfal, step)
        step=step%26
        print("Итоговый шаг ", step)
    return int(step)

def NormalAlpha(step,secretString):
    alpha = insert(remove(al, secretString),step)
    print(alpha)
    return alpha

def remove(alpha, string):
    for symbol in string:
        if symbol in alpha: 
            alpha.remove(symbol)
    for symbol in string:
        if symbol not in [chr(x) for x in range(65,91)] \
        or string.count(symbol) > 1: 
            string.remove(symbol) 
    return alpha, string

def insert(alpha_string,step):
    for index, symbol in enumerate(alpha_string[1]):
        alpha_string[0].insert((step+index), symbol)
    return alpha_string[0]

def main():
    try:
        print("Начало работы программы")
        
      
        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
