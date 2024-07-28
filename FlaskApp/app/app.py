from flask import Flask, request, jsonify
from db import Database


class FlaskApp:

    @property
    def app(self) -> Flask:
        return self._app
  
    @app.setter
    def app(self, app: Flask):
        self._app = app

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.dataBase = Database()
        self.register_endpoints()

    def register_endpoints(self):
        self.app.add_url_rule(rule='/users', endpoint='users', view_func=self.user, methods=['GET', "POST"])
        self.app.add_url_rule(rule='/users/<id>', endpoint='users/<id>', view_func=self.user_by_id, methods=['GET', "PUT", "DELETE"])

    def user_by_id(self, id):

        if request.method == 'GET':
            user = self.dataBase.get_user_by_id(id)
            if user:
                return jsonify(user)
            return jsonify({"Error": "User not found"})         
           
        if request.method == 'PUT':
            updated_user = self.dataBase.update_user_by_id(id, request.form.to_dict())
            if updated_user:
                return jsonify(updated_user)
            return jsonify({"Error": "User not found"})
        
        if request.method == 'DELETE':
            deleteResult = self.dataBase.delete_user_by_id(id)
            if deleteResult.deleted_count > 0:
                return jsonify({"Info":"User deleted"})
            return jsonify({"Error": "User not found"})
        
        return jsonify({"Error": "Method not allowed"})
    def __isValidUserData(self, user_data: dict):
        missing = []
        print(user_data)
        if user_data:
            if not user_data.get("_id"):
                missing.append("_id")
            if not user_data.get("name"):
                missing.append("name")
            if not user_data.get("email"):
                missing.append("email")
            if not user_data.get("password"):
                missing.append("password")
            if len(missing) > 0:
                return None, missing
            return user_data, None
        return None

    def user(self):
        if request.method == 'POST':
            user_data, missing = self.__isValidUserData(request.form.to_dict())
            if user_data:
                if self.dataBase.insert_user(user_data = user_data) is None:
                    return jsonify({"Error": f"User with Id {user_data['_id']} Already Exists!"})            
                return jsonify(user_data)
            return jsonify({"Error":f"Requires {missing} missing parameter"}) 
        if request.method == 'GET':
            return jsonify(self.dataBase.get_all_users())
        return jsonify({"Error":"Method not Allowed"})

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

if  __name__ == "__main__":
    myFlaskApp = FlaskApp()
    myFlaskApp.run(debug=False, host = '0.0.0.0', port=5100)