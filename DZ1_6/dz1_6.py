def sports():
    sport.append(input('Введите свой любимый вид спорта: ').capitalize())
    print(sorted(sport))

def print_learning():
    for i in sorted(school_learning):
        print(i, end=' ')
    print()

def remove_learning():
    """
    т.к. в задании сказано вывести список)))) а не list вывожу список человеческий)), просто люблю фишки  множеств
    """

    remove = input('Введите через зяпатую предметы которые хотите удалить: ').title()
    remove = remove.replace(' ','')
    return set(remove.split(','))

if __name__ == '__main__':
    sport = ['Бокс', 'Теннис']
    school_learning = ['Математика', 'Физика', 'Химия', 'Информатика', 'Философия', 'История']
    sports()
    print_learning()
    school_learning = set(school_learning) - remove_learning()
    print_learning()

