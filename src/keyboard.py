from src.item import Item


class MixinLang:
    """
    Миксин-класс для хранению и изменения раскладки клавиатуры
    """
    def __init__(self):
        """Создание экземпляра класса MixinLang, по умолчанию язык английский"""
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Изменяет язык расклдаки клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLang):
    """
    Класс для клавиатур, продаваемых в магазине
    """
    def __init__(self, name, price, quantity):
        """
        :param name: Название клавиатуры.
        :param price: Цена за единицу.
        :param quantity: Количество клавиатур данного вида в магазине.
        """
        super().__init__(name, price, quantity)
