# Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
# и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NotDigit(ValueError):
    def __init__(self, value):
        self.value = value


class DigitCheck:
    @classmethod
    def check(cls, str):
        try:
            return int(str)
        except ValueError:
            raise NotDigit("Input value does not consist only of numbers")


def main():
    print('Enter stop to exit program')
    val_checker = DigitCheck()
    input_str = None
    numberlist = []
    while input_str != 'stop':
        input_str = input("Enter number: ")
        try:
            numberlist.append(val_checker.check(input_str))
        except NotDigit as nd:
            print(nd.value)
    print(numberlist)


if __name__ == '__main__':
    main()

