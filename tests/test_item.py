"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_Item():
    test_item3 = Item("Смартфон", 50000, 30)

    assert test_item3.name == "Смартфон"
    assert test_item3.price == 50000
    assert test_item3.quantity == 30


def test_calculate_total_price():
    test_item3 = Item("Смартфон", 50000, 30)
    calculate_total_price = test_item3.price * test_item3.quantity

    assert calculate_total_price == 1500000


def test_apply_discount():
    test_item4 = Item("Смартфон", 50000, 30)
    test_item4.price = test_item4.price * Item.pay_rate

    assert test_item4.price == 50000.0