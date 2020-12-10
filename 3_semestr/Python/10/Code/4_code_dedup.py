import math
import random
import transliterate

def DistinctAndSortArray(someData):
    if type(someData) is not str:
        print("Переданный объект не имеет необходимый тип строки")
        return 0
    if ( not someData ):
        print("Никаких данных не было введено")
        return []
    listd = set(someData.split())
    varLus=sorted(listd, key=lambda x: transliterate.translit(x, 'ru'))
    return varLus


def PrintList(listd):
    if(len(listd) == 0):
        return
    print("\nНекоторые отсортированные и почищенные данные")
    for item in listd:
        print(f" {item} ", end="")
    print()


def PartTwo():
    while True:
        try:
            stri = input()
            if(RepresentsInt(stri) and int (stri)==0):
                break
            PrintList(DistinctAndSortArray(stri))
        except EOFError:
            break


def PartOne():
    PrintList(DistinctAndSortArray(PartOneInput()))


def PartOneInput():
    print("ВВедите некоторые данные. Для остановки ввода 0.")
    contents = ""
    while True:
        try:
            line = input()
            if(RepresentsInt(line) and int (line)==0):
                break
        except EOFError:
            break
        contents += f"{line} "
    return contents


def main():
    try:
        print("Задание 4")
        inputType = int(input(
            "Введите тип работы\n1.Считать все строки и потом поделить проблемов и вывести в отсортированном виде\n2.Каждый раз после переноса коретки сортировать\n=> "))
        tasks = {
            1: PartOne,
            2: PartTwo
        }
        if(inputType in tasks):
            tasks[inputType]()
        else:
            print("Задание не найдено")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
