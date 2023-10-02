from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.user import User
from flask import flash

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.duration = data ['duration']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        recipe_in_db = User.get_by_id(data)
        if len(data['name'])  < 2:
            flash("Name needs to be longer then 3 characters.")
            is_valid = False
        if len(data['description'])  < 2:
            flash("Desciption needs to be longer then 3 characters.")
            is_valid = False
        if len(data['instructions'])  < 2:
            flash("Instructions needs to be longer then 3 characters.")
            is_valid = False       
        if data['created_at'] == '':
            flash("You should fixe the date.")
            is_valid = False
        if data['duration'] == 8:
            flash("You should define the duration .")
        return is_valid
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        recipe = None
        if results:
            user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at'],
            }
            recipe = cls(results[0])
            recipe.user = User(user_data)
        return recipe
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        if results:
            for row in results:
                user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
                }
                recipe = cls(row)
                recipe.user = User(user_data)
                recipes.append(recipe)
        return recipes
    
    @classmethod 
    def create(cls , data):
        query = "INSERT INTO recipes (name, description, instructions,duration,created_at, user_id) VALUES(%(name)s,%(description)s,%(instructions)s,%(duration)s,%(created_at)s,%(user_id)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description= %(description)s, instructions=%(instructions)s, duration=%(duration)s, created_at=%(created_at)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result