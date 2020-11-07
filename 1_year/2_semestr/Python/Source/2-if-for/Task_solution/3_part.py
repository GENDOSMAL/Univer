import traceback
import math
def core(a,b,sqrtdesc):
    return (-b+sqrtdesc)/(2*a)
def main():
    try:
        print("Начало работы программы")
        ainfo=float(input("Введите значение а (если нет то просто 0): "))
        binfo=float(input("Введите значение b (если нет то просто 0): "))
        cinfo=float(input("Введите значение c (если нет то просто 0): "))
        
        desc=(binfo*binfo)-(4*ainfo*cinfo)
        print("Дескриминант ",desc)
        if(desc<0):
            print("Корней нет")
            print("Конец работы программы")
            return
        sqrtdesc=math.sqrt(desc)
        print("Корень из него ",sqrtdesc)

        if(sqrtdesc==0):
            print("Корень только 1 и равен он ",core(ainfo,binfo,sqrtdesc))
        else:
            print("Корень 1 равен ",core(ainfo,binfo,sqrtdesc))
            print("Корень 2 равен ",core(ainfo,binfo,-sqrtdesc))
        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
