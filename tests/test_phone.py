import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test_initial(phone1):
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_incorrect_number_of_sim_not_positive():
    with pytest.raises(ValueError):
        Phone.incorrect_number_of_sim(0)


def test_incorrect_number_of_sim_float():
    with pytest.raises(ValueError):
        Phone.incorrect_number_of_sim(2.5)


def test_number_of_sim(phone1):
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
