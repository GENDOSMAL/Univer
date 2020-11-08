
def complementWC(dncCode):
    res = ""
    for dncEl in reversed(dncCode):
        if dncEl.lower() == 'a':
            res += 'T'
        elif dncEl.lower() == 't':
             res +=  'A'
        elif dncEl.lower() == 'g':
             res +=  'C'
        else:
             res +=  'G'
    return res

def printInputAndReverse(input,reverse):
    print(input)    
    for base in input:
        print('|', end='')    
    print()            
    for base in reversed(reverse):
        print(base, end='')        
    print()

def main():
    try:
        inputDncCode = input("Введите строку ДНК: ")
        if inputDncCode:
            preObrDncCode=complementWC(inputDncCode)
            print("Результат преобразования")
            printInputAndReverse(inputDncCode,preObrDncCode)
        else:
            print("Ввведенные данные пусты")
    except Exception:
        print("Ошибка при работе программы ", traceback.format_exc())


if __name__ == "__main__":
    main()
