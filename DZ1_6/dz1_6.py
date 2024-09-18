# sport = ['Бокс', 'Теннис']
# sport.append(input('Введите свой любимый вид спорта: ').capitalize())
# print(sorted(sport))
from pprint import pprint

school_learning = ['Математика','Физика','Химия','Информатика','Философия','История']
def print_learning():
    for i in sorted(school_learning):
        print(i, end=' ')
    print()

def remove_learning():
    remove = input('Введите через зяпатую предметы которые хотите удалить: ').title()
    remove = remove.replace(' ','')
    return set(remove.split(','))

if __name__ == '__main__':
    print_learning()
    school_learning = set(school_learning) - remove_learning()
    print_learning()

