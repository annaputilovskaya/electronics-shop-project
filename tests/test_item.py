import pytest

from src.item import Item


@pytest.fixture
def items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_repr(items):
    assert repr(items[0]) == "Item('Смартфон', 10000, 20)"


def test_str(items):
    assert str(items[0]) == 'Смартфон'


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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_string_to_number_not_number():
    with pytest.raises(ValueError):
        Item.string_to_number('')


def test_instantiate_from_csv():
    Item.instantiate_from_csv('electronics-shop-project/src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
