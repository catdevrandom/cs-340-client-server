from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:

    def __init__(self, username, password, host="localhost", port=27017,
                 db_name="aac", collection_name="animals"):
        # Initialize connection to MongoDB with provided credentials
        self.client = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource="admin"
        )
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        # Validate input is a non-empty dictionary
        if not data or not isinstance(data, dict):
            print("Error: data must be a non-empty dictionary.")
            return False
        try:
            # Insert the document into the collection
            result = self.collection.insert_one(data)
            return True if result.acknowledged else False
        except PyMongoError as e:
            print(f"Insert error: {e}")
            return False

    def read(self, query):
        # Validate input is a dictionary
        if query is None or not isinstance(query, dict):
            print("Error: query must be a dictionary.")
            return []
        try:
            # Use find() and convert cursor to list
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Query error: {e}")
            return []
    def update(self, query, update_data):
        # Validate inputs are non-empty dictionaries
        if not query or not isinstance(query, dict):
            print("Error: query must be a non-empty dictionary.")
            return 0
        if not update_data or not isinstance(update_data, dict):
            print("Error: update_data must be a non-empty dictionary.")
            return 0
        try:
            # Update all documents matching the query
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        # Validate input is a non-empty dictionary
        if not query or not isinstance(query, dict):
            print("Error: query must be a non-empty dictionary.")
            return 0
        try:
            # Delete all documents matching the query
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete error: {e}")
            return 0
