import pytest

from src.item import Item


@pytest.fixture
def items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(items):
    assert Item.calculate_total_price(items[0]) == 200000
    assert Item.calculate_total_price(items[1]) == 100000


def test_apply_discount(items):
    Item.pay_rate = 0.8
    items[0].apply_discount()
    assert items[0].price == 8000.0
    assert items[1].price == 20000


def test_name(items):
    assert items[0].name == 'Смартфон'
    items[0].name = 'Суперсмартфон'
    assert items[0].name == 'Суперсмарт'
    items[0].name = 'Смартфон'
    assert items[0].name == 'Смартфон'
