# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle
from threading import Timer


def destroy_TrafficLight_make_chaos_AHAHAHAH():
    next(TrafficLight._TrafficLight__colors)


class TrafficLight:
    __colors = cycle((str, timer) for str, timer in {'red': 7, 'yellow': 2, 'green': 10}.items())
    __cur_color = None

    def running(self):
        tmp = next(TrafficLight.__colors)
        TrafficLight.__cur_color = tmp[0]
        return tmp

    def check_light_color(self, color):
        if color != TrafficLight.__cur_color:
            print("""Скользкие улицы,
                    Иномарки целуются,
                    Помятые крылья
                    Несчастной любви...""")
            exit(1)
        else:
            print("Without accidents")


def main():
    t = Timer(10.0, destroy_TrafficLight_make_chaos_AHAHAHAH)
    t.start()
    tl = TrafficLight()
    while True:
        color, timer = tl.running()
        sleep(timer)
        tl.check_light_color(color)
        print(color)


if __name__ == '__main__':
    main()
