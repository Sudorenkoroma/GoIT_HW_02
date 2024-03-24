from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb+srv://sudorenkoroma:sudorenkoroma@cluster0.vcn7idw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["db02"]
collection = db["cats"]

# Читання: Виведення всіх записів з колекції
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"An error occurred: {e}")

# Читання: Виведення інформації про кота за ім'ям
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("No cat found with that name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Оновлення: Оновити вік кота за ім'ям
def update_cat_age(name, age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.modified_count:
            print("The cat's age was updated.")
        else:
            print("No cat found with that name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Оновлення: Додати нову характеристику до списку features
def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.modified_count:
            print("A new feature was added to the cat.")
        else:
            print("No cat found with that name or the feature already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Видалення: Видалити запис за ім'ям тварини
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("The cat was deleted.")
        else:
            print("No cat found with that name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Видалення: Видалити всі записи з колекції
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Приклади виклику функцій:
# read_all_cats()
# read_cat_by_name("barsik")
# update_cat_age("barsik", 4)
# add_feature_to_cat("barsik", "loves catnip")
# delete_cat_by_name("barsik")
# delete_all_cats()
