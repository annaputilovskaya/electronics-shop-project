from src.item import Item


class Phone(Item):
    """
    Класс для телефонов, продаваемых в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        Phone.incorrect_number_of_sim(self.__number_of_sim)

    def __repr__(self):
        """
        Отображает информацию об объекте класса Phone для отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @staticmethod
    def incorrect_number_of_sim(number_of_sim):
        """
        Выводит исключение, если переданное значение не является целым числом больше нуля
        """
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        Phone.incorrect_number_of_sim(number)
        self.__number_of_sim = number
