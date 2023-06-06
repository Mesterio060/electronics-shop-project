import csv
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        calculate_total_price = self.price * self.quantity
        return calculate_total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname):
        try:
            if len(newname) <= 10:
                self._name = newname
        except Exception:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        cls.all = []
        with open('C:/Users/79538/PycharmProjects/electronics-shop-project/src/items.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = Item(name, price, quantity)
                cls.all.append(item)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса Item
        """
        return f"Item(name='{self._name}', price='{self.price}', quantity='{self.quantity}')"

    @staticmethod
    def string_to_number(num):
        number = int(math.floor(float(num.strip())))
        return number
