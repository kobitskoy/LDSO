# Вывести на экран все целые числа от 100 до 200 кратные 3 и посчитать сумму этих цифр
# Вывести все простые числа от 2 до 100 (дополнительное задание для
def sum_of_numbers(a,b):
    sum = 0
    for i in range(a,b):
        if i % 3 == 0:
            print(i, end=' ')
            sum += i
    print()
    return sum
def sum_of_numbers_optimized():
    """
    решение более оптимальное, но т.к. мы еще не учили range()
    """
    sum = 0
    for i in range(102,201,3):
        print(i, end=' ')
        sum += i
    print()
    return sum

def prime_numbers():
    """
    т.к. рассмотрен частный случай, нет особого смысла в оптимизации алгоритма
    """
    for i in range(2,101):
        if i % 2 == 0:
            continue
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
    print()

if __name__ == '__main__':
    print(sum_of_numbers(100,201))
    print(sum_of_numbers_optimized())
    prime_numbers()