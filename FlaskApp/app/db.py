from pymongo import MongoClient

class Database:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb://db:27017/")
        self.db = self.client["UserDB"]
        self.collection = self.db["UserData"]
    
    def insert_user(self, user_data: dict):
        cur = self.collection.find_one({'_id': user_data['_id']})
        if cur:
            return None
        return self.collection.insert_one(user_data)
    
    def get_user_by_id(self, user_id: str):
        return self.collection.find_one({'_id': user_id})
    
    def update_user_by_id(self,id: int, user_data: dict):
        self.collection.update_one({'_id': id}, {"$set": user_data})
        return self.collection.find_one({'_id': id})
    
    def delete_user_by_id(self, user_id: str):
        return self.collection.delete_one({'_id': user_id})
    
    def get_all_users(self):
        return list(self.collection.find())