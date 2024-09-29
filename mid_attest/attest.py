def solve_quadratic(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return 'Корней нет'
    elif d == 0:
        try:
            return f'Корень один: {round(-b / (2*a),5)}'
        except ZeroDivisionError:
            return 'Деление на 0'
    else:
        try:
            x1 = (-b - d**0.5) / (2*a)
            x2 = (-b + d**0.5) / (2*a)
            return f'x1 = {round(x1,5)}, x2 = {round(x2,5)}'
        except ZeroDivisionError:
            return 'Это не квадратное уравнение, т.к. а = 0'
if __name__ == '__main__':
    try:
        a,b,c = map(float, input('Введите коэффициент a, b, c через пробел: ').replace(',', '.') .split())
        print(solve_quadratic(a, b, c))
    except ValueError:
        print('Введены некорректные данные')



