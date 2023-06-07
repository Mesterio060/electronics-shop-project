import csv
import math
import os


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

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Нельзя складывать')
        return int(self.quantity) + int(other.quantity)

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
        if len(newname) <= 10:
            self._name = newname
        else:
            raise Exception("Длина наименования товара больше 10 симвовов")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        cls.all = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data = os.path.join(current_dir, 'items.csv')
        with open(data, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num):
        number = int(math.floor(float(num.strip())))
        return number

    @name.setter
    def name(self, value):
        self._name = value
