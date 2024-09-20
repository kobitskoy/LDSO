# users_name = {'user1': '5', 'user2': '2', 'user3': '15'}
# print(users_name)
# my_dict = users_name.copy()
# dict_sorted_by_key = sorted(users_name.items(), key=lambda x: x[0])
# dict_sorted_by_value = sorted(users_name.items(), key=lambda x: x[1])

# Есть товар каталога(id,title,price)
# Есть товар корзины (id,count)



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
    title = input("Введите название товара")
    price = int(input("Введите стоимость товара"))
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
            item['price'] = int(input(f"Введите цену для {item['title']}\n"))
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


while True:
    choise = input('Выберите пункт меню:\n1) Показать каталог товаров'
                   '\n2) Добавить товар в каталог товаров'
                   '\n2.1) Редактировать стоимость товара'
                   '\n2.2) Удалить товар'
                   '\n3) Добавить товар в корзину покупок'
                   '\n4) Вывести корзину покупок'
                   '\n5) Выход\n').strip()