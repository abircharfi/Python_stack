from flask_app.config.mysqlconnection import connectToMySQL , DB

class Dojo: 
    def __init__(self,data):
        self.id= data['id']
        self.name=data['name']
        self.created_at= data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def create(cls,data):
     query="INSERT INTO dojos (name) VALUES (%(name)s)"
     return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def select_all(cls):
     query ="SELECT * from dojos"
     results = connectToMySQL(DB).query_db(query)
     dojos =[]
     for item in results: 

        dojos.append(cls(item))

     return dojos

    @classmethod
    def get_one_dojo(cls,data):
     query="SELECT * from dojos where id=%(id)s;"
     results = connectToMySQL(DB).query_db(query,data)
     dojo =None
     if results != []:
        dojo=cls(results[0])
     return dojo

    @classmethod
    def update_dojo(cls,data):
     query="UPDATE dojos SET name=%(name)s WHERE id =%(id)s"
     return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete_dojo(cls,data):
     query ="DELETE FROM dojos WHERE id=%(id)s"
     return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_by_name(cls, name):
     query = "SELECT * FROM dojos WHERE name = %(name)s LIMIT 1;"
     data = {'name': name}
     result = connectToMySQL(DB).query_db(query, data)
     dojo = None

     if result:
        dojo = cls(result[0])

     return dojo



    




