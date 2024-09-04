from random import randint

def cost_of_ringing_per_day_of_the_week(day,cost):
    if day in [6, 7]:
        cost *= 0.8
        print('Скидка 20% т.к. выходной день')
    else:
        print('Будний день, скидки нет')
    return cost

def check_variable(a,b):
    """
    до сих пор ни кто не знает какой знак у нуля)))
    по этому не ясно, что делать выводить разность или произведение
    уточните этот момент
    предлагаю два варинта с нулем, либо пляшем от знака второй переменной
    либо обрабатываем нуль отьдельно
    """
    # if a >= 0 and b >= 0: return a - b
    # if a <= 0 and b <= 0: return a * b
    # if a * b < 0: return a + b

    if a == 0 or b == 0: return "0 не предусмотрен в ТЗ"
    if a > 0 and b > 0: return a - b
    if a < 0 and b < 0: return a * b
    if a * b < 0: return a + b

def is_it_raining():
    first_question = input('Is it raining? ').lower()
    if first_question == 'yes':
        second_question = input('Is it windy? ').lower()
        if second_question == 'yes':
            return 'It is too windy for an umbrella'
        else:
            return 'Take an umbrella'
    else:
        return 'Enjoy your day'




if __name__ == '__main__':
    # day = int(input('Введите день недели: '))
    # cost = float(input('Введите стоимость звонка: '))
    # print(cost_of_ringing_per_day_of_the_week(day,cost))
    for i in range(10):
        day = randint(1, 7)
        cost = 20
        print(cost_of_ringing_per_day_of_the_week(day,cost))

    for i in range(10):
        a = randint(-10, 10)
        b = randint(-10, 10)
        print(check_variable(a,b))

    print(is_it_raining())