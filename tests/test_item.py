"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


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


def test_name():
    Item.name = 'Игра-Кот'
    assert Item.name == 'Игра-Кот'


@pytest.fixture
def item():
    Item.all = []
    item = Item(name="Игра-Динозавр", price=1200, quantity=25)
    return item


def test_all_items_list(item):
    assert len(Item.all) == 1
    assert Item.all[0] == item


def test_len_name(item):
    with pytest.raises(Exception) as e:
        item.name = "Игра-Динозавр"
        assert str(e.value) == "Длина наименования товара превышает 10 символов"


def test_len_name2(item):
    item.name = "Телевизор"
    assert item.name == "Телевизор"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


def test_repr_and_str(item):
    # Создаем экземпляр класса для проверки магических методов
    item = Item("Телевизор", 45000, 12)

    # Проверяем магический метод __repr__
    assert repr(item) == "Item('Телевизор', 45000, 12)"

    # Проверяем магический метод __str__
    assert str(item) == 'Телевизор'


def test_Phone():

    # Проверяем новый класс
    phone1 = Phone("iPhone 14", 120000, 12, 2)
    # Проверяем методы
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 12, 2)"
    assert phone1.number_of_sim == 2

    # Еще один класс для проверки
    item1 = Item("Смартфон", 10000, 10)
    # Проверяем сложение - правильно
    assert item1 + phone1 == 22
    # Проверяем сложение - нельзя складывать
    assert phone1 + phone1 == 24

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

