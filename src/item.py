from csv import DictReader
import os

from src.instantiate_csv_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """
        Отображает информацию об объекте класса Item для отладки
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Отображает информацию об объекте класса Item для пользователей
        """
        return f'{self.__name}'

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
        filename = csvfile.split('/')[-1]
        Item.all.clear()

        if os.path.exists(path):
            with open(path, newline='', encoding='windows-1251') as file:
                reader = DictReader(file)
                for dictionary in reader:
                    name = dictionary.get('name')
                    price = dictionary.get('price')
                    quantity = dictionary.get('quantity')
                    for value in (name, price, quantity):
                        if value is None:
                            raise InstantiateCSVError(f"Файл {filename} поврежден")
                    else:
                        try:
                            cls(name, float(price), Item.string_to_number(quantity))
                        except TypeError:
                            raise InstantiateCSVError(f"Файл {filename} поврежден")
        else:
            raise FileNotFoundError('Отсутствует файл items.csv')
    @staticmethod
    def string_to_number(string) -> int:
        """
        Возвращает число из числа-строки
        :param string: строка
        :return: число
        """
        return int(float(string))

    def __add__(self, other):
        """
        Складывает по количеству товары в магазине
        :param other: Другой вид товара
        :return: Количество складываемых товаров
        """
        if not isinstance(other, Item):
            raise TypeError("Сложение данных объектов невозможно")
        return self.quantity + other.quantity
