import traceback
import math
import os.path
import os


def core(a, b, sqrtdesc):
    return (-b+sqrtdesc)/(2*a)


def Task1():
    pathToFile = input("Указжите путь до файла: ")
    if(not os.path.exists(pathToFile)):
        print("Указанный файл не существует")
        return
    with open(pathToFile) as f:
        lines = f.read().splitlines()
    ainfo = float(lines[0])
    binfo = float(lines[1])
    cinfo = float(lines[2])
    print(f"Ввдены следующие данные: a=[{ainfo}] b=[{binfo}] c=[{cinfo}]")
    desc = (binfo*binfo)-(4*ainfo*cinfo)
    print("Дескриминант ", desc)
    if(desc < 0):
        print("Корней нет")
        print("Конец работы программы")
        return
    sqrtdesc = math.sqrt(desc)
    print("Корень из него ", sqrtdesc)

    if(sqrtdesc == 0):
        print("Корень только 1 и равен он ", core(ainfo, binfo, sqrtdesc))
    else:
        print("Корень 1 равен ", core(ainfo, binfo, sqrtdesc))
        print("Корень 2 равен ", core(ainfo, binfo, -sqrtdesc))
    print("1")


def Task2():
    tasks = {
        1: Task2CreateFile,
        2: Task2RemoveFile,
        3: Task2Read,
        4: Task2WriteFile,
    }
    pathToFile=input("Введите путь до файла\n:")
    inputInfo=-1
    while inputInfo != 0:
        inputInfo = int(input("1. Добавление файла\n2. Удаление файла\n3. Чтение из файла\n4. Запись файла\n0. Выход\n: "))
        if inputInfo in tasks:
            tasks[inputInfo](pathToFile)
        elif inputInfo != 0:
            print("Нет введёного пункта меню")


def Task2CreateFile(pathToFile):
    print(f"Создаем файл по пути [{pathToFile}]")
    f = open(pathToFile, "w")
    f.close()


def Task2RemoveFile(pathToFile):
    print(F"Удаляем файл по пути [{pathToFile}]")
    os.remove(pathToFile)


def Task2Read(pathToFile):
    print(F"Считываем файл по пути [{pathToFile}]")
    try:
        with open(pathToFile, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Ошибка чтения файла. Файла не существует")


def Task2WriteFile(pathToFile):
    print(F"Записываем файл по пути [{pathToFile}]")
    user_info = input("Введите строку для записи\n: ")
    with open(pathToFile, "a") as f:
        f.write(f"{user_info}\n")

def Main():
    try:
        print("Начало работы программы")
        tasks = {
            1: Task1,
            2: Task2
        }
        inputInfo = int(input("Введите номер задания (1-2): "))
        if(inputInfo in tasks):
            tasks[inputInfo]()
        else:
            print("Введены не корректные данные: ")

        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    Main()
