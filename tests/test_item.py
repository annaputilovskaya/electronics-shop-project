from src.item import Item

item1 = Item('milk', 119.5, 10)
item2 = Item('bread', 60.5, 20)


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 1195.0
    assert Item.calculate_total_price(item2) == 1210.0


def test_apply_discount():
    Item.pay_rate -= 0.1
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 107.55
    assert item2.price == 54.45
