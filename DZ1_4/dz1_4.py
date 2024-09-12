from random import randint
def get_middle(start,end):
    if start == end:
        return start
    else:
        sum = 0
        for i in range(start,end+1):
            sum += i
        return sum/(end-start+1)

def input_numbers(n):
    positive = negative = zero = 0
    for i in range(int(n)):
            #number = int(input('Введите вещественное число или ноль : '))
            number = randint(-1000,1000)
            print(number, end=' ')
            if number > 0:
                positive += 1
            elif number < 0:
                negative += 1
            elif number == 0:
                zero += 1
            else:
                print('Введено не число')
    print()
    return positive, negative, zero

def print_result(numbers):
    print(f'Количество положительных чисел: {numbers[0]}')
    print(f'Количество отрицательных чисел: {numbers[1]}')
    print(f'Количество нулей: {numbers[2]}')



if __name__ == '__main__':
    start = randint(1,10)
    end = randint(start,20)
    print(', '.join(str(i) for i in range(start,end+1)))
    print(get_middle(start,end))


    while 1:
        n = input('Введите количество чисел: ')
        if n.isdigit():
            numbers = input_numbers(n)
            print_result(numbers)
            break
        else:
            print('Введено не число. повторите ввод')

