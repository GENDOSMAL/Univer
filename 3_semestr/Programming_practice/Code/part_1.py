import random



class TryData:

    def __init__(self):
        self.expectedCode=random.sample(range(0,9), 4)
        print(self.expectedCode)

    expectedCode=[]
    objectInfo=[]
    def AddNewTry(self,value,countOfBull,countOfCow):
        self.objectInfo.append(TryInf(value,countOfBull,countOfCow))
    
    def WriteData(self):
        if(len(self.objectInfo)==0):
            return
        print("Ход\tЧисло\tБыки\tКоровы")
        count=0
        print("———————————————————————————————")
        for item in self.objectInfo:
            count += 1
            print(f"{count}\t{item._value}\t{item._countOfBull}\t{item._countOfCow}")


    def IsInputNormal(self,data):
        try:
            return (len(self.PrepareStrToOperate(data))==4)
        except Exception:
            return False


    def PrepareStrToOperate(self,data):
        data=data.strip()
        datInList=list(data)
        datInList=list(dict.fromkeys(datInList))
        guessnumbers = list(map(int, datInList))
        return guessnumbers

    def NewInput(self,value):
        if self.IsInputNormal(value)!=True:
            print(f"Введенное число не соответствует требованиям [{value}]")
            return False 
        numberToOperate=self.PrepareStrToOperate(value)
        cows = 0
        bulls = 0
        for i in range(len(self.expectedCode)):
            print(f"{numberToOperate[i]} {self.expectedCode[i]}")
            if numberToOperate[i] in self.expectedCode and numberToOperate[i] != self.expectedCode[i]:
                cows += 1
            if numberToOperate[i] in self.expectedCode and numberToOperate[i] == self.expectedCode[i]:
                bulls += 1

        self.AddNewTry(value,bulls,cows)
        self.WriteData()

        if(bulls==4):
            return True

        return False


    
    

class TryInf:
    def __init__(self,value,countOfBull,countOfCow):
        self._value=value
        self._countOfBull=countOfBull
        self._countOfCow=countOfCow

def GetRandomCode():
    return random.sample(range(0,9), 4)

def main():
    try:
        print("Начинаем игру 'Быки и коровы' правила можно посмотреть тут http://xn--90aeltibbl.xn--p1ai/Articles/BullsAndCowsRules")
        print("Число задано. Игра будет вестить до тех пор пока не игрок не выйграет, либо до ввода 0")
     
        helpObject=TryData()
        while True:
            data=input("=>")
            if(data=='0'):
                break
            if(helpObject.NewInput(data)):
                str1=''
                print(f"Поздравляем. Число {data} огадано! ")
                break
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())

        
if __name__ == "__main__":
    main()