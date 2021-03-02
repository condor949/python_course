# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeEquipment:
    def __init__(self, model=None, lan_module=False):
        self.model = model
        self.lan_module = lan_module


class Printer(OfficeEquipment):
    def __init__(self, model=None, lan_module=False, double_sided_print=False, *args):
        self.double_sided_print = double_sided_print
        self.printable_formats = args
        OfficeEquipment.__init__(model,lan_module)

    def print(self):
        pass


class Scanner(OfficeEquipment):
    def __init__(self, model=None, lan_module=False, scan_speed=20):
        self.scan_speed = scan_speed
        OfficeEquipment.__init__(model,lan_module)

    def scan(self):
        pass


class Xerox(OfficeEquipment):
    def __init__(self, model=None, lan_module=False, double_sided_print=False):
        pass

    def fax(self):
        pass

