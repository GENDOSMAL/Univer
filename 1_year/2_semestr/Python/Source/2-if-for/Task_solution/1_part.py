import traceback


def main():
    try:
        print("Начало работы программы")
        tempSize = input("Введите температуру: ")
        typeOfDownFall = input(
            "Тип осадков:\nДождь - 1\nЛивень- 2 \nСнег - 3\nЛедяной дождь - 4\nСолнечно - 5\n")
        typeOfDownFall = int(typeOfDownFall)
        tempSize=float(tempSize)
        if tempSize > 22:
            if typeOfDownFall == 1:
                print("На улице дождь, но тепло, возьмите зонт")
            elif typeOfDownFall == 2:
                print(
                    "На улице тепло но идет ливень, если есть накидка от от дождя лучше взять ее!, если нет возьмите зонт")
            elif typeOfDownFall == 3:
                print("На улице тепло, но неождинно идет снег.\n Предполагаю что лучше взять зонт, но самое идеальное сидеть дома ибо снег при такой температуре явно не очень полезный.")
            elif typeOfDownFall == 4:
                print("На улице тепло, но неождинно идет ледяной дождь.\n Предполагаю что лучше взять зонт, но самое идеальное сидеть дома ибо ледяной дождь при такой температуре явно не очень полезный.")
            elif typeOfDownFall == 5:
                print("На улице тепло и солнечно, желательно взять воды и надеть что-то на голову во избежание солнечного удара.")
            else:
                print("На улице тепло и солнечно, желательно взять воды и надеть что-то на голову во избежание солнечного удара.\n Заданные осадки в настоящее время неизвестны!")
        elif tempSize <= float(21.9) and tempSize>=float(10):
            if typeOfDownFall == 1:
                print("На улице дождь и прохладно(одевайтесь теплее), возможен ветер, возьмите зонт")
            elif typeOfDownFall == 2:
                print(
                    "На улице прохладно(одевайтесь теплее) и возможен ветер, а также идет ливень, если есть накидка от от дождя лучше взять ее!, если нет возьмите зонт")
            elif typeOfDownFall == 3:
                print("На улице прохладно(одевайтесь теплее) и возможен ветер, но неождинно идет снег.\n Предполагаю что лучше взять зонт, но самое идеальное сидеть дома ибо снег при такой температуре явно не очень полезный.")
            elif typeOfDownFall == 4:
                print("На улице прохладно(одевайтесь теплее) и возможен ветер, но неождинно идет ледяной дождь.\n Предполагаю что лучше взять зонт, но самое идеальное сидеть дома ибо ледяной дождь при такой температуре явно не очень полезный.")
            elif typeOfDownFall == 5:
                print("На улице прохладно(одевайтесь теплее) и возможен ветер.")
            else:
                print("На улице прохладно(одевайтесь теплее) и возможен ветер. Заданные осадки в настоящее время неизвестны!")
        elif  tempSize <= float(9.9) and tempSize>=float(-5):
            if typeOfDownFall == 1:
                print("На улице дождь и холодно(желательно одеть что-то зимнее), возможен ветер, возьмите зонт")
            elif typeOfDownFall == 2:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер, а также идет ливень, если есть накидка от от дождя лучше взять ее!, если нет возьмите зонт")
            elif typeOfDownFall == 3:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер,  и идет снег.\n Предполагаю что лучше взять зонт ибо температура изменчива.")
            elif typeOfDownFall == 4:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер, но неождинно идет ледяной дождь.\n Предполагаю что лучше взять зонт ибо температура изменчива.")
            elif typeOfDownFall == 5:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер.")
            else:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер. Заданные осадки в настоящее время неизвестны!")
        elif  tempSize <= float(-5.1) and tempSize>float(-20):
            if typeOfDownFall == 1:
                print("На улице при условии отрицательной температуры идет дождь (стоит задуматься на счет вообще выхода из дома), но если прям есть желание, то возьмите зонт.\n Также там холодно(одевайтесь в зимнее ), возможен ветер")
            elif typeOfDownFall == 2:
                print("На улице при условии отрицательной температуры идет дождь (стоит задуматься на счет вообще выхода из дома), но если прям есть желание, то возьмите зонт.\n Также там холодно(одевайтесь в зимнее ), возможен ветер")
            elif typeOfDownFall == 3:
                print("На улице холодно(желательно одеть зимнее) и возможен ветер,  а также идет снег.\n Если вы плохо относитесь к осадкам которые в теплых местах могут расстаять прямо на вашей одежде, то луше взять зонт.")
            elif typeOfDownFall == 4:
                print("а улице холодно(желательно одеть зимнее) и возможен ветер, но неождинно идет ледяной дождь. Предполагаю что лучше взять зонт.")
            elif typeOfDownFall == 5:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер.")
            else:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер. Заданные осадки в настоящее время неизвестны!")
        elif tempSize <= -20:
            if typeOfDownFall == 1:
                print("На улице очень холодно, а также идет дождь, стоит задуматься на счет выхода из дома, но в любом случае стоит взять зонт.")
            elif typeOfDownFall == 2:
                print("На улице очень холодно, а также идет ливень, стоит задуматься на счет выхода из дома, но в любом случае стоит взять зонт.")
            elif typeOfDownFall == 3:
                print("На улице очень холодно и возможен ветер,  а также идет снег. Советую не сильно далеко отходить из теплых помещений на долгое время.\n Если вы плохо относитесь к осадкам которые в теплых местах могут расстаять прямо на вашей одежде, то луше взять зонт.")
            elif typeOfDownFall == 4:
                print("На улице очень холодно и возможен ветер, но неождинно идет ледяной дождь.\n Предполагаю что лучше взять зонт, но лучще вообще остаться дома. ")
            elif typeOfDownFall == 5:
                print("На улице очень холодно и возможен ветер.\n Советую не сильно далеко отходить из теплых помещений на долгое время")
            else:
                print("На улице холодно(желательно одеть что-то зимнее) и возможен ветер.\n Заданные осадки в настоящее время неизвестны!")
 
        print("Конец работы программы")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
