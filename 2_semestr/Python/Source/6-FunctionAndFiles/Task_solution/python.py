import traceback

class EightVariantException(Exception):
    def __init__(self,text):
        self.txt=text


someStrongText="Ошибка в дате"
def Task2():
    inputInfo = list(input("Введите даты для определения (через пробел) ").split(" "))
    d={}
    for i in inputInfo:
        typeOf=GetPartOfYear(i)
        if(typeOf in d.keys()):
            d[typeOf]=d[typeOf]+1
        else:
            d[typeOf]=1+bgvnlk;bnvpg0o[rgtwf p0n9i[r5etpor4]]

    print(f"Задание 2 выполнено. Его итоги для введенных данных \n [{inputInfo}]\n:")
    strange=False
    if(someStrongText in d.keys()):
        strange=True
        print(f"Введено ошибочных дат [{d[someStrongText]}]")

    if(len(d)==1 and strange ):
        return

    print("Время года\tКоличество")
    print("____________________________")
    for k, v in d.items():
        if(k==someStrongText):
            continue
        print(f"{k}\t\t|\t{v}")
        


def Task1():
    dateInf=str(input("Введите дату в формате [dd.mm.yy]: "))
    print(GetPartOfYear(dateInf))

def GetPartOfYear(datIenfo):
    try:
        datePart = datIenfo.split(".")
        if(len(datePart)!=3):
            raise Exception("В заданной дате значений не равно 3 параметрам, которые предполагалось использовать в качестве дат" )

        if(not(datePart[0].isdigit()) or not( datePart[1].isdigit()) or not( datePart[2].isdigit()) ):
            raise Exception("В заданной дате некоторые части не являются целочисленным типом данных")
        
        if(not(int(datePart[1])>=1 and int(datePart[1])<=12)):
            raise Exception("В заданной дате месяц больше возможного числа")

        CheckDatebyMounth(datePart[0],datePart[1])
        return GetPartByMounth(int(datePart[1]))
    except EightVariantException as mer:
        print(mer)
        return someStrongText
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())
        return someStrongText


def CheckDatebyMounth(day,mounth):
    mounth=int(mounth)
    day=int(day)
    varErrorText="В заданной дате число чем больше возможно в этом месяце"
    if (mounth==4 or mounth==6 or mounth==9 or mounth==11):
        if(not(day>=1 and day<=30)):
            raise EightVariantException(varErrorText)
    elif (mounth==2):
        if(not(day>=1 and day<=28)):
            raise EightVariantException(varErrorText)
    else:
        if(not(day>=1 and day<=31)):
            raise EightVariantException(varErrorText)

def GetPartByMounth(month):
    if month < 3 or month  == 12:
        return "Зима"
    if 3 <= month < 6:
        return "Весна"
    if 6 <= month < 9:
        return "Лето"
    if 9 <= month < 12:
        return "Осень"

def Main():
    try:
        print("Начало работы программы")
        tasks = {
            1: Task1,
            2: Task2,
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