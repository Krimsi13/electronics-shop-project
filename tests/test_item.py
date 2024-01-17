"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from config import ROOT_DIR
import os.path

DATA_DIR = os.path.join(ROOT_DIR, "src", "items.csv")

item1 = Item("Banana", 8.95, 4)


def test_case1():
    assert item1.calculate_total_price() == 35.8


def test_case2():
    item1.apply_discount()
    assert 8.95 * Item.pay_rate == item1.price


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_case3():
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_case4():
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(DATA_DIR)
    assert len(Item.all) == 5
    item2 = Item.all[0]
    assert item2.name == 'Смартфон'


def test_case5():
    item2 = Item("Смартфон", 10000, 20)
    assert repr(item2) == "Item('Смартфон', 10000, 20)"
    assert str(item2) == 'Смартфон'
