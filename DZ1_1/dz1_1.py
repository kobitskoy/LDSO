def print_words_on_new_line(str):
    """
    Решениe задачи для общего случая, лень ставить \n
    """
    words = str.split()
    for word in words:
        print(word)

def if_evennumber(num):
    """
    Пользуемся тем, что у четных остаток от деления 0
    """
    print(not bool(num%2))

def calculate_age(birth_year):
    """
    Без комментариев
    """
    current_year = 2024
    return current_year - birth_year

if __name__ == '__main__':
    print_words_on_new_line("Silence is golden")
    if_evennumber(41)
    if_evennumber(50)
    birth_year = int(input("Enter your birth year: "))
    print("Your age is:", calculate_age(birth_year))
