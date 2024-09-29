# users_name = {'user1': '5', 'user2': '2', 'user3': '15'}
# print(users_name)
# my_dict = users_name.copy()
# dict_sorted_by_key = sorted(users_name.items(), key=lambda x: x[0])
# dict_sorted_by_value = sorted(users_name.items(), key=lambda x: x[1])

# Есть товар каталога(id,title,price)
# Есть товар корзины (id,count)
#gerasimenkosv@bk.ru



users = [
    {
        'id':1,
        'login':'admin',
        'password':'12345'
    },
    {
        'id':2,
        'login':'test',
        'password':'54321'
    }
]
# Структура товара в корзине:
# id,count
carts = []

items = [
    {
        'id':1,
        'title':'Audi',
        'price':1000
    },
    {
        'id':2,
        'title':'BMW',
        'price':1200
    },
    {
        'id':3,
        'title':'VW',
        'price':900
    }
]
def show_items():
    print("-"*50)
    for i,item in enumerate(items,1):
        print(f"{i}) {item['title']} стоит {item['price']} (id = {item['id']})")
    print("-"*50)
def get_max_id():
    max_id = 0
    for item in items:
        if item['id'] > max_id:
            max_id = item['id']
    return max_id
def add_item():
    title = input("Введите название товара: ")
    price = int(input("Введите стоимость товара: "))
    item = {
        'title':title,
        'price':price,
        'id':get_max_id() + 1
    }
    items.append(item)
    show_items()
def edit_price_from_item(id):
    for item in items:
        if item['id'] == id:
            item['price'] = int(input(f"Введите цену для {item['title']}: \n"))
            break
    show_items()
def del_item(id):
    for i,item in enumerate(items):
        if item['id'] == id:
           print(f"Товар {items.pop(i)['title']} был удален!")
           show_items()
           break
    else:
        print("Товар не найден")
def show_cart():
    print("-" * 50)
    if carts:
        print('В корзине: ')
        for item in carts:
            for i in items:
                if item['id'] == i['id']:
                    print(f"ID: {item['id']} {i['title']} {item['count']} шт")
    else:
        print('Корзина пуста')
    print("-" * 50)
def add_carts():
    item_id = int(input('Введите ID товара, который нужно добавить в корзину: '))
    for item in items:
        if item['id'] == item_id:
            count = int(input('Введите кол-во товара: '))
            carts.append({'id':item_id, 'count':count })
            break
    print(f"Товар с ID: {item_id} не найден")
    show_cart()
def auth_users():
    while 1:
        auth = input('Введите логин или нажмите Enter для покупок: ').strip().lower()
        if auth:
            for user in users:
                if user['login'] == auth:
                    passwd = input('Введите пароль: ').strip().lower()
                    if user['password'] == passwd:
                        print('Вы вошли как', user['login'])
                        return 'admin'
                    else:
                        print('Неверный пароль')
                        return
            print('Пользователь не найден')
        else:
            print('Вы вошли как покупатель')
            return 'buyer'

admin_menu = """
Выберите пункт меню:
    1) Показать каталог товаров
    2) Добавить товар в каталог товаров
    2.1) Редактировать стоимость товара
    2.2) Удалить товар
    3) Добавить товар в корзину покупок
    4) Вывести корзину покупок
    5) Выход
"""
main_menu = """
Выберите пункт меню:
    1) Показать каталог товаров
    2) Добавить товар в корзину покупок
    3) Вывести корзину покупок
    4) Выход
    """
def admin_match():
    while 1:
        choise = input(admin_menu).strip()
        match choise:
            case "1":
                show_items()
            case "2":
                add_item()
            case "2.1":
                edit_price_from_item(int(input('Введите ID товара, который нужно изменить')))
            case "2.2":
                del_item(int(input('Введите ID товара, который нужно удалить')))
            case "3":
                add_carts()
            case "4":
                show_cart()
            case "5":
                break
def user_match():
    while 1:
        choise = input(main_menu).strip()
        match choise:
            case "1":
                show_items()
            case "2":
                add_carts()
            case "3":
                show_cart()
            case "4":
                break
def main_store(user):
    match user:
        case 'admin':
            admin_match()
        case 'buyer':
            user_match()
if __name__ == '__main__':
    while 1:
        is_auth = auth_users()
        if is_auth == 'admin' or is_auth == 'buyer':
            main_store(is_auth)
            break




    #
    # if choise == "1":
    #     show_items()
    # elif choise == "2":
    #     add_item()
    # elif choise == "2.1":
    #     edit_price_from_item(int(input('Введите ID товара, который нужно изменить')))
    # elif choise == "2.2":
    #     del_item(int(input('Введите ID товара, который нужно удалить')))
    # elif choise == "5":
    #     break
