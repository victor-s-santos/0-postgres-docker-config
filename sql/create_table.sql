CREATE DATABASE mcdonalds_health_db;
\c mcdonalds_health_db;

CREATE TABLE public.fast_food_nutrition_menu (
    id SERIAL Primary Key,
    Company text NOT NULL,
    Item text NOT NULL,
    Calories FLOAT,
    "CaloriesFromFat" FLOAT,
    "TotalFat(g)" FLOAT,
    "SaturatedFat(g)" FLOAT,
    "TransFat(g)" FLOAT,
    "Cholesterol(mg)" FLOAT,
    "Sodium(mg)" FLOAT,
    "Carbs(g)" FLOAT,
    "Fiber(g)" FLOAT,
    "Sugars(g)" FLOAT,
    "Protein(g)" FLOAT,
    "WeightWatchersPnts" FLOAT
);