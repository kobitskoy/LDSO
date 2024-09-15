from random import randint
result = 0
for i in range(5):
    a = randint(1,9)
    b = randint(1,9)
    num = int(input(f'Введите овтет {a} * {b} = '))
    if num == (a * b):
        result += 1
print('Зачтено') if result > 4 else print('Не зачтено')
