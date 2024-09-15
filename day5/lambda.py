# # check = (lambda x: not x%2)
# # print(check(3))
# # add = lambda x, y: x + y
# # sub = lambda x, y: x - y
# # mult = lambda x, y: x * y
# # div = lambda x, y: x / y if y != 0 else "Ошибка: деление на ноль"
# #
# # print(add(5, 3))
# # print(sub(10, 4))
# # print(mult(2, 6))
# # print(div(15, 3))
# # print(div(15, 0))
# #
# # calc = lambda f, x, y: eval(str(x) + f + str(y)) if not(y == 0 and f == '/') else "Ошибка: деление на ноль"
# # print(calc('*', 1, 0))
# # print(calc('+', 1, 0))
# # print(calc('-', 1, 0))
# # print(calc('/', 1, 0))
# #
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
# def negative_degree(a,n):
#     if n == 0:
#         return 1
#     else:
#         return 1/a * negative_degree(a,n+1)
# print(negative_degree(2,-5))
#
# def fibonacci(n):
#     if n in (1,2):
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(6))
#
#
# print(list(range(1,3)).)
from random import randint
q =[]
while 1:
    if len(q) <= 5:
        q.append(randint(1,100))
    else:
        print(f'Входите {q.pop(0)}')
        print(f'Готовьтесь {q(0)}')
        q.append(randint(1,100))
