import math, sys, time
from random import randint

'''
код делется специально для прораммы ... , которую делаем на чистом интузиазме,(школьный проект)
'''
def summ(repeat):
    ans=0
    for i in range(repeat):
        a=randint(1,100)
        b=randint(1,100)
        c=a+b
        decision=int(input('{0}+{1}='.format(a,b)))
        if c==decision:
            print('Верно, ответ равен {0}'.format(c))
            ans+=1
        else:
            print('Неправильно, ответ равен {0}'.format(c))
    print('правильных ответов {0} из {1}'.format(ans, repeat))


def subt(repeat):
    ans = 0
    for i in range(repeat):
        a = randint(1, 100)
        b = randint(1, 100)
        c = a - b
        decision = int(input('{0}-{1}='.format(a, b)))
        if c == decision:
            print('Верно, ответ равен {0}'.format(c))
            ans += 1
        else:
            print('Неправильно, ответ равен {0}'.format(c))


def mult(repeat):
    ans = 0
    for i in range(repeat):
        a = randint(1, 100)
        b = randint(1, 100)
        c = a * b
        decision = int(input('{0}x{1}='.format(a, b)))
        if c == decision:
            print('Верно, ответ равен {0}'.format(c))
            ans += 1
        else:
            print('Неправильно, ответ равен {0}'.format(c))
    print('правильных ответов {0} из {1}'.format(ans, repeat))


def divi(repeat):
    ans = 0
    print('выберите ')
    a=int(input(''))
    for i in range(repeat):
        a = randint(1, 100)
        b = randint(1, 100)
        c = a / b

        decision = int(input('{0}:{1}='.format(a, b)))
        if c == decision:
            print('Верно, ответ равен {0}'.format(c))
            ans += 1
        else:
            print('Неправильно, ответ равен {0}'.format(c))
    print('правильных ответов {0} из {1}'.format(ans, repeat))

#############################################################################

print('выберите вариант примеров')
option=int(input('1 - сложение\n2 - вычитание\n3 - умножение\n5 - деление\n ваш выбор - '))
repeat=int(input('введите колл-во примеров - '))

def menu():
    if option == 1:
        summ(repeat)
    elif option == 2:
        subt(repeat)
    elif option == 3:
        mult(repeat)
    elif option == 4:
        divi(repeat)
