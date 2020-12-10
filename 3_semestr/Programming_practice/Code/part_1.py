# Основное задание 

# Реализовать программу, с которой можно играть в логическую игру «Быки и коровы» (описание правил игры: http://робомозг.рф/Articles/BullsAndCowsRules ). 
# Программа загадывает число, пользователь вводит очередной вариант отгадываемого числа, программа возвращает количество быков и коров и в случае выигрыша 
# игрока сообщает о победе и завершается. Сама программа НЕ ходит, т.е. не пытается отгадать число загаданное игроком.
# Взаимодействие с программой производится через консоль, при запросе данных от пользователя программа сообщает, что ожидает от пользователя и проверяет корректность ввода.


import random


class TryData:

    def __init__(self):
        self.expectedCode = random.sample(range(0, 9), 4)

    expectedCode = []
    objectInfo = []

    def AddNewTry(self, value, countOfBull, countOfCow):#Добавить новую попытку  отгадать
        self.objectInfo.append(TryInf(value, countOfBull, countOfCow))

    def WriteData(self):#Вывести данные в консоль
        if(len(self.objectInfo) == 0):
            return
        print("Ход\tЧисло\tБыки\tКоровы")
        count = 0
        print("———————————————————————————————")
        for item in self.objectInfo:
            count += 1
            print(f"{count}\t{item._value}\t{item._countOfBull}\t{item._countOfCow}")

    def IsInputNormal(self, data):#Проверить на то что ввод нормлен, что данные из 4 цифр и что они разные
        try:
            return (len(self.PrepareStrToOperate(data)) == 4)
        except Exception:
            return False

    def PrepareStrToOperate(self, data):#Подготовка данных для некоторых операций над ними
        data = data.strip()
        datInList = list(data)
        datInList = list(dict.fromkeys(datInList))
        guessnumbers = list(map(int, datInList))
        return guessnumbers

    def NewInput(self, value):#Новый ввод данных от пользователя
        if self.IsInputNormal(value) != True:
            print(f"Введенное число не соответствует требованиям [{value}]")
            return False
        numberToOperate = self.PrepareStrToOperate(value)
        cows = 0
        bulls = 0
        for i in range(len(self.expectedCode)):
            if numberToOperate[i] in self.expectedCode and numberToOperate[i] != self.expectedCode[i]:
                cows += 1
            if numberToOperate[i] in self.expectedCode and numberToOperate[i] == self.expectedCode[i]:
                bulls += 1

        self.AddNewTry(value, bulls, cows)
        self.WriteData()

        if(bulls == 4):
            return True

        return False


class TryInf:#Класс описывающий ходы, сделан для хранения данных о ходах в списке
    def __init__(self, value, countOfBull, countOfCow):
        self._value = value
        self._countOfBull = countOfBull
        self._countOfCow = countOfCow


def GetRandomCode():#Получить рандомный из разных цифр код
    return random.sample(range(0, 9), 4)


def main():
    try:
        print("Начинаем игру 'Быки и коровы' правила можно посмотреть тут http://xn--90aeltibbl.xn--p1ai/Articles/BullsAndCowsRules")
        print("Число задано. Игра будет вестить до тех пор пока не игрок не выйграет, либо до ввода 0")

        helpObject = TryData()
        while True:
            data = input("=>")
            if(data == '0'):
                break
            if(helpObject.NewInput(data)):
                print(f"Поздравляем. Число {data} огадано! ")
                break
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
