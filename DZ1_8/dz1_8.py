import re
def check_ip(i):
    regex_ip = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ip_addr = ['10.10.10.10','192.167.1.1','123.s21.12.12']
    for ip in ip_addr:
        if re.match(regex_ip, ip):
            print('IP address is valid')
        else:
            print('IP address is invalid')

items = [
    {'name': 'Термос', 'weight': 2},
    {'name': 'Палатка', 'weight': 5},
    {'name': 'Спальный мешок', 'weight': 3},
    {'name': 'Еда', 'weight': 4},
    {'name': 'Одежда', 'weight': 6},
]
def show_items(items):
    for item in items:
        print(f'{item["name"]} - {item["weight"]} кг')

if __name__ == '__main__':

    max_weight = 10
    total_weight = 0
    edit_bag = None
    items_names = [i['name'] for i in items]
    bag = []
    show_items(items)

    while total_weight < max_weight:
        """
        считаю, что если свободного места в рюкзаке не осталось, то он автоматически сохрнаняется
        т.к. это не оговорено в ТЗ
        """
        if edit_bag == 'Нет':
            print('Вещи в рюкзаке:')
            show_items(bag)
            break
        add_item = input('Введите название вещи для добавления: ').capitalize()
        if add_item not in items_names:
            print(f'{add_item} нет в списке вещей')
            continue

        for item in items:
            if item['name'] == add_item:
                if item['weight'] <= max_weight - total_weight:
                    total_weight += item['weight']
                    bag.append(item)
                    print(f'Добавляем {item["name"]}, осталось {max_weight - total_weight} кг')
                else:
                    print(f'{item["name"]} не помещается, необходимый вес {item["weight"]}, доступно {max_weight - total_weight} кг')
                    edit_bag = input(f'Желатете удалить вещь из рюкзака? Да/Нет: ').capitalize()
                    if edit_bag == 'Да':
                        remove_item = input('Введите название вещи для удаления: ').capitalize()
                        for i in bag:
                            if i['name'] == remove_item:
                                bag.remove(i)
                                total_weight -= i['weight']
                                print(f'Удаляем {i["name"]}, осталось {max_weight - total_weight} кг')
                                print('Вещи в рюкзаке:')
                                show_items(bag)
                                break

