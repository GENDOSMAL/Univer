import traceback
import random
from itertools import permutations


def InputSomeDataInt():
    try:
         return [int(x) for x in input("Введите список чисел через пробел ").split(" ")]
    except:
        print("Ошибка при работе программы ", traceback.format_exc())
        return


def TaskOne():
    inputInfo = InputSomeDataInt()
    result = []
    if(len(inputInfo) == 1):
        result = inputInfo
    else:
        result.append(inputInfo[1]+inputInfo[-1])
        for i in range(1, len(inputInfo) - 1):
            result.append(inputInfo[i - 1] + inputInfo[i + 1])
        result.append(inputInfo[-2] + inputInfo[0])
    print(' '.join([str(v) for v in result]))


def SecondTask():
    inputInfo = InputSomeDataInt()
    result = []
    for i in inputInfo:
        if i not in result:
            if inputInfo.count(i) > 1:
                result.append(i)
    print(' '.join([str(v) for v in result]))


def ThirdTask():
    n = int(input("Введите N "))
    m = int(input("Введите M "))
    h = int(input("Введите Н "))
    matrix = [[random.randrange(0, 10) for y in range(m)] for x in range(n)]
    print("Сгенерированная матрица ")
    for im in range(n):
        print(matrix[im])
    for col in range(m):
        inf = [row[col] for row in matrix]
        if(h in inf):
            print("В столбце {0} найдено число {1}.".format(col+1, h))


def FourthTask():
    inputInfo = InputSomeDataInt()
    if inputInfo == inputInfo[::-1]:
        print("Cписок является симметричным")
    else:
        print("Cписок является НЕ симметричным")


def FivedTask():
    inputInfo = InputSomeDataInt()
    perm = permutations(inputInfo, 2)
    for e in list(perm):
        buf_list = inputInfo[:]
        buf_list.remove(e[0])
        buf_list.remove(e[1])
        buf_list1 = buf_list[:]
        buf_list1.sort()
        if (buf_list1 == buf_list):
            print("Удалили элементы", e[0], "и", e[1], "\nПолучили:", buf_list)
            return        
    print("Условие выполнить не удалось")


def SixedTask():
    inputInfo = InputSomeDataInt()
    r = len(set([e for e in inputInfo]))
    print("Уникальных значений в списке:", r)


def SevenedTask():
    inputInfo = InputSomeDataInt()
    result = list(set([e for e in inputInfo]))
    print("Список без повторяющихся значений ",
          " ".join([str(v) for v in result]))


def EightedTask():
    bookList = input("Введеите список книг через точку с запятой: ").split(";")
    for i in range(len(bookList)):
        if bookList[i][0] == " ":
            bookList[i] = bookList[i][1:]
    bookList = sorted(bookList, key=str.lower)
    print("Введенный list:\n" + str(bookList))

    newBook = input("Ввведите название книг для добавления: ")

    bookList.append(newBook)
    bookList = sorted(bookList, key=str.lower)
    print("Итого list:\n" + str(bookList))


def NinedTask():
    try:
        n = int(input("Введит размер списка: "))
    except:
        print("Ошибка при работе программы ", traceback.format_exc())
        return
    someRange = [random.randint(-15, 15) for _ in range(n)]
    print(f"Получился следующий массив: [{someRange}]")
    print("Часть a: ")
    bufA=[]
    resultA=someRange
    for i in range(n):
        if(resultA[i]>0):
            bufA.append(resultA[i])
    print(bufA)
    bufA.sort()
    print(bufA)
    index=0
    for i in range(n):
        if(resultA[i]>0):
            resultA[i]=bufA[index]
            index+=1
    print(resultA)

    print("Часть b: ")
    bufb=[]
    resultb=someRange
    for i in range(n):
        if(i%2==0):
            bufb.append(resultb[i])
    bufb.sort()
    index=0
    for i in range(n):
        if(i%2==0):
            resultb[i]=bufb[index]
            index+=1
    print(resultb)

def TenedTask():
    print("Введите список 1")
    in1=InputSomeDataInt()
    print("Введите список 2")
    in2=InputSomeDataInt()
    print(f"Введены следующие списки\n{in1}\n{in2}\n")
    if(in1==in2):
        print("Списки совпадают")
    else:
        print("Списки НЕ совпадают")

def ElevenedTask():
    s=InputSomeDataInt()
    counter = -1
    outputList = [s[0]]
    for el in s:
        counter += 1
        if counter == 0:
            pass
        else:
            outputList.append(el)
            for elAfter in outputList[:counter]:
                outputList.append(elAfter)
                counter += 1
    print(f"Результат работы \n{outputList}")

def TwelwedTask():
    inputInfo = list(input("Введите строку для замены (через пробел) 'itmathrepetitor' на 'silence': ").split(" "))
    print(f"Введены следующие данные:\n{inputInfo}")
    for i in range(len(inputInfo)):
        if(inputInfo[i]=="itmathrepetitor"):
            inputInfo[i]="silence"
    print(f"Результат\n{inputInfo}")

def main():
    try:
        tasks = {
            1: TaskOne,
            2: SecondTask,
            3: ThirdTask,
            4: FourthTask,
            5: FivedTask,
            6: SixedTask,
            7: SevenedTask,
            8: EightedTask,
            9: NinedTask,
            10: TenedTask,
            11: ElevenedTask,
            12: TwelwedTask
        }
        taskForWork = int(input("Введите номер задания от 1 до 12: "))
        if(taskForWork in tasks):
            tasks[taskForWork]()
        else:
            print("Задание не найдено")

    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
