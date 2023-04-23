from dataclasses import dataclass
from typing import List

from .ingredients import Ingredient


@dataclass
class Meal:
    name: str
    ingredients: List[Ingredient]
    portion: int


@dataclass
class Meals:
    meal_list: List[Meal]

    def add_meal(self):
        pass

    def remove_meal(self):
        pass


# add comment
