import random
from dataclasses import dataclass

from .meals import Meals


@dataclass
class Planner:
    meals: Meals

    def generate_meal_plan(self, num_days: int):
        for _ in range(num_days):

            meal = random.choice(self.meals.meal_list)
            print(meal.name)
