import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_initial_keyboard(keyboard1):
    assert str(keyboard1) == "Dark Project KD87A"
    assert str(keyboard1.language) == "EN"


def test_change_lang(keyboard1):
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "EN"


def test_language(keyboard1):
    with pytest.raises(AttributeError):
        keyboard1.language = 'CH'
