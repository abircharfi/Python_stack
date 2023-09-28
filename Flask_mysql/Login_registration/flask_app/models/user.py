from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask import flash
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:

    def __init__(self,data):
     self.id = data['id']
     self.first_name = data['first_name']
     self.last_name = data['last_name']
     self.email = data['email']
     self.password= data['password']
     self.created_at = data['created_at']
     self.updated_at = data['updated_at']


    @staticmethod
    def validate_user(user):
        is_valid = True 
        user_in_db = User.get_by_email(user)
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if  not user_in_db :
            flash('Email exist already !')
            is_valid = False
        if len(user['password']) < 9:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['password'] != user['confirm_password']:
           flash("Passwords are not identical.")
           is_valid = False
        return is_valid
    
    
    @classmethod
    def create(cls,data):
       query ="INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
       
       return connectToMySQL('DB').query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
     query = "select * from users ORDER BY users.id DESC LIMIT 1"
     results = connectToMySQL(DB).query_db(query)
     return User(results[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result:
            # user_data = result[0]
            # user = cls(user_data)
            return cls(result[0])
        return False
    
    @classmethod
    def find_by_email_and_password(cls,data):
        query ="select * from users where email=%(email)s and password=%(password)s;"
        return connectToMySQL(DB).query_db(query,data)
       

      
