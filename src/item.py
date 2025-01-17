import csv
import os.path


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.9
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и наследников.')
        return int(self.quantity) + int(other.quantity)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        cls.all.clear()
        if not os.path.exists(csvfile):
            raise FileNotFoundError(f"_Отсутствует данный файл_")

        with open(csvfile, newline='', encoding="windows-1251") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if len(row) != 3:
                    raise InstantiateCSVError(f"_Данный файл поврежден_")
                cls(row['name'], row['price'], row['quantity'])
        # except FileNotFoundError:
        #     print(f"_Отсутствует данный файл_")

    @staticmethod
    def string_to_number(string_int: str) -> int:
        return int(float(string_int))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name[:10]
