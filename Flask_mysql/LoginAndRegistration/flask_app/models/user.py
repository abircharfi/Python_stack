from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)
 
class User:
    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
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
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True 
        user_in_db = User.get_by_email(user)
        if len(user['first_name']) < 3:
            flash("The first name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("the last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if  user_in_db :
            flash('Email exist already !')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['password'] != user['confirm_password']:
           flash("Passwords are not identical.")
           is_valid = False
        return is_valid
    
    
    @classmethod
    def create(cls,data):
       encrypted_password = bcrypt.generate_password_hash(data['password'])
       data = dict(data)
       data['password'] = encrypted_password
       query ="INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
       
       return connectToMySQL('DB').query_db(query,data)
    
    @classmethod
    def get_one(cls):
     query = "select * from users ORDER BY users.id DESC LIMIT 1"
     results = connectToMySQL(DB).query_db(query)
     return User(results[0])
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not User.EMAIL_REGEX.match(data['email']):
            flash("Login: Invalid email format.")
            is_valid = False
        if not user_in_db:
            flash("Login: User with this email doesn't exist.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Login: Password needs to be 8 characters or more.")
            is_valid = False
        if not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Login: Incorrect Password")
            is_valid = False
        return is_valid
        
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result:
            return cls(result[0])
        return False
    
  

      
