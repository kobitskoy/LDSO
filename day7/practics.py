#1
import math
from random import random, randint


def split_users_fio(fio):
    return f'Фамилия: {fio.split()[0]}\nИмя: {fio.split()[1]}\nОтчество: {fio.split()[2]}'
#2

def logistic(box):
    truck = 0
    container = 0
    konteyner_need = math.ceil(box / 28)
    gruzpvik_need = math.ceil(konteyner_need / 12)
    print(f'Для перевозки {box} потребуется грузовиков: {gruzpvik_need}, контейнеров: {konteyner_need}')
    for i in range(1, box + 1):
        if container % 12 == 0:
            truck += 1
            print(f'Грузовик: {truck}')
        if i % 28 == 0:
            container += 1
            print(f'    Контейнер: {container}')
        print(f'        Ящик: {i}')

    # box = 0
    # con = 0
    # truck = 0
    # gruzpvik = 12*27
    # konteyner = 27
    # gruzpvik_need = math.ceil(korob / gruzpvik)
    # konteyner_need = math.ceil(korob / konteyner )
    # print(f'Для перевозки {korob} потребуется грузовиков: {gruzpvik_need}, контейнеров: {konteyner_need}')
    # for i in range(1, gruzpvik_need+1):
    #     if box == korob:
    #         print()
    #         break
    #
    #     truck += 1
    #     print()
    #     print(f'Грузовик {i}')
    #
    #
    #     for j in range(1, 13):
    #         if box == korob:
    #             print()
    #             break
    #
    #         con += 1
    #         print()
    #         print(f'    Контейнер {con}')
    #
    #         for k in range(1, 29):
    #             if box == korob:
    #                 break
    #             box += 1
    #             print(f'        Ящик {box}', end=' ')



#3
def numbers ():
    numbers = [randint(100, 999) for i in range(4)]
    for num in numbers:
        print(num)
    user_number = int(input('Введите 3х значное число: '))
    if user_number in numbers:
        print('Вы ввели число, его позиция: ', numbers.index(user_number)+1)
    else:
        print('число отсутствует в списке')
#4
def guests():
    guests = []
    for i in range(3):
        guest = input('Введите имя гостя: ')
        guests.append(guest.title())
    if input('Хотите добавить гостя в список? ').title() == 'Да':
        while 1:
            guest= input('Введите имя гостя или "стоп" чтоб закончить: ').title()
            if guest.title() == 'Стоп':
                break
            if guest in guests:
                print('Гость уже есть в списке')
            else:
                guests.append(guest)
    return guests
#5
def tv_program():
    list_tv_program = ['Первая программа', 'Вторая программа', 'Третья программа', 'Четвертая программа']
    for program in list_tv_program:
        print(program)
    new_program = input('Введите новую программу: ').title()
    program_index = int(input('Введите позицую в списке: '))
    list_tv_program.insert(program_index-1, new_program)
    print(list_tv_program)
if __name__ == '__main__':

  # print(split_users_fio(input('Введите ФИО: ').title()))
   logistic(int(input('Введите кол-во ящиков: ')))
   #numbers()
   #print(guests())
   #tv_program()
