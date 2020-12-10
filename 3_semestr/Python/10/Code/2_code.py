import math
import random


class Point:
   
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def distanceTo(self,b):
        if(type(b) is not Point):
            print("Переданный объект не имеет необходимый тип b")
            return 0
        if(type(self) is not Point):
            print("Переданный объект не имеет необходимый тип self")
            return 0
        return math.sqrt((math.pow((b._x - self._x),2)+ math.pow((b._y - self._y),2)))

    def __str__(self):
        return "x={0} y={1}".format(self._x, self._y)


def GetRandomPoint():
    return Point(random.randint(1,100),random.randint(1,100))


def main():
    try:
        print("Задание 2")
        pointA=GetRandomPoint()
        pointB=GetRandomPoint()

        print("Получили рандомную точку A {0}".format(str(pointA)))
        print("Получили рандомную точку B {0}".format(str(pointB)))

        print("Евклидово растояние {0}".format(pointA.distanceTo(pointB)))

        print("Метод отображения A {0}".format(str(pointA)))
        print("Метод отображения B {0}".format(str(pointB)))
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
