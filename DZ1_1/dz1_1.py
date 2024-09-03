def print_words_on_new_line(usr_str):
    """
    Решениe задачи для общего случая, лень ставить \n
    """
    # for word in usr_str.split():
    #     print(word)
    print('\n'.join(map(str,usr_str.split())))

def if_evennumber(num):
    """
    Пользуемся тем, что у четных остаток от деления 0
    """
    print(not bool(num%2))

def calculate_age(birth_year):
    """18
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
