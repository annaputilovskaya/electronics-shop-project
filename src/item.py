from csv import DictReader
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        """
        Инициализирует экземпляры класса `Item` данными из файла
        :param csvfile: файл .csv с данными о товарах
        :return: None
        """
        path = os.path.join('../', csvfile)
        Item.all.clear()
        with open(path, newline='', encoding='windows-1251') as file:
            reader = DictReader(file)
            for dictionary in reader:
                cls(dictionary['name'], dictionary['price'], dictionary['quantity'])

    @staticmethod
    def string_to_number(string) -> int:
        """
        Возвращает число из числа-строки
        :param string: строка
        :return: число
        """
        return int(float(string))
