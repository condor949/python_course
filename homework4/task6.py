# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle


def iter_a(x):
    if x > 10:
        print('Enter less value')
    else:
        for i in count(x):
            print(i, end=' ')
            if i > 9:
                break


def iter_b():
    R = ['Du', 'Du hast', 'Du hast mich']
    i = 0
    for x in cycle(R):
        print(x)
        i += 1
        if i > 5:
            break


def main():
    iter_a(int(input('Enter number less then 10: ')))
    print()
    iter_b()


if __name__ == '__main__':
    main()
