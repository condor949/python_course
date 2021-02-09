# * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#   (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#   “название”: [“компьютер”, “принтер”, “сканер”],
#   “цена”: [20000, 6000, 2000],
#   “количество”: [5, 2, 7],
#   “ед”: [“шт.”]
# }

import keyboard

selected = 1


def show_menu():
    global selected
    print("\n" * 30)
    print("Choose an option:")
    for i in range(1, 5):
        print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))


def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()


def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()


show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.wait()
# def input_string_val():
#     return input('Enter string title')
#
#
# def input_number_val():
#     num = ''
#     while type(num) != int:
#         try:
#             num = int(input('Enter correct quantity'))
#             if num < 0:
#                 num = ''
#                 continue
#             return num
#         except ValueError:
#             num = ''
#
#
# item_dict = {'name': None,
#              'costs': None,
#              'quantity': None,
#              'units': None}
#
# items = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#          (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#          (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
# count = 1
# stat = {}
#
# _, test_dict = items[0]
#
# for key in test_dict.keys():
#     stat[key] = []
# #slow
# # for _,dict in items:
# #   for key in stat.keys():
# #     if (stat[key].count(dict[key]) == 0):
# #       stat[key].append(dict[key])
#
# #faster
# for _, dict in items:
#     for key, value in stat.items():
#         temp = dict[key]
#         if value.count(temp) == 0:
#             value.append(temp)
#
# print(stat)
