import datetime
import random

def randomListItem(l):
    return l[random.randint(0, len(l)-1)]

def randomTime(n):
    # Задайте начальную и конечную даты в интервале
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 12, 31)

    # Генерируйте случайное время между начальной и конечной датами
    random_time = start_date + (end_date - start_date) * random.random()

    return random_time

# Функция для генерации случайного названия на русском языке
def generate_random_name(length):
    russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return (random.choice(russian_letters).upper())+"".join(random.choice(russian_letters) for _ in range(length))

def generate_n_digit_number(n):
    # Генерируем число с n цифрами
    return random.randint(10**(n-1), 10**n - 1)
