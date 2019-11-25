import pymongo

# from bson.objectid import ObjectId

try:
    client = pymongo.MongoClient()
    print("Connected Successfully!")
except:
    print("Couldn't connect to MongoDB")

# database name: db
db = client["db"]

# created or switched to collection with name: visitor_book
collection = db.visitor_book


def add_to_database(timestamp, visitor, host, check_times):
    entry = {
        "_id": timestamp,
        "visitor": visitor,
        "host": host,
        "check_times": check_times,
    }

    id = collection.insert_one(entry).inserted_id
    return id


def query_from_database(uid):
    return collection.find_one({"_id": uid})


def update_time_in_database(uid, check_times):
    # print(check_times)
    collection.update(
        {"_id": uid}, {"$set": {"check_times": check_times}},
    )


def view_database(admin_id):
    import os
    from dotenv import load_dotenv

    load_dotenv()

    if admin_id == os.getenv("ADMIN_AID"):
        return [str(post) for post in collection.find()]

    return False
