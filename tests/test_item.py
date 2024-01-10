"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Banana", 8.95, 4)


def test_case1():
    assert item1.calculate_total_price() == 35.8


def test_case2():
    item1.apply_discount()
    assert 8.95 * Item.pay_rate == item1.price
