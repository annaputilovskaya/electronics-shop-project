from src.instantiate_csv_error import InstantiateCSVError


def test_str_instantiate_csv_error():
    exception1 = InstantiateCSVError()
    assert str(exception1) == 'Файл поврежден'

    exception2 = InstantiateCSVError('Иное описание')
    assert str(exception2) == 'Иное описание'
