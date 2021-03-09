# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
class Storage:
    def __init__(self):
        self.items_dict = {}
        self.subdivision_list = []

    def move_to_storage(self, item, quantity):
        self.items_dict[item] = quantity

    def move_to_subdivision(self):
        pass
