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
import unittest


class TrafficLight:
    __colors = cycle((str, timer) for str, timer in {'red': 7, 'yellow': 2, 'green': 10}.items())
    cur_color = None

    def running(self):
        tmp = next(TrafficLight.__colors)
        print(tmp[0])
        return tmp

def destroy_TrafficLight_make_chaos_AHAHAHAH():
    next(TrafficLight._TrafficLight__colors)


class TestTrafficLight(unittest.TestCase):

    def test_color(self):
        t = Timer(20.0, destroy_TrafficLight_make_chaos_AHAHAHAH)
        t.start()
        tl = TrafficLight()
        for _ in range(15):
            color, timer = tl.running()
            sleep(timer)
            self.assertEqual(color, TrafficLight.cur_color, "something wrong")


if __name__ == '__main__':
    unittest.main()
