from random import randint
def area_Of_A_Circle(radius): return 3.14 * radius * radius;
def volume_Of_A_Sphere(radius): return 4 / 3 * 3.14 * radius * radius* radius;
if __name__ == '__main__':
    radius = randint(1,10)
    area = area_Of_A_Circle(radius)
    volume = volume_Of_A_Sphere(radius)
    print(f'При радиусе {radius} \n'
          f'Объем сферы равен {volume}\n'
          f'площадь круга равна {area}\n'
          f'Объем сферы больше площади круга в',volume/area, 'раз')
