import re
import sys

class ChessPiece(object):
    def __init__(self,color,x,y): #Инициализурем цвета
        self.color=color
        self.x=x
        self.y=y
        
    def can_it_move_basic(self,x2,y2,field,number): #Основная логика
        if (number%2==0)==(self.color=='white'):
            if self.can_it_move(x2,y2,field):
                return True
            else:
                print("Вы не можете сделать данный ход!")
                return False
        else:
            print("Это не ваша шахматная фигура!")
            return False
        
class Pawn(ChessPiece): # Класс пешки
    def __init__(self,color,x,y): #Инициалищация
        super().__init__(color,x,y)
        self.letter='p' if self.color=='black' else 'P'
    
    def can_it_move(self,x2,y2,field): #Может ли делать ход
        x1,y1=self.x,self.y
        distance=x2-x1 if self.color=='black' else x1-x2
        if type(field[x2][y2])==EmptyCell:
            if y1==y2:
                if distance==1:
                    return True
                elif distance==2 and (x1==1 or x1==6) and type(field[x1+(x2-x1)//2][y1])==EmptyCell:
                    return True
                          
        elif field[x1][y1].color!=field[x2][y2].color and distance==1 and abs(y1-y2)==1:
            return True
        return False
      
class King(ChessPiece): #Класс короля
    def __init__(self,color,x,y): #Инициализация
        super().__init__(color,x,y)
        self.letter='k' if self.color=='black' else 'K'
        
    def can_it_move(self,x2,y2,field): #Может ли делать ход
        x1,y1=self.x,self.y
        distance=abs(x2-x1)<=1 and abs(y2-y1)<=1
        return distance and self.color!=field[x2][y2].color
    
    def check_the_king(self,field): 
        for i in field:
            for j in i:
                if j.can_it_move(self.x,self.y,field):
                    return True
        return False
    
    def checkmate(self,field): #Проверка на шах и мат
        x1,y1=self.x,self.y
        if x1==0:
            i_iter=(0,1)
        elif x1==7:
            i_iter=(-1,0)
        else:
            i_iter=(-1,0,1)
        if y1==0:
            j_iter=(0,1)
        elif y1==7:
            j_iter=(-1,0)
        else:
            j_iter=(-1,0,1)
            
        for i in i_iter:
            for j in j_iter:
                x2,y2=x1+i,y1+j
                if self.can_it_move(x2,y2,field):
                    temp_chesse_piece=field[x2][y2]
                    field[x2][y2]=field[x1][y1]
                    field[x2][y2].x=x2
                    field[x2][y2].y=y2
                    field[x1][y1]=EmptyCell('other',x1,y1)
                    if not self.check_the_king(field):
                        field[x1][y1]=field[x2][y2]
                        field[x1][y1].x=x1
                        field[x1][y1].y=y1
                        field[x2][y2]=temp_chesse_piece
                        field[x2][y2].x=x2
                        field[x2][y2].y=y2
                        return False
                    field[x1][y1]=field[x2][y2]
                    field[x1][y1].x=x1
                    field[x1][y1].y=y1
                    field[x2][y2]=temp_chesse_piece
                    field[x2][y2].x=x2
                    field[x2][y2].y=y2
        return True      
         
class Queen(ChessPiece): #Класс королевы
    def __init__(self,color,x,y): #Инициализация
        super().__init__(color,x,y)
        self.letter='q' if self.color=='black' else 'Q'
        
    def can_it_move(self,x2,y2,field): #Логика ходов
        x1,y1=self.x,self.y
        distance=abs(x1-x2),abs(y1-y2)
        if distance[0]==distance[1]:
            for i in range(distance[0]-1):
                if type(field[x1+(i+1) if x1<x2 else x1-(i+1)][y1+(i+1) if y1<y2 else y1-(i+1)])!=EmptyCell:
                    return False
        elif distance[0]==0:
            for i in range(distance[1]-1):
                if type(field[x1][y1+i+1 if y1<y2 else y1-i-1])!=EmptyCell:
                    return False
        elif distance[1]==0:
            for i in range(distance[0]-1):
                if type(field[x1+i+1 if x1<x2 else x1-i-1][y1+i])!=EmptyCell:
                    return False
        else:
            return False
        return self.color!=field[x2][y2].color
      
class Rook(ChessPiece): #Класс ладьи
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='r' if self.color=='black' else 'R'
        
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        if x2-x1==0 and y2-y1!=0:
            for i in range(abs(y2-y1)-1):
                if type(field[x1][y1+i+1 if y1<y2 else y1-i-1])!=EmptyCell:
                    return False
        elif x2-x1!=0 and y2-y1==0:
            for i in range(abs(x2-x1)-1):
                if type(field[x1+i+1 if x1<x2 else x1-i-1][y1])!=EmptyCell:
                    return False
        else:
            return False
        return self.color!=field[x2][y2].color
        
class Knight(ChessPiece): #Класс коня
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='n' if self.color=='black' else 'N'
        
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        distance=abs(x2-x1), abs(y2-y1)
        return (distance==(2,1) or distance==(1,2)) and self.color!=field[x2][y2].color   
    
class Bishop(ChessPiece): #Класс ферзя
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='b' if self.color=='black' else 'B'
        
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        distance=abs(x2-x1), abs(y2-y1)
        if distance[0]==distance[1]:
            for i in range(distance[0]-1):
                if type(field[x1+(i+1) if x1<x2 else x1-(i+1)][y1+(i+1) if y1<y2 else y1-(i+1)])!=EmptyCell:
                    return False
        else:
            return False
        return self.color!=field[x2][y2].color
    
class Deer(ChessPiece): #Дополнительное задание (Новая фигура - Олень)
    '''Олень ходит как конь только на клетку вперед больше (3 в одну сторону 1 в другую)'''
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='d' if self.color=='black' else 'D'
        
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        distance=abs(x2-x1), abs(y2-y1)
        return (distance==(3,1) or distance==(1,3)) and self.color!=field[x2][y2].color
    
class Ant(ChessPiece): #Дополнительное задание (Новая фигра - Муравей)
    '''Муравей ходит по диагонали и ест вперед (все на 1 клетку)'''
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='a' if self.color=='black' else 'A'
        
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        distance=x2-x1 if self.color=='black' else x1-x2
        if distance==1:
            if type(field[x2][y2])==EmptyCell and abs(y1-y2)==1:
                return True     
            elif field[x1][y1].color!=field[x2][y2].color and y1==y2:
                return True
        return False  
    
class Fox(ChessPiece): #Дополнительное задание (Новая фигура - Лиса)
    '''Лиса еще хитрее Дамы и может ходить в любую клетку не дальше 2 вокруг себя'''
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='f' if self.color=='black' else 'F'
        
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        distance=abs(x2-x1), abs(y2-y1)
        return distance[0]<=2 and distance[1]<=2 and self.color!=field[x2][y2].color 
        
class EmptyCell(ChessPiece): #Класс пустой клетки
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='.'        
    
    def can_it_move(self,x2,y2,field):
        return False
        
class Checker(ChessPiece): #Класс шашки
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
        self.letter='x' if self.color=='black' else 'X'
        self.superuser=False
    
    def can_it_move(self,x2,y2,field):
        x1,y1=self.x,self.y
        distance=x2-x1 if self.color=='black' else x1-x2
        if type(field[x2][y2])==EmptyCell:
            if not self.superuser:
                if distance==1 and abs(y1-y2):
                    return True
                if abs(x1-x2)==2 and abs(y1-y2)==2:
                    x3=x1+(x2-x1)//2
                    y3=y1+(y2-y1)//2
                    if field[x3][y3].color!=self.color and type(field[x3][y3])!=EmptyCell:
                        return True
            else:
                if abs(x1-x2)==abs(y1-y2) and x1!=x2:
                    x_=1 if x2>x1 else -1
                    y_=1 if y2>y1 else -1
                    for i in range(abs(x1-x2)-1):
                        if field[x1+x_*(i+1)][y1+y_*(i+1)].color==self.color:
                            break
                    else:
                        return True               
        return False
           
class Chessboard(object): #Класс шахматной доски
    def __init__(self):
        self.number_of_move=0
        self.field=[[None]*8 for _ in range(8)]
        self.input_rules="Введите координаты вашего хода в формате: 'A1 B2'.\nНачальная ячейка и конечная - должны быть разделены пробелом.\nВведите 'help' чтобы вызвать это сообщение снова"
        self.rules=("Введите 'help' чтобы вызвать это сообщение снова. \nВведите 'stop' чтобы прекратить игру")
        
    def create_chessborad(self,modifier):
        if(modifier!= 'common'):
            self.rules+="\nПредставлена модифицированная версия шахмат. Суть модифицированной версии: Добавлены новые фигуры\n"
            self.rules+="F(f) Лиса еще хитрее Дамы и может ходить в любую клетку не дальше 2 вокруг себя\n "
            self.rules+="A(a) Муравей ходит по диагонали и ест вперед (все на 1 клетку)\n"
            self.rules+="D(d) Олень ходит как конь только на клетку вперед больше (3 в одну сторону 1 в другую)\n"

        for i in (0,7):
            self.field[0][i]=Rook('black',0,i)
            self.field[7][i]=Rook('white',7,i)
        for i in (1,6):
            if modifier=='common':
                self.field[0][i]=Knight('black',0,i)
                self.field[7][i]=Knight('white',0,i)
            else:
                self.field[0][i]=Deer('black',0,i)
                self.field[7][i]=Deer('white',0,i)
        for i in (2,5):
            self.field[0][i]=Bishop('black',0,i)
            self.field[7][i]=Bishop('white',7,i)
        if modifier=='common':
            self.field[0][3]=Queen('black',0,3)
            self.field[7][3]=Queen('white',7,3)
        else:
            self.field[0][3]=Fox('black',0,3)
            self.field[7][3]=Fox('white',7,3)
            
        self.field[0][4]=King('black',0,4)
        self.black_king=self.field[0][4]
        self.field[7][4]=King('white',7,4)
        self.white_king=self.field[7][4]
        for i in range(8):
            if modifier=='common':
                self.field[1][i]=Pawn('black',1,i)
                self.field[6][i]=Pawn('white',6,i)
            else:
                self.field[1][i]=Ant('black',1,i)
                self.field[6][i]=Ant('white',6,i)
            for j in range(2,6):
                self.field[j][i]=EmptyCell('other',j,i)
    
    def create_chessborad_for_checkers(self):
        for i in range(8):
            for j in range(8):
                self.field[i][j]=EmptyCell('other',i,j)
        for i in range(3):
            for j in range(0,7,2):
                self.field[i][(j+i)%8]=Checker('black',i,(j+i)%8)
                self.field[i+5][(j+i+1)%8]=Checker('white',i+5,(j+i+1)%8)
                
    def print_screen(self):
        print('   A B C D E F G H\n')
        for i in range(8):
            print(8-i,end='  ')
            for j in range(8):
                print(self.field[i][j].letter,end=' ')
            print(' ',8-i)
        print('\n   A B C D E F G H')
    
    def convert_to_numb(self,*coord):
        alphabet='abcdefgh'
        coordinates=[]
        for el in coord:
            coordinates.append(8-int(el[1]))
            coordinates.append(alphabet.index(el[0]))
        return coordinates
    
    def move_chess_piece(self,x1,y1,x2,y2):
        if self.field[x1][y1].can_it_move_basic(x2,y2,self.field,self.number_of_move):
            temp_chesse_piece=self.field[x2][y2]
            self.field[x2][y2]=self.field[x1][y1]
            self.field[x2][y2].x=x2
            self.field[x2][y2].y=y2
            self.field[x1][y1]=EmptyCell('other',x1,y1)
            
            if (self.field[x2][y2].color=='white' and self.white_king.check_the_king(self.field)) or (self.field[x2][y2].color=='black' and self.black_king.check_the_king(self.field)):
                print('Шах королю!!!')
                self.field[x1][y1]=self.field[x2][y2]
                self.field[x1][y1].x=x1
                self.field[x1][y1].y=y1
                self.field[x2][y2]=temp_chesse_piece
                self.field[x2][y2].x=x2
                self.field[x2][y2].y=y2
                return False
            self.number_of_move+=1
            return True
        else:
            return False
    
    def move_checkers_piece(self,*coordinates):
        temp=0

        for i in range(len(coordinates)//2-1):
            x1=coordinates[i*2]
            y1=coordinates[i*2+1]
            x2=coordinates[i*2+2]
            y2=coordinates[i*2+3]
            if self.field[x1][y1].can_it_move_basic(x2,y2,self.field,self.number_of_move):
                if (x2==0 and self.field[x1][y1].color=='white')or(x2==7 and self.field[x1][y1].color=='black'):
                    self.field[x1][y1].superuser=True
                    self.field[x1][y1].letter='Q' if self.field[x1][y1].color=='white' else 'q'
                self.field[x2][y2]=self.field[x1][y1]
                self.field[x2][y2].x=x2
                self.field[x2][y2].y=y2
                x_=1 if x2>x1 else -1
                y_=1 if y2>y1 else -1
                for i in range(abs(x1-x2)):

                    self.field[x1+x_*(i)][y1+y_*(i)]=EmptyCell('other',x1+x_*(i),y1+y_*(i))

                temp+=1

        return bool(temp)
    
    def start_playing_chess(self,modifier='common'):

        self.create_chessborad(modifier)

        self.number_of_move=0
       
        print("Давайте сыграем в нахматы!!!\n"+self.rules)
       
        while True:
            self.print_screen()
            if self.number_of_move%2==0:
                if self.white_king.check_the_king(self.field):
                    if self.white_king.checkmate(self.field):
                        print('Шах и мат\nЧёрные победили')
                        break
                    print('Шах королю!!!')
                print('Ходят белые (большие символы).')
            else:
                if self.black_king.check_the_king(self.field):
                    if self.black_king.checkmate(self.field):
                        print('Шах и мат!\nБелые победили')
                        break
                    print('Шах королю!!!')
                print('Ходят чёрные (маленькие символы).')
                
            while True:
                coordinates=input(self.input_rules+'\n').lower()
                searcher=re.search('[a-h]\d [a-h]\d\Z',coordinates)
                if coordinates=='help':
                    print(self.rules)
                    continue
                elif coordinates=='stop':
                    return
                elif searcher:
                    coordinates=coordinates.split(' ')
                    if self.move_chess_piece(*self.convert_to_numb(*coordinates)):
                        break
                else:
                    print('Неверный ввод!\n'+self.input_rules)
    
    def start_playing_checkers(self):
        self.create_chessborad_for_checkers()
        self.number_of_move=0
        print("Давйте сыграем в шашки!!!\n"+self.rules)
        while True:
            self.print_screen()
            b,w=0,0
            for i in range(8):
                for j in range(8):
                    if self.field[i][j].color=='white':
                        w+=1
                    elif self.field[i][j].color=='black':
                        b+=1
            if not b:
                print('Белые победили!')
                return
            elif not w:
                print('Чёрные победили!')
                return
            if self.number_of_move%2==0:
                print('Ходят белые (большие символы).')
            else:
                print('Ходят чёрные (маленькие символы).')
            while True:
                coordinates=input(self.input_rules+'\n').lower()
                searcher=re.search('[a-h]\d( [a-h]\d)+\Z',coordinates)
                if coordinates=='help':
                    print(self.rules)
                    continue
                elif coordinates=='stop':
                    return
                elif searcher:
                    coordinates=coordinates.split(' ')
                    if self.move_checkers_piece(*self.convert_to_numb(*coordinates)):
                        self.number_of_move+=1
                        break
                else:
                    print('Неверный ввод!\n'+self.input_rules)

def main():
    chessboard=Chessboard()                    
    while True:
        try:
            inpt=input('Введите:\n1.Для шахмат\n2.Для модифицированных шамат\n3.Для шашек \nstop  Для выхода \n')
            if inpt=='1':
                chessboard.start_playing_chess()
            elif inpt=='2':
                chessboard.start_playing_chess('other')
            elif inpt=='3':
                chessboard.start_playing_checkers()
            else:
                print("Программа закрывается!")
                break
        except:
            print("Не ожиданная ошибка при работе программы:", sys.exc_info()[0])


if __name__ == "__main__":
    main()