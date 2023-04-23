from src.core.ingredients import Ingredient
from src.core.meals import Meal, Meals
from src.core.planner import Planner

if __name__ == "__main__":
    i1 = Ingredient(name="Cheese", amount=1.0, unit="gram")
    i2 = Ingredient(name="Bacon", amount=1.0, unit="gram")
    i3 = Ingredient(name="Bread", amount=1.0, unit="gram")
    i4 = Ingredient(name="Bread", amount=1.0, unit="gram")
    i5 = Ingredient(name="Bread", amount=1.0, unit="gram")
    i6 = Ingredient(name="Bread", amount=1.0, unit="gram")
    i7 = Ingredient(name="Bread", amount=1.0, unit="gram")

    m1 = Meal("Frozen Pizza", ingredients=[i1, i2, i4], portion=[4])
    m2 = Meal("Stuffed Pasta", ingredients=[i6, i2, i3], portion=[4])
    m3 = Meal("Burger", ingredients=[i1, i4, i5], portion=[4])
    m4 = Meal("Stir Fry", ingredients=[i1, i2, i3], portion=[4])
    m5 = Meal("Bolognase", ingredients=[i1, i4, i5], portion=[4])
    m6 = Meal("Chicken Wraps", ingredients=[i6, i5, i7], portion=[4])
    m7 = Meal("Parma Ham Pasta", ingredients=[i2, i4, i5], portion=[4])
    m8 = Meal("Teriaki Salmon", ingredients=[i1, i4, i3], portion=[4])

    meals = Meals(meal_list=[m1, m2, m3, m4, m5, m6, m7])

    planner = Planner(meals, 7)
    meals = planner.generate_meal_plan()

    for m in meals:
        print(m.name)
