from math import *

n1 = float(input('ВВедите первое число:'))
'''Принимаем на вход знак выражения'''
zn = input('ВВедите знак выражения:')
'''Принимаем на вход второе число'''
if zn != 'sin' and zn != 'cos' and zn != 'tan':
    n2 = float(input('ВВедите второе число:'))
else:
    n2 = int(0)
'''Проверяем ввели ли числа'''
class kalkul:
    def __init__(self, n1, n2, zn):
        self.n1 = n1
        self.n2 = n2
        self.zn = zn

    def ingeneer(self):
        if type(self.n1) != float and type(self.n2) != float:
            return 'ERROR'
        '''Проверяем знак выражения и выводим ответ'''
        if self.zn == '+':
            return 'Ответ:',self.n1+self.n2
        elif self.zn == '-':
            return 'Ответ:',self.n1-self.n2
        elif self.zn == '*':
            return 'Ответ:',self.n1*self.n2
        elif self.zn == '/':
            return 'Ответ:',self.n1/self.n2
        elif self.zn == '//':
            return 'Ответ:',self.n1//self.n2
        elif self.zn == 'sin':
            return 'Ответ:', sin(self.n1)
        elif self.zn == 'cos':
            return 'Ответ:', cos(self.n1)
        elif self.zn == 'tan':
            return 'Ответ:', tan(self.n1)
        else:
            return 'ERROR'

    def obichniy(self):
        if type(self.n1) != float and type(self.n2) != float:
            return 'ERROR'
        '''Проверяем знак выражения и выводим ответ'''
        if self.zn == '+':
            return 'Ответ:',self.n1+self.n2
        elif self.zn == '-':
            return 'Ответ:',self.n1-self.n2
        elif self.zn == '*':
            return 'Ответ:',self.n1*self.n2
        elif self.zn == '/':
            return 'Ответ:',self.n1/self.n2
        elif self.zn == '//':
            return 'Ответ:',self.n1//self.n2
        else:
            return 'ERROR'
par = kalkul(n1,n2,zn)
print(kalkul.ingeneer(par))
