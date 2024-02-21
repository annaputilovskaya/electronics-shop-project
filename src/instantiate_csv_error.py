class InstantiateCSVError(Exception):
    """
    Класс для исключения при поврежденном файле
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация объекта класса InstantiateCSVError
        """
        self.message = args[0] if args else 'Файл поврежден'

    def __str__(self):
        """
        Отображает информацию об объекте класса InstantiateCSVError для пользователей
        """
        return self.message
