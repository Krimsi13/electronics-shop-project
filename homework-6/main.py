from src.item import Item
from config import ROOT_DIR
import os.path

DATA_DIR = os.path.join(ROOT_DIR, "src", "item.csv")
DATA_DIR_2 = os.path.join(ROOT_DIR, "src", "items_2.csv")

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(DATA_DIR)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(DATA_DIR_2)
    # InstantiateCSVError: Файл item.csv поврежден
