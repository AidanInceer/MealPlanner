from meal_planner.ingredients import Ingredient
from meal_planner.meals import Meal, Meals
from meal_planner.planner import Planner

if __name__ == "__main__":
    i1 = Ingredient(name="cheese", amount=1.0, unit="gram")
    i2 = Ingredient(name="cheese", amount=1.0, unit="gram")
    i3 = Ingredient(name="cheese", amount=1.0, unit="gram")

    m1 = Meal("Pizza", ingredients=[i1, i2, i3], portion=[4])
    m2 = Meal("Pasta", ingredients=[i1, i2, i3], portion=[4])
    m3 = Meal("Burger", ingredients=[i1, i2, i3], portion=[4])

    meals = Meals(meal_list=[m1, m2, m3])

    planner = Planner(meals)
    planner.generate_meal_plan(7)
