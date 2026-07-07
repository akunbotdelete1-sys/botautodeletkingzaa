from pymongo import MongoClient

OLD_URI = "mongodb+srv://rezaakbar426_db_user:anjayalok@bot-telegram.iul3lyl.mongodb.net/?appName=BOT-TELEGRAM"
NEW_URI = "mongodb+srv://akbarzaaa358_db_user:botdelete@cluster0.3haqnda.mongodb.net/?appName=Cluster0"

old = MongoClient(OLD_URI)
new = MongoClient(NEW_URI)

old_db = old["telegram_bot"]
new_db = new["telegram_bot"]

for collection_name in old_db.list_collection_names():
    print(f"Copy {collection_name}...")

    docs = list(old_db[collection_name].find())

    if docs:
        new_db[collection_name].delete_many({})
        new_db[collection_name].insert_many(docs)

print("✅ Semua collection berhasil dipindahkan!")
