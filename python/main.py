from decouple import config
from csv import DictReader
import psycopg2

postgres_credentials = {
    "host": config("HOST"),
    "database_name": config("DB_NAME"),
    "user": config("USUARIO"),
    "password": config("SENHA")
}

filename = "FastFoodNutritionMenu.csv"

with open(filename, "r") as file:
    dict_objs = DictReader(file)
    try:
        conn = psycopg2.connect(
            host=postgres_credentials["host"],
            database=postgres_credentials["database_name"],
            user=postgres_credentials["user"],
            password=postgres_credentials["password"],
            port="5432",
        )
        mycursor = conn.cursor()
        print("Conectado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

    for dicio in dict_objs:
        insert_query = f"""
            INSERT INTO fast_food_nutrition_menu("Company", "Item", "Calories", "CaloriesFromFat", "TotalFat(g)", "SaturatedFat(g)", "TransFat(g)", "Cholesterol(mg)", "Sodium(mg)", "Carbs(g)", "Fiber(g)", "Sugars(g)", "Protein(g)", "WeightWatchersPnts") 
            VALUES ('{dicio["Company"]}', '{dicio["Item"]}', '{dicio["Calories"]}', '{dicio["CaloriesFromFat"]}', '{dicio["TotalFat(g)"]}', '{dicio["SaturatedFat(g)"]}', '{dicio["TransFat(g)"]}', '{dicio["Cholesterol(mg)"]}', '{dicio["Sodium(mg)"]}', '{dicio["Carbs(g)"]}', '{dicio["Fiber(g)"]}', '{dicio["Sugars(g)"]}', '{dicio["Protein(g)"]}', '{dicio["WeightWatchersPnts"]}')
        """
        try:
            mycursor.execute(insert_query)
            conn.commit()
            print(f"Valor inserido com sucesso!")        
        except Exception as e:
            print(f"Erro: {e}")

conn.close()