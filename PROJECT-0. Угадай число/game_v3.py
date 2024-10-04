"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def half_division_method(number):
    """ Устанавливаем любое random число, а потом методом деления отрезка пополам ищет загаданное число.
        Функция принимает загаданное число и возвращает число попыток """
    count = 1
    predict = np.random.randint(1, 101)
    right = 100
    left = 1
    while number != predict:
        count += 1
        if number > predict:
            right = number
            number = (left+right)//2
        elif number < predict:
            left = number
            number = (left + right)//2 + 1
    return count  # выход из цикла, если угадали


def score_game(half_division_method) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        half_division_method ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(half_division_method(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(half_division_method)