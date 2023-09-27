from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask import flash

class Dojo:  
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_dojo(data):  
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if data['location'] == '':
            flash("Must choose a location.")
            is_valid = False
        if data['language'] == '':
            flash("Must choose a language.")
            is_valid = False
        if len(data['comments']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comments) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s)"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_one_dojo(cls,data):
     query="SELECT * from dojos where id=%(id)s;"
     results = connectToMySQL(DB).query_db(query,data)
     dojo =None
     if results != []:
        dojo=cls(results[0])
     return dojo