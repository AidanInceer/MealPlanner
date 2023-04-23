import random
from dataclasses import dataclass

from .meals import Meals


@dataclass
class Planner:
    meals: Meals
    num_days: int

    def generate_meal_plan(self):
        planned_meals = []
        for index in range(self.num_days):
            planned_meal = self.select_meal(index, self.meals.meal_list, planned_meals)
            planned_meals.append(planned_meal)

        return planned_meals

    def select_meal(self, index: int, meals_list: list, planned_meals: list):
        planned_meal = random.choice(meals_list)
        portion_flag = True if planned_meal.portion == 2 else False
        if index in [0, 1]:
            pass
        elif (portion_flag) and (planned_meals[index - 1] != planned_meals[index - 2]):
            planned_meal = planned_meals[index - 1]

        if planned_meals.count(planned_meal) > 3:
            planned_meal = random.choice(meals_list)

        return planned_meal
