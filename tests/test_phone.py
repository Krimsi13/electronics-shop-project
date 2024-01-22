from src.phone import Phone
import pytest

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_case1():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
    with pytest.raises(ValueError):
        phone1.number_of_sim = 2.0
