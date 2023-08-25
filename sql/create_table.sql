CREATE DATABASE mcdonalds_health_db;
\c mcdonalds_health_db;

CREATE TABLE public.fast_food_nutrition_menu (
    id SERIAL Primary Key,
    "Company" text NOT NULL,
    "Item" text NOT NULL,
    "Calories" text,
    "CaloriesFromFat" text,
    "TotalFat(g)" text,
    "SaturatedFat(g)" text,
    "TransFat(g)" text,
    "Cholesterol(mg)" text,
    "Sodium(mg)" text,
    "Carbs(g)" text,
    "Fiber(g)" text,
    "Sugars(g)" text,
    "Protein(g)" text,
    "WeightWatchersPnts" text
);