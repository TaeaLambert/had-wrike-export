import os
import pymongo


def get_all_collections_mongodb():
    client = pymongo.MongoClient(
        str(os.getenv("DATABASE_URL")) + "&" + str(os.getenv("CA_CERT")),
        authSource="admin",
    )
    db = client[os.getenv("MONGO_DB")]
    return db.list_collection_names()
