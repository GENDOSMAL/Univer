import traceback

def main():
    try:
        print("Начало работы программы")
        tempSize=float(input("Введите значение тепмературы: "))
        typeOfWeather=int(input("Тип погоды:\nДождь - 1\nСнег- 2 \nВетер - 3\nЯсно - 4\n"))
        if tempSize > 22:
            if typeOfWeather==1:
                print("На улице тепло, но есть дождь. Одентесь в летнее и возьмите зонт")
            elif typeOfWeather==2:
                print("Сидите дома")
            elif typeOfWeather==3:
                print("На улице тепло, но ветренно. Одевайтесь в летнее но нацеленное на лето в Москве")
            elif typeOfWeather==4:
                print("На улице тепло и ясно, одевайтесь в летнее. Не забудьте кепку и немного воды.")
            else:
                print("Не ожиданное значени типа погоды. Предполагаю что нужно одеться по летнему и взять зонт (лишним не будет)")
        elif tempSize <= float(21.9) and tempSize>=float(10):
            if typeOfWeather==1:
                print("На улице дождь и достаточно тепло. Стоит взять зонт и одется по межсезону.")
            elif typeOfWeather==2:
                print("На улице снег. Сидите дома")
            elif typeOfWeather==3:
                print("На улице ветер. Одевайтесь по теплее на одежде предназначенной для межсезона")
            elif typeOfWeather==4:
                print("На улице солненчно. Одевайтесь в легкую одежду для межсезона!")
            else:
                print("Не ожиданное значени типа погоды. Предполагаю что нужно одеться по летнему и взять зонт (лишним не будет)")

        elif  tempSize <= float(9.9) and tempSize>=float(-5):
            if typeOfWeather==1:
                print("На улице возможен дождь, а также возможны низкие температуры. Одевайтесь по зимненму тепло и возьмите зонт.")
            elif typeOfWeather==2:
                print("На улице снег и прохладно. Стоит взять зонт если вы не любите мокрую верхнюю олежду при входе в помещение. Одеваться стоит по зимнему тепло")
            elif typeOfWeather==3:
                print("На улице ветер и прохладно. Стоит одеваться по зимнему.")
            elif typeOfWeather==4:
                print("На улице ясно и прохлдано. Одевайтесь по зимнему")
            else:
                print("Не ожиданное значени типа погоды. Предполагаю что нужно одеться по летнему и взять зонт (лишним не будет)")

        elif  tempSize <= float(-5.1) and tempSize>float(-20):
            if typeOfWeather==1:
                print("На улице дожждь и холодно. Не советую вообше выходить на улицу")
            elif typeOfWeather==2:
                print("На улице снег и ходно. Одеватйтесь очень тепло, также стоит взять перчатки и шарф")
            elif typeOfWeather==3:
                print("На улице ходно и ветренно. Если нет необходимости то стои вообще не идти. При выходе стоит взять что-то теплое на все части тела!")
            elif typeOfWeather==4:
                print("На улице холдная зима и ясно. Одевайтесь тепло, также стоит взять перчатки и шарф")
            else:
                print("Не ожиданное значени типа погоды. На улице холодно, при выходе стоит взять перчатки и щарф")
        elif tempSize <= -20:
            if typeOfWeather==1:
                print("На улице дожждь и очень холодно. Не советую вообше выходить на улицу")
            elif typeOfWeather==2:
                print("На улице снег и очень ходно. Одеватйтесь очень тепло, также стоит взять перчатки и шарф")
            elif typeOfWeather==3:
                print("На улице очень ходно и ветренно. Если нет необходимости то стои вообще не идти. При выходе стоит взять что-то теплое на все части тела!")
            elif typeOfWeather==4:
                print("На улице холдная зима и ясно. Одевайтесь очень тепло, также стоит взять перчатки и шарф")
            else:
                print("Не ожиданное значени типа погоды. На улице холодно, одевайтесь по зимнему, но наверное вообще не стоит выходить")

        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
