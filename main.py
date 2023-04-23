from src.core.ingredients import Ingredient
from src.core.meals import Meal, Meals
from src.core.planner import Planner
from src.utils.config import Config
from src.utils.sql_utils import SQLManager

if __name__ == "__main__":
    conf = Config()
    config = conf.create_config()
    sql_Manager = SQLManager()
    conn = sql_Manager.create_db(config["db_path"])

    # Create/Update/Delete Meals:
    meal_input = input("Would you like to 'Add'/'Update'/'Delete' meals or 'skip': ")
    if meal_input is True:
        print("ing add update")

    # Plan meals
    # read meals from meal DB
    # meals = Meals(1, 2, 3, 4, 5, 6)
    # planner = Planner(meals, 7)
    # planned_meals = planner.generate_meal_plan()

    # # Display "Read" planned meals to user
    # for planned_meal in planned_meals:
    #     print(planned_meal.name)
