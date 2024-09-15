from datetime import datetime
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calc_factorial():
    return factorial(3)*(factorial(8)+factorial(4))

def check_age(age):
    if age % 10 == 1:
        return f'Вам {age} год'
    elif 1 < age % 10 < 5:
        return f'Вам {age} года'
    else:
        return f'Вам {age} лет'

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f'{check_age(age)}, до пенсии {check_age(65- age)}')
    return age

if __name__ == '__main__':
    print(f'3!*(8!+4!) = {calc_factorial()}')
    calculate_age(int(input('Введите год рождения: ')))
    calculate_age(1984)
    calculate_age(1983)
    calculate_age(1982)