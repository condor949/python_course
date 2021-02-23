# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).



class Worker:
    name = ""
    surname = ""

    class Position:
        def get_full_name(self, *args):
            return args[0]+args[1]
        def get_total_income(self, *args):
            return sum(args)

    position = Position()
    __income = {"wage":0, "bonus":0}

    def __init__(self, name, surname, *kwargs):
        self.name = name
        self.surname = surname
        self.__income = kwargs


